using System;
using System.IO;
using System.Linq;
using TMPro;
using UnityEditor;
using UnityEditor.Build;
using UnityEditor.Build.Reporting;
using UnityEditor.PackageManager;
using UnityEditor.SceneManagement;
using UnityEditor.XR.Management;
using UnityEditor.XR.Management.Metadata;
using UnityEditor.XR.OpenXR.Features;
using UnityEngine;
using UnityEngine.Rendering;
using UnityEngine.Rendering.Universal;
using UnityEngine.XR.Management;
using UnityEngine.XR.OpenXR;

public sealed class VRLabProjectSetup : IPreprocessBuildWithReport
{
    public const int Lab = __LAB__;
    public const string ScenePath = "Assets/Scenes/__SCENE__.unity";
    const string Prepared = "ProjectSettings/VRLabPrepared.txt";
    public int callbackOrder => -100;

    [InitializeOnLoadMethod]
    static void Initialize()
    {
        EditorApplication.delayCall += () =>
        {
            if (!File.Exists(Prepared) && !EditorApplication.isPlayingOrWillChangePlaymode)
                Prepare();
        };
    }

    [MenuItem("Tools/Learning Hub VR/Preparar proyecto")]
    public static void Prepare()
    {
        if (EditorApplication.isPlayingOrWillChangePlaymode || BuildPipeline.isBuildingPlayer) return;
        if (File.Exists(Prepared) && !Application.isBatchMode &&
            !EditorUtility.DisplayDialog("Reconstruir laboratorio",
                "Se reconstruira la escena de ejemplo. Guarda una copia de tus cambios antes de continuar.",
                "Reconstruir", "Cancelar")) return;
        if (!Application.isBatchMode && !EditorSceneManager.SaveCurrentModifiedScenesIfUserWantsTo()) return;
        try
        {
            if (!EnsureTMP()) return;
            foreach (string path in new[] { "Assets/Scenes", "Assets/Settings", "Assets/XR" })
                Directory.CreateDirectory(path);
            AssetDatabase.Refresh();
            ConfigurePipeline();
            ConfigureAndroid();
            ConfigureXR();
            VRLabSceneBuilder.Build(Lab, ScenePath);
            EditorBuildSettings.scenes = new[] { new EditorBuildSettingsScene(ScenePath, true) };
            AssetDatabase.SaveAssets();
            File.WriteAllText(Prepared, "Unity 6.3 / URP 17.3.0 / XRI 3.3.2 / OpenXR 1.16.1\n");
            Debug.Log("VR-C0" + Lab + " preparado. Revisa Project Validation antes de Build And Run.");
        }
        catch (Exception error)
        {
            Debug.LogException(error);
            Debug.LogError("La preparacion no termino. Corrige el error y usa Tools > Learning Hub VR > Preparar proyecto.");
        }
    }

    static bool EnsureTMP()
    {
        if (AssetDatabase.LoadAssetAtPath<TMP_FontAsset>(
            "Assets/TextMesh Pro/Resources/Fonts & Materials/LiberationSans SDF.asset") != null) return true;
        var package = UnityEditor.PackageManager.PackageInfo.GetAllRegisteredPackages().FirstOrDefault(p => p.name == "com.unity.ugui");
        if (package == null) throw new InvalidOperationException("Falta el paquete Unity UI (UGUI).");
        string path = Directory.GetFiles(package.resolvedPath,
            "TMP Essential Resources.unitypackage", SearchOption.AllDirectories).FirstOrDefault();
        if (path == null) throw new FileNotFoundException("Importa TMP Essential Resources desde Window > TextMeshPro.");
        if (SessionState.GetBool("LearningHub.VR.ImportingTMP", false)) return false;
        SessionState.SetBool("LearningHub.VR.ImportingTMP", true);
        AssetDatabase.importPackageCompleted += TMPImported;
        AssetDatabase.importPackageFailed += TMPFailed;
        AssetDatabase.ImportPackage(path, false);
        return false;
    }

    static void TMPImported(string package)
    {
        SessionState.SetBool("LearningHub.VR.ImportingTMP", false);
        AssetDatabase.importPackageCompleted -= TMPImported;
        AssetDatabase.importPackageFailed -= TMPFailed;
        EditorApplication.delayCall += Prepare;
    }

    static void TMPFailed(string package, string error)
    {
        SessionState.SetBool("LearningHub.VR.ImportingTMP", false);
        AssetDatabase.importPackageCompleted -= TMPImported;
        AssetDatabase.importPackageFailed -= TMPFailed;
        Debug.LogError("No se importaron los recursos TMP: " + error);
    }

    static void ConfigurePipeline()
    {
        const string rendererPath = "Assets/Settings/VR_Renderer.asset";
        const string pipelinePath = "Assets/Settings/VR_URP.asset";
        var renderer = AssetDatabase.LoadAssetAtPath<UniversalRendererData>(rendererPath);
        if (renderer == null)
        {
            renderer = ScriptableObject.CreateInstance<UniversalRendererData>();
            renderer.renderingMode = RenderingMode.Forward;
            AssetDatabase.CreateAsset(renderer, rendererPath);
        }
        var pipeline = AssetDatabase.LoadAssetAtPath<UniversalRenderPipelineAsset>(pipelinePath);
        if (pipeline == null)
        {
            pipeline = UniversalRenderPipelineAsset.Create(renderer);
            AssetDatabase.CreateAsset(pipeline, pipelinePath);
        }
        pipeline.msaaSampleCount = 4;
        pipeline.supportsHDR = false;
        GraphicsSettings.defaultRenderPipeline = pipeline;
        int original = QualitySettings.GetQualityLevel();
        for (int i = 0; i < QualitySettings.names.Length; i++)
        {
            QualitySettings.SetQualityLevel(i, false);
            QualitySettings.renderPipeline = pipeline;
        }
        QualitySettings.SetQualityLevel(original, false);
        EditorUtility.SetDirty(pipeline);
    }

    static void ConfigureAndroid()
    {
        PlayerSettings.companyName = "Learning Hub";
        PlayerSettings.productName = "Laboratorio VR-C0" + Lab;
        PlayerSettings.SetApplicationIdentifier(NamedBuildTarget.Android, "edu.learninghub.vrc0" + Lab);
        PlayerSettings.Android.minSdkVersion = AndroidSdkVersions.AndroidApiLevel29;
        PlayerSettings.Android.targetSdkVersion = AndroidSdkVersions.AndroidApiLevelAuto;
        PlayerSettings.Android.targetArchitectures = AndroidArchitecture.ARM64;
        PlayerSettings.SetScriptingBackend(NamedBuildTarget.Android, ScriptingImplementation.IL2CPP);
        PlayerSettings.SetUseDefaultGraphicsAPIs(BuildTarget.Android, false);
        PlayerSettings.SetGraphicsAPIs(BuildTarget.Android, new[] { GraphicsDeviceType.Vulkan });
        PlayerSettings.colorSpace = ColorSpace.Linear;
    }

    static void ConfigureXR()
    {
        if (!EditorBuildSettings.TryGetConfigObject(XRGeneralSettings.k_SettingsKey,
            out XRGeneralSettingsPerBuildTarget settings))
        {
            settings = ScriptableObject.CreateInstance<XRGeneralSettingsPerBuildTarget>();
            AssetDatabase.CreateAsset(settings, "Assets/XR/VRXRSettings.asset");
            EditorBuildSettings.AddConfigObject(XRGeneralSettings.k_SettingsKey, settings, true);
        }
        if (!settings.HasSettingsForBuildTarget(BuildTargetGroup.Android))
            settings.CreateDefaultSettingsForBuildTarget(BuildTargetGroup.Android);
        if (!settings.HasManagerSettingsForBuildTarget(BuildTargetGroup.Android))
            settings.CreateDefaultManagerSettingsForBuildTarget(BuildTargetGroup.Android);
        var general = settings.SettingsForBuildTarget(BuildTargetGroup.Android);
        general.InitManagerOnStart = true;
        if (!XRPackageMetadataStore.AssignLoader(general.Manager,
            "UnityEngine.XR.OpenXR.OpenXRLoader", BuildTargetGroup.Android))
            throw new BuildFailedException("No se asigno OpenXR. Instala Android Build Support y revisa XR Plug-in Management.");
        FeatureHelpers.RefreshFeatures(BuildTargetGroup.Android);
        var openxr = OpenXRSettings.GetSettingsForBuildTargetGroup(BuildTargetGroup.Android);
        if (openxr == null) throw new BuildFailedException("Activa OpenXR en Android y ejecuta de nuevo la preparacion.");
        foreach (var feature in openxr.GetFeatures())
        {
            if (feature == null) continue;
            string type = feature.GetType().Name;
            if (type == "MetaQuestFeature" || type == "OculusTouchControllerProfile") feature.enabled = true;
            if (type == "OculusQuestFeature") feature.enabled = false;
            EditorUtility.SetDirty(feature);
        }
        openxr.renderMode = OpenXRSettings.RenderMode.SinglePassInstanced;
        EditorUtility.SetDirty(openxr);
        EditorUtility.SetDirty(settings);
        EditorUtility.SetDirty(general);
        EditorUtility.SetDirty(general.Manager);
    }

    public void OnPreprocessBuild(BuildReport report)
    {
        if (!File.Exists(Prepared) || GraphicsSettings.defaultRenderPipeline == null)
            throw new BuildFailedException("Ejecuta Tools > Learning Hub VR > Preparar proyecto antes de compilar.");
        if (report.summary.platform != BuildTarget.Android)
            throw new BuildFailedException("Este proyecto es para Quest autonomo. Selecciona Meta Quest o Android.");
    }
}
