using System;
using System.IO;
using System.Reflection;
using UnityEngine;
using UnityEditor;

public static class LabContentMenuAudit
{
    public static void Run()
    {
        var attr=typeof(LabContent).GetCustomAttribute<CreateAssetMenuAttribute>();
        if(attr==null)throw new Exception("Falta CreateAssetMenuAttribute.");
        if(!AssetDatabase.IsValidFolder("Assets/Configuracion"))AssetDatabase.CreateFolder("Assets","Configuracion");
        Selection.activeObject=AssetDatabase.LoadAssetAtPath<DefaultAsset>("Assets/Configuracion");
        bool menu=EditorApplication.ExecuteMenuItem("Assets/Create/"+attr.menuName);
        AssetDatabase.SaveAssets();
        var created=AssetDatabase.FindAssets("t:LabContent",new[]{"Assets/Configuracion"});
        var check=ScriptableObject.CreateInstance<LabContent>();
        AssetDatabase.CreateAsset(check,"Assets/Configuracion/ContenidoLab-Auditoria.asset");
        AssetDatabase.SaveAssets();
        bool valid=AssetDatabase.LoadAssetAtPath<LabContent>("Assets/Configuracion/ContenidoLab-Auditoria.asset")!=null;
        string report="Class: "+typeof(LabContent).FullName+"\nMenu: Assets/Create/"+attr.menuName+"\nExecuteMenuItem: "+menu+"\nAssets after menu: "+created.Length+"\nScriptableObject serialization: "+valid+"\nUnity: "+Application.unityVersion;
        File.WriteAllText("LabContent-audit.txt",report);Debug.Log(report);
        if(!valid)throw new Exception("No se pudo crear LabContent.");
    }
}
