using System.IO;
using System.Linq;
using UnityEditor;
using UnityEditor.Build;
using UnityEditor.Build.Reporting;
using UnityEditor.SceneManagement;
using UnityEditor.XR.ARCore;
using UnityEditor.XR.ARSubsystems;
using UnityEditor.XR.Management;
using UnityEditor.XR.Management.Metadata;
using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.InputSystem.XR;
using UnityEngine.Rendering;
using UnityEngine.Rendering.Universal;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;
using UnityEngine.XR.Management;

namespace ImageTrackingExamples.Editor
{
    [InitializeOnLoad]
    public sealed class ImageProjectSetup : IPreprocessBuildWithReport
    {
        const int Practice = 1;
        const string ScenePath = "Assets/Scenes/Practica1AR.unity";
        const string LibraryPath = "Assets/Resources/BibliotecaBlancos.asset";
        const string PreparedPath = "ProjectSettings/ImageProjectPrepared.txt";
        const string RendererPath = "Assets/Settings/AR_Renderer.asset";
        const string PipelinePath = "Assets/Settings/AR_URP.asset";
        public int callbackOrder => -100;

        static ImageProjectSetup()
        {
            EditorApplication.delayCall += () =>
            {
                if (!File.Exists(PreparedPath) && !EditorApplication.isPlayingOrWillChangePlaymode)
                    Prepare();
            };
        }

        [MenuItem("Tools/AR Imágenes/Preparar proyecto")]
        public static void Prepare()
        {
            if (EditorApplication.isPlayingOrWillChangePlaymode) return;
            if (!Application.isBatchMode && !EditorSceneManager.SaveCurrentModifiedScenesIfUserWantsTo()) return;
            Directory.CreateDirectory("Assets/Settings");
            Directory.CreateDirectory("Assets/XR");
            AssetDatabase.Refresh();
            ConfigureImages();
            ConfigurePipeline();
            ConfigureAndroid();
            ConfigureXR();
            ConfigureScene();
            EditorBuildSettings.scenes = new[] { new EditorBuildSettingsScene(ScenePath, true) };
            AssetDatabase.SaveAssets();
            File.WriteAllText(PreparedPath, "Unity 6.3 / URP 17.3 / AR Foundation 6.3.5\n");
            Debug.Log("Práctica " + Practice + " AR preparada. Revisa Project Validation y compila para Android.");
        }

        static void ConfigureImages()
        {
            var library = AssetDatabase.LoadAssetAtPath<XRReferenceImageLibrary>(LibraryPath);
            if (library == null) throw new FileNotFoundException("Falta la biblioteca de imágenes.", LibraryPath);
            for (int i = 0; i < library.count; i++)
            {
                string path = "Assets/Blancos/" + library[i].name + ".png";
                var importer = AssetImporter.GetAtPath(path) as TextureImporter;
                if (importer == null) throw new FileNotFoundException("Falta la imagen de referencia.", path);
                importer.textureType = TextureImporterType.Default;
                importer.isReadable = true;
                importer.mipmapEnabled = false;
                importer.maxTextureSize = 1024;
                importer.textureCompression = TextureImporterCompression.Uncompressed;
                importer.SaveAndReimport();
                // Preserve names, reference identifiers and physical dimensions edited by the student.
                library.SetTexture(i, AssetDatabase.LoadAssetAtPath<Texture2D>(path), true);
            }
            EditorUtility.SetDirty(library);
        }

        static void ConfigurePipeline()
        {
            var renderer = AssetDatabase.LoadAssetAtPath<UniversalRendererData>(RendererPath);
            if (renderer == null)
            {
                renderer = ScriptableObject.CreateInstance<UniversalRendererData>();
                renderer.name = "AR_Renderer";
                AssetDatabase.CreateAsset(renderer, RendererPath);
            }
            renderer.renderingMode = RenderingMode.Forward;
            renderer.depthPrimingMode = DepthPrimingMode.Disabled;
            if (!renderer.rendererFeatures.Any(feature => feature is ARBackgroundRendererFeature))
            {
                var background = ScriptableObject.CreateInstance<ARBackgroundRendererFeature>();
                background.name = "AR Background Renderer Feature";
                AssetDatabase.AddObjectToAsset(background, renderer);
                renderer.rendererFeatures.Add(background);
                background.Create();
            }
            renderer.SetDirty();
            EditorUtility.SetDirty(renderer);
            var pipeline = AssetDatabase.LoadAssetAtPath<UniversalRenderPipelineAsset>(PipelinePath);
            if (pipeline == null)
            {
                pipeline = UniversalRenderPipelineAsset.Create(renderer);
                pipeline.name = "AR_URP";
                AssetDatabase.CreateAsset(pipeline, PipelinePath);
            }
            GraphicsSettings.defaultRenderPipeline = pipeline;
            int previousQuality = QualitySettings.GetQualityLevel();
            for (int i = 0; i < QualitySettings.names.Length; i++)
            {
                QualitySettings.SetQualityLevel(i, false);
                QualitySettings.renderPipeline = pipeline;
            }
            QualitySettings.SetQualityLevel(previousQuality, false);
        }

        static void ConfigureAndroid()
        {
            PlayerSettings.companyName = "LearningHub";
            PlayerSettings.productName = "Práctica " + Practice + " AR";
            PlayerSettings.SetApplicationIdentifier(NamedBuildTarget.Android, "edu.learninghub.practica" + Practice + "ar");
            PlayerSettings.Android.minSdkVersion = AndroidSdkVersions.AndroidApiLevel24;
            PlayerSettings.Android.targetSdkVersion = AndroidSdkVersions.AndroidApiLevelAuto;
            PlayerSettings.Android.targetArchitectures = AndroidArchitecture.ARM64;
            PlayerSettings.SetScriptingBackend(NamedBuildTarget.Android, ScriptingImplementation.IL2CPP);
            PlayerSettings.SetUseDefaultGraphicsAPIs(BuildTarget.Android, false);
            PlayerSettings.SetGraphicsAPIs(BuildTarget.Android, new[] { GraphicsDeviceType.OpenGLES3 });
            PlayerSettings.defaultInterfaceOrientation = UIOrientation.Portrait;
        }

        static void ConfigureXR()
        {
            if (!EditorBuildSettings.TryGetConfigObject(XRGeneralSettings.k_SettingsKey,
                    out XRGeneralSettingsPerBuildTarget settings))
            {
                settings = ScriptableObject.CreateInstance<XRGeneralSettingsPerBuildTarget>();
                AssetDatabase.CreateAsset(settings, "Assets/XR/ImageXRSettings.asset");
                EditorBuildSettings.AddConfigObject(XRGeneralSettings.k_SettingsKey, settings, true);
            }
            if (!settings.HasSettingsForBuildTarget(BuildTargetGroup.Android))
                settings.CreateDefaultSettingsForBuildTarget(BuildTargetGroup.Android);
            if (!settings.HasManagerSettingsForBuildTarget(BuildTargetGroup.Android))
                settings.CreateDefaultManagerSettingsForBuildTarget(BuildTargetGroup.Android);
            var general = settings.SettingsForBuildTarget(BuildTargetGroup.Android);
            general.InitManagerOnStart = true;
            if (!XRPackageMetadataStore.AssignLoader(general.Manager,
                    "UnityEngine.XR.ARCore.ARCoreLoader", BuildTargetGroup.Android))
                throw new BuildFailedException("No se asignó ARCore. Actívalo en XR Plug-in Management > Android.");
            EditorUtility.SetDirty(settings);
            EditorUtility.SetDirty(general);
            EditorUtility.SetDirty(general.Manager);
            var arcore = ARCoreSettings.currentSettings;
            if (arcore == null)
            {
                arcore = ScriptableObject.CreateInstance<ARCoreSettings>();
                AssetDatabase.CreateAsset(arcore, "Assets/XR/ImageARCoreSettings.asset");
                ARCoreSettings.currentSettings = arcore;
            }
            arcore.requirement = ARCoreSettings.Requirement.Required;
            arcore.depth = ARCoreSettings.Requirement.Optional;
            EditorUtility.SetDirty(arcore);
        }

        static void ConfigureScene()
        {
            var scene = EditorSceneManager.OpenScene(ScenePath);
            var camera = scene.GetRootGameObjects().SelectMany(root => root.GetComponentsInChildren<Camera>(true)).Single();
            RenderSettings.ambientMode = AmbientMode.Flat;
            RenderSettings.ambientLight = new Color(0.65f, 0.65f, 0.65f);
            foreach (var root in scene.GetRootGameObjects())
                foreach (var light in root.GetComponentsInChildren<Light>(true))
                    light.transform.rotation = Quaternion.Euler(45f, -30f, 0f);
            camera.GetComponent<ARCameraManager>().requestedFacingDirection = CameraFacingDirection.World;
            var driver = camera.GetComponent<TrackedPoseDriver>();
            if (driver == null) driver = camera.gameObject.AddComponent<TrackedPoseDriver>();
            var position = new InputAction("Position", InputActionType.Value,
                "<XRHMD>/centerEyePosition", expectedControlType: "Vector3");
            position.AddBinding("<HandheldARInputDevice>/devicePosition");
            var rotation = new InputAction("Rotation", InputActionType.Value,
                "<XRHMD>/centerEyeRotation", expectedControlType: "Quaternion");
            rotation.AddBinding("<HandheldARInputDevice>/deviceRotation");
            var tracking = new InputAction("Tracking State", InputActionType.Value,
                "<XRHMD>/trackingState", expectedControlType: "Integer");
            tracking.AddBinding("<HandheldARInputDevice>/trackingState");
            driver.positionInput = new InputActionProperty(position);
            driver.rotationInput = new InputActionProperty(rotation);
            driver.trackingStateInput = new InputActionProperty(tracking);
            camera.GetUniversalAdditionalCameraData().SetRenderer(0);
            EditorUtility.SetDirty(driver);
            EditorSceneManager.MarkSceneDirty(scene);
            EditorSceneManager.SaveScene(scene);
        }

        public void OnPreprocessBuild(BuildReport report)
        {
            if (!File.Exists(PreparedPath) || GraphicsSettings.defaultRenderPipeline == null)
                throw new BuildFailedException("Ejecuta Tools > AR Imágenes > Preparar proyecto antes de compilar.");
            var scenes = EditorBuildSettings.scenes.Where(scene => scene.enabled).ToArray();
            if (scenes.Length != 1 || scenes[0].path != ScenePath)
                throw new BuildFailedException("La lista global debe contener únicamente " + ScenePath + ". Revisa también la lista del perfil activo.");
        }
    }
}
