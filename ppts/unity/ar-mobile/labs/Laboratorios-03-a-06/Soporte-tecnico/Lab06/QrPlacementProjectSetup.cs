using System.IO;
using System.Linq;
using UnityEditor;
using UnityEditor.Build;
using UnityEditor.SceneManagement;
using UnityEditor.XR.ARCore;
using UnityEditor.XR.Management;
using UnityEditor.XR.Management.Metadata;
using UnityEngine;
using UnityEngine.Rendering;
using UnityEngine.Rendering.Universal;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.Management;

namespace QrPlace.Editor
{
    public static class QrPlacementProjectSetup
    {
        const string ScenePath = "Assets/Scenes/QrPlacement.unity";
        [MenuItem("Tools/AR QR/Preparar proyecto")]
        public static void Prepare()
        {
            Directory.CreateDirectory("Assets/Resources");
            Directory.CreateDirectory("Assets/XR");
            Directory.CreateDirectory("Assets/Settings");
            AssetDatabase.Refresh();
            ConfigurePipeline();
            MakeMaterial("CubeMaterial", new Color(1f, 0.40f, 0.08f));
            MakeMaterial("SphereMaterial", new Color(0.15f, 0.55f, 1f));
            MakeMaterial("SelectedMaterial", new Color(1f, 0.85f, 0.1f));
            MakeMaterial("PreviewMaterial", new Color(0.1f, 0.9f, 0.3f));
            MakeMaterial("SimulationMaterial", new Color(0.55f, 0.60f, 0.65f));
            var overlay = MakeMaterial("PlaneMaterial", new Color(0.05f, 0.65f, 0.8f, 0.22f));
            overlay.SetFloat("_Surface", 1f);
            overlay.SetOverrideTag("RenderType", "Transparent");
            overlay.EnableKeyword("_SURFACE_TYPE_TRANSPARENT");
            overlay.SetInt("_SrcBlend", (int)BlendMode.SrcAlpha);
            overlay.SetInt("_DstBlend", (int)BlendMode.OneMinusSrcAlpha);
            overlay.SetInt("_SrcBlendAlpha", (int)BlendMode.One);
            overlay.SetInt("_DstBlendAlpha", (int)BlendMode.OneMinusSrcAlpha);
            overlay.SetInt("_ZWrite", 0);
            overlay.DisableKeyword("_ALPHATEST_ON");
            overlay.DisableKeyword("_ALPHAPREMULTIPLY_ON");
            overlay.EnableKeyword("_ALPHABLEND_ON");
            overlay.renderQueue = 3000;
            EditorUtility.SetDirty(overlay);
            ConfigureTextures();
            ConfigureAndroid();
            ConfigureXR();
            EditorBuildSettings.scenes = new[] { new EditorBuildSettingsScene(ScenePath, true) };
            AssetDatabase.SaveAssets();
            if (!Application.isBatchMode) EditorSceneManager.OpenScene(ScenePath);
            Debug.Log("QR AR preparado. Abre QrPlacement.unity y presiona Play para la simulación.");
        }

        static Material MakeMaterial(string name, Color color)
        {
            string path = "Assets/Resources/" + name + ".mat";
            var material = AssetDatabase.LoadAssetAtPath<Material>(path);
            var shader = Shader.Find("Universal Render Pipeline/Lit");
            if (shader == null) throw new System.InvalidOperationException("Falta Universal Render Pipeline/Lit.");
            bool created = material == null;
            if (created) material = new Material(shader) { name = name };
            if (material.shader != shader) material.shader = shader;
            material.color = color;
            if (created) AssetDatabase.CreateAsset(material, path);
            EditorUtility.SetDirty(material);
            return material;
        }

        static void ConfigurePipeline()
        {
            var renderer = AssetDatabase.LoadAssetAtPath<UniversalRendererData>("Assets/Settings/AR_Renderer.asset");
            if (renderer == null)
            {
                renderer = ScriptableObject.CreateInstance<UniversalRendererData>();
                renderer.name = "AR_Renderer";
                AssetDatabase.CreateAsset(renderer, "Assets/Settings/AR_Renderer.asset");
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
            var pipeline = AssetDatabase.LoadAssetAtPath<UniversalRenderPipelineAsset>("Assets/Settings/AR_URP.asset");
            if (pipeline == null)
            {
                pipeline = UniversalRenderPipelineAsset.Create(renderer);
                pipeline.name = "AR_URP";
                AssetDatabase.CreateAsset(pipeline, "Assets/Settings/AR_URP.asset");
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

        static void ConfigureTextures()
        {
            foreach (var name in new[] {"QrCube","QrSphere"})
            {
                var importer = AssetImporter.GetAtPath("Assets/Resources/" + name + ".png") as TextureImporter;
                if (importer == null) continue;
                importer.isReadable = true;
                importer.mipmapEnabled = false;
                importer.textureCompression = TextureImporterCompression.Uncompressed;
                importer.maxTextureSize = 1024;
                importer.SaveAndReimport();
            }
        }

        static void ConfigureAndroid()
        {
            PlayerSettings.stripEngineCode = false;
            PlayerSettings.usePlayerLog = true;
            PlayerSettings.companyName = "LearningHub";
            PlayerSettings.productName = "QR AR";
            PlayerSettings.SetApplicationIdentifier(NamedBuildTarget.Android, "edu.learninghub.qrar");
            PlayerSettings.Android.minSdkVersion = AndroidSdkVersions.AndroidApiLevel25;
            PlayerSettings.Android.targetSdkVersion = (AndroidSdkVersions)36;
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
                AssetDatabase.CreateAsset(settings, "Assets/XR/CodeXRSettings.asset");
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
                Debug.LogWarning("No se asignó ARCore. Actívalo en Project Settings > XR Plug-in Management > Android.");
            EditorUtility.SetDirty(settings);
            EditorUtility.SetDirty(general);
            EditorUtility.SetDirty(general.Manager);
            var arcore = ARCoreSettings.currentSettings;
            if (arcore == null)
            {
                arcore = ScriptableObject.CreateInstance<ARCoreSettings>();
                AssetDatabase.CreateAsset(arcore, "Assets/XR/CodeARCoreSettings.asset");
                ARCoreSettings.currentSettings = arcore;
            }
            arcore.requirement = ARCoreSettings.Requirement.Required;
            arcore.depth = ARCoreSettings.Requirement.Optional;
            EditorUtility.SetDirty(arcore);
        }
    }
}
