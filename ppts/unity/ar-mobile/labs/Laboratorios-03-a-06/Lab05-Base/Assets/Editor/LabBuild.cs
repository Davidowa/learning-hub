using System;
using System.IO;
using UnityEditor;
using UnityEditor.Build.Reporting;
using UnityEngine;

public static class LabBuild
{
    [MenuItem("Tools/Laboratorio/Compilar APK Android")]
    public static void Android()
    {
        bool previousExport = EditorUserBuildSettings.exportAsGoogleAndroidProject;
        try
        {
            int lab = int.Parse(File.ReadAllText("LAB.txt").Trim());
            PlayerSettings.Android.targetSdkVersion = (AndroidSdkVersions)36;
            PlayerSettings.stripEngineCode = false;
            PlayerSettings.usePlayerLog = true;
            EditorUserBuildSettings.buildAppBundle = false;
            EditorUserBuildSettings.exportAsGoogleAndroidProject = false;
            AssetDatabase.SaveAssets();
            string folder = Path.GetFullPath(Path.Combine(Application.dataPath, "../../APK"));
            Directory.CreateDirectory(folder);
            string output = Path.Combine(folder, "Lab" + lab.ToString("00") + "-Editor.apk");
            var report = BuildPipeline.BuildPlayer(new BuildPlayerOptions {
                scenes = System.Array.ConvertAll(System.Array.FindAll(EditorBuildSettings.scenes, x => x.enabled), x => x.path),
                locationPathName = output,
                target = BuildTarget.Android,
                options = BuildOptions.None
            });
            if (report.summary.result != BuildResult.Succeeded)
                throw new Exception("La compilacion Android de Unity fallo: " + report.summary.result);
            File.WriteAllText(Path.ChangeExtension(output, ".build.txt"),
                "Unity: " + Application.unityVersion + "\nResultado: " + report.summary.result +
                "\nErrores Unity: " + report.summary.totalErrors + "\nAPK: " + output +
                "\nTamano APK: " + new FileInfo(output).Length + " bytes");
            Debug.Log("LAB_BUILD_SUCCEEDED: " + output);
            EditorUserBuildSettings.exportAsGoogleAndroidProject = previousExport;
            if (Application.isBatchMode) EditorApplication.Exit(0);
        }
        catch (Exception exception)
        {
            EditorUserBuildSettings.exportAsGoogleAndroidProject = previousExport;
            Debug.LogException(exception);
            if (Application.isBatchMode) EditorApplication.Exit(1);
            else throw;
        }
    }

    [MenuItem("Tools/Laboratorio/Exportar y compilar con Gradle (alternativo)")]
    public static void AndroidExportado()
    {
        bool previousExport = EditorUserBuildSettings.exportAsGoogleAndroidProject;
        try
        {
            int lab=int.Parse(File.ReadAllText("LAB.txt").Trim());
            PlayerSettings.Android.targetSdkVersion = (AndroidSdkVersions)36;
            EditorUserBuildSettings.buildAppBundle = false;
            EditorUserBuildSettings.exportAsGoogleAndroidProject = true;
            PlayerSettings.stripEngineCode = false;
            PlayerSettings.usePlayerLog = true;
            AssetDatabase.SaveAssets();
            string folder = Path.GetFullPath(Path.Combine(Application.dataPath, "../../APK"));
            string export = Path.GetFullPath("Build/AndroidGradle");
            Directory.CreateDirectory(folder);
            string label = "Lab"+lab.ToString("00")+"-Editor";
            string output = Path.Combine(folder, label+".apk");
            var report = BuildPipeline.BuildPlayer(new BuildPlayerOptions {
                scenes = System.Array.ConvertAll(System.Array.FindAll(EditorBuildSettings.scenes,x=>x.enabled),x=>x.path),
                locationPathName = export,
                target = BuildTarget.Android,
                options = BuildOptions.None
            });
            if (report.summary.result != BuildResult.Succeeded)
                throw new Exception("La exportacion Android de Unity fallo: " + report.summary.result);
            // Java's local sockets require a normal Windows path, not the 8.3 TEMP alias.
            string javaTemp = Path.GetFullPath(Path.Combine(Application.dataPath, "../../../work"));
            Directory.CreateDirectory(javaTemp);
            javaTemp = javaTemp.Replace(Path.DirectorySeparatorChar, '/');
            string android = Path.Combine(EditorApplication.applicationContentsPath, "PlaybackEngines/AndroidPlayer");
            string java = Path.Combine(android, "OpenJDK/bin/java.exe");
            string launcher = Directory.GetFiles(Path.Combine(android, "Tools/gradle/lib"), "gradle-launcher-*.jar")[0];
            var info = new System.Diagnostics.ProcessStartInfo(java,
                "-classpath \"" + launcher + "\" org.gradle.launcher.GradleMain assembleRelease --no-daemon --max-workers=4") {
                WorkingDirectory = export, UseShellExecute = false, CreateNoWindow = true,
                RedirectStandardOutput = true, RedirectStandardError = true
            };
            info.EnvironmentVariables["TEMP"] = javaTemp;
            info.EnvironmentVariables["TMP"] = javaTemp;
            info.EnvironmentVariables["JAVA_TOOL_OPTIONS"] = "-Djava.io.tmpdir=\"" + javaTemp + "\" -Djdk.net.unixdomain.tmpdir=\"" + javaTemp + "\"";
            using (var process = System.Diagnostics.Process.Start(info))
            {
                var stdout = process.StandardOutput.ReadToEndAsync();
                var stderr = process.StandardError.ReadToEndAsync();
                process.WaitForExit();
                string log = stdout.GetAwaiter().GetResult() + "\n" + stderr.GetAwaiter().GetResult();
                File.WriteAllText(Path.Combine(folder, label + "-gradle.log"), log);
                if (process.ExitCode != 0) throw new Exception("Gradle fallo. Revisa " + label + "-gradle.log");
            }
            File.Copy(Path.Combine(export, "launcher/build/outputs/apk/release/launcher-release.apk"), output, true);
            File.WriteAllText(Path.Combine(folder, label + "-build.txt"),
                "Unity: " + Application.unityVersion + "\nExportacion Unity: " + report.summary.result +
                "\nErrores Unity: " + report.summary.totalErrors + "\nGradle: BUILD SUCCESSFUL\nAPK: " + output +
                "\nTamano APK: " + new FileInfo(output).Length + " bytes\nPlataforma: Android ARM64 / IL2CPP / GLES3 / API 25-36");
            Debug.Log("LAB_BUILD_SUCCEEDED: " + output);
            EditorUserBuildSettings.exportAsGoogleAndroidProject = previousExport;
            if (Application.isBatchMode) EditorApplication.Exit(0);
        }
        catch (Exception exception)
        {
            EditorUserBuildSettings.exportAsGoogleAndroidProject = previousExport;
            Debug.LogException(exception);
            if (Application.isBatchMode) EditorApplication.Exit(1);
            else throw;
        }
    }
}




