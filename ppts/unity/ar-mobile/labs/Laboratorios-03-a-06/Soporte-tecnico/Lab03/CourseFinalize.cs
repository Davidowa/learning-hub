using System.IO;
using System.Linq;
using UnityEditor;
using UnityEditor.SceneManagement;
using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.InputSystem.UI;
public static class CourseFinalize
{
 static void Assign(GameObject root)
 {
  var module=root.GetComponentInChildren<InputSystemUIInputModule>(true);var so=new SerializedObject(module);
  var refs=AssetDatabase.LoadAllAssetsAtPath("Assets/Input/AccionesUI.asset").OfType<InputActionReference>().ToArray();
  string[] fields={"m_PointAction","m_LeftClickAction","m_RightClickAction","m_MiddleClickAction","m_ScrollWheelAction","m_MoveAction","m_SubmitAction","m_CancelAction"};
  string[] names={"UI_Point","UI_Click","UI_RightClick","UI_MiddleClick","UI_ScrollWheel","UI_Navigate","UI_Submit","UI_Cancel"};
  for(int i=0;i<fields.Length;i++)so.FindProperty(fields[i]).objectReferenceValue=refs.Single(x=>x.name==names[i]);so.ApplyModifiedPropertiesWithoutUndo();EditorUtility.SetDirty(module);PrefabUtility.RecordPrefabInstancePropertyModifications(module);
 }
 public static void Run()
 {
  AssetDatabase.Refresh();AssetDatabase.SaveAssets();
  var prefab=PrefabUtility.LoadPrefabContents("Assets/Prefabs/Interfaz.prefab");Assign(prefab);PrefabUtility.SaveAsPrefabAsset(prefab,"Assets/Prefabs/Interfaz.prefab");PrefabUtility.UnloadPrefabContents(prefab);
  EditorSceneManager.OpenScene("Assets/Scenes/Laboratorio.unity");Assign(UnityEngine.Object.FindFirstObjectByType<LabUI>().gameObject);EditorSceneManager.SaveScene(EditorSceneManager.GetActiveScene());
  var root=new GameObject("ModeloAlternativo");var collider=root.AddComponent<BoxCollider>();collider.size=Vector3.one;
  var model=UnityEngine.Object.Instantiate(AssetDatabase.LoadAssetAtPath<GameObject>("Assets/Modelos/PiramideEjemplo.obj"));model.name="MallaImportada";model.transform.SetParent(root.transform,false);
  foreach(var renderer in model.GetComponentsInChildren<Renderer>())renderer.sharedMaterial=AssetDatabase.LoadAssetAtPath<Material>("Assets/Resources/CubeMaterial.mat");
  PrefabUtility.SaveAsPrefabAsset(root,"Assets/Prefabs/ModeloAlternativo.prefab");UnityEngine.Object.DestroyImmediate(root);AssetDatabase.SaveAssets();Debug.Log("COURSE_FINALIZED");EditorApplication.Exit(0);
 }
}
