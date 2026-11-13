using System;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Collections.Generic;
using UnityEditor;
using UnityEditor.SceneManagement;
using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.InputSystem.LowLevel;

[InitializeOnLoad]
public static class CourseSmoke
{
 const string Key="CourseSmoke.Active";const BindingFlags Flags=BindingFlags.Instance|BindingFlags.NonPublic|BindingFlags.Public;
 static List<string> checks=new();static string error;
 static CourseSmoke(){if(SessionState.GetBool(Key,false)){EditorApplication.update+=WaitForPlay;Application.logMessageReceived+=Log;}}
 static void WaitForPlay()
 {
  if(!EditorApplication.isPlaying||Time.time<.1f)return;
  var loop=UnityEngine.LowLevel.PlayerLoop.GetCurrentPlayerLoop();
  for(int i=0;i<loop.subSystemList.Length;i++)if(loop.subSystemList[i].type==typeof(UnityEngine.PlayerLoop.Update))
  {
   var list=loop.subSystemList[i].subSystemList.ToList();
   list.Add(new UnityEngine.LowLevel.PlayerLoopSystem{type=typeof(CourseSmoke),updateDelegate=Tick});
   loop.subSystemList[i].subSystemList=list.ToArray();break;
  }
  UnityEngine.LowLevel.PlayerLoop.SetPlayerLoop(loop);EditorApplication.update-=WaitForPlay;
 }
 public static void Run()
 {
  SessionState.SetBool(Key,true);SessionState.SetInt("CourseSmoke.Step",0);SessionState.SetBool("CourseSmoke.Release",false);SessionState.SetFloat("CourseSmoke.Deadline",0);SessionState.SetFloat("CourseSmoke.Start",(float)EditorApplication.timeSinceStartup);
  EditorSceneManager.OpenScene("Assets/Scenes/Laboratorio.unity");EditorApplication.EnterPlaymode();
 }
 static void Log(string text,string stack,LogType type){if((type==LogType.Error||type==LogType.Exception)&&!stack.Contains("UnityEditor.Search"))error=text+"\n"+stack;}
 static object Field(object obj,string field)=>obj.GetType().GetField(field,Flags).GetValue(obj);
 static object Call(object obj,string method,params object[] args)=>obj.GetType().GetMethod(method,Flags).Invoke(obj,args);
 static void Require(bool value,string message){if(!value)throw new Exception(message);checks.Add("PASS "+message);}
 static int Count()=>UnityEngine.Object.FindObjectsByType<MonoBehaviour>(FindObjectsSortMode.None).Count(x=>x.GetType().Name=="PlacedShape");
 static void Click(UnityEngine.UI.Button button)
 {
  Require(button!=null&&button.interactable&&button.gameObject.activeInHierarchy,"Boton habilitado: "+button.name);
  Canvas.ForceUpdateCanvases();
  Vector2 point=RectTransformUtility.WorldToScreenPoint(null,button.GetComponent<RectTransform>().TransformPoint(button.GetComponent<RectTransform>().rect.center));
  Require(LabUI.BlocksWorld(point),"GraphicRaycaster intercepta el boton "+button.name);
  checks.Add("DEBUG callbacks="+button.onClick.GetPersistentEventCount()+" method="+button.onClick.GetPersistentMethodName(0)+" state="+button.onClick.GetPersistentListenerState(0)+" target="+button.onClick.GetPersistentTarget(0));
  var hits=new List<UnityEngine.EventSystems.RaycastResult>();UnityEngine.EventSystems.EventSystem.current.RaycastAll(new UnityEngine.EventSystems.PointerEventData(UnityEngine.EventSystems.EventSystem.current){position=point},hits);checks.Add("DEBUG click "+point+" top="+hits.FirstOrDefault().gameObject);
  button.onClick.AddListener(()=>Debug.Log("COURSE_CLICK_RECEIVED "+button.name));
  var mouse=InputSystem.devices.OfType<Mouse>().First(x=>x.name=="LabTestMouse");
  InputState.Change(mouse,new MouseState{position=point}.WithButton(MouseButton.Left,true));
  UnityEngine.EventSystems.EventSystem.current.currentInputModule.Process();
  SessionState.SetBool("CourseSmoke.Release",true);
 }
 static void Tick()
 {
  if(!SessionState.GetBool(Key,false))return;
  int lab=int.Parse(File.ReadAllText("LAB.txt").Trim());
  try
  {
   if(EditorApplication.timeSinceStartup-SessionState.GetFloat("CourseSmoke.Start",0)>100)throw new Exception("Timeout del Editor");
   if(!EditorApplication.isPlaying||Time.time<1||Time.time<SessionState.GetFloat("CourseSmoke.Deadline",0))return;
   if(error!=null)throw new Exception(error);
   if(SessionState.GetBool("CourseSmoke.Release",false))
   {
    var mod=UnityEngine.Object.FindFirstObjectByType<UnityEngine.InputSystem.UI.InputSystemUIInputModule>();
    checks.Add("DEBUG point="+mod.point.action.ReadValue<Vector2>()+" enabled="+mod.point.action.enabled+" click="+mod.leftClick.action.ReadValue<float>()+" enabled="+mod.leftClick.action.enabled+" mouse="+InputSystem.devices.OfType<Mouse>().First(x=>x.name=="LabTestMouse").position.ReadValue()+" focused="+UnityEngine.EventSystems.EventSystem.current.isFocused+" module="+UnityEngine.EventSystems.EventSystem.current.currentInputModule);
    var mouse=InputSystem.devices.OfType<Mouse>().First(x=>x.name=="LabTestMouse");InputState.Change(mouse,new MouseState{position=mouse.position.ReadValue()});UnityEngine.EventSystems.EventSystem.current.currentInputModule.Process();SessionState.SetBool("CourseSmoke.Release",false);SessionState.SetFloat("CourseSmoke.Deadline",Time.time+.65f);return;
   }
   var root=UnityEngine.Object.FindObjectsByType<MonoBehaviour>(FindObjectsSortMode.None).First(x=>x.GetType().Name==(lab==3?"CaptureBootstrap":lab==4?"PlacementBootstrap":lab==5?"ArucoBootstrap":"QrPlacementBootstrap"));
   var ui=(LabUI)Field(root,"ui");int step=SessionState.GetInt("CourseSmoke.Step",0);float delay=.25f;
   if(step==0)
   {
    InputSystem.AddDevice<Mouse>("LabTestMouse").MakeCurrent();InputSystem.settings.backgroundBehavior=InputSettings.BackgroundBehavior.IgnoreFocus; InputSystem.settings.editorInputBehaviorInPlayMode=InputSettings.EditorInputBehaviorInPlayMode.AllDeviceInputAlwaysGoesToGameView;
    Require(CourseConfiguration.Problems().Count==0,"Escena configurada: URP, prefabs, un EventSystem y callbacks serializados");
    Require(UnityEngine.Object.FindObjectsByType<Camera>(FindObjectsSortMode.None).Count(x=>x.isActiveAndEnabled)==1,"Una sola camara activa en simulacion");
    if(lab==3)Click(ui.secondary);else Click(ui.primary);
   }
   else if(lab==3)
   {
    var target=UnityEngine.Object.FindObjectsByType<MonoBehaviour>(FindObjectsSortMode.None).First(x=>x.GetType().Name=="CaptureTarget");
    if(step==1){Require(!(bool)target.GetType().GetProperty("IsCaptured").GetValue(target),"Reinicio mediante evento de boton");Click(ui.primary);delay=2f;}
    else if(step==2){Require((bool)target.GetType().GetProperty("IsCaptured").GetValue(target),"Click real de InputSystem lanza prefab y captura el objetivo");Click(ui.simulation);}
    else if(step==3){Require(!(bool)target.GetType().GetProperty("IsTracking").GetValue(target),"Boton de perdida oculta el contenido");Click(ui.simulation);}
    else{Require((bool)target.GetType().GetProperty("IsTracking").GetValue(target),"Boton de recuperacion conserva captura");Finish(true,lab);return;}
   }
   else if(lab==5)
   {
    var cube=(GameObject)Field(root,"cube");
    if(step==1){Require(!(bool)Field(root,"showCorners"),"Boton Canvas cambia diagnostico una sola vez");Require(cube.activeSelf,"Detector reconoce la textura y muestra prefab");Click(ui.simulation);delay=.7f;}
    else if(step==2){Require(!cube.activeSelf,"Perdida oculta prefab");Click(ui.simulation);delay=.7f;}
    else{Require(cube.activeSelf,"Recuperacion muestra prefab");Finish(true,lab);return;}
   }
   else
   {
    var camera=(Camera)Field(root,"viewCamera");
    if(step==1)
    {
     if(lab==6)Require((bool)Field(root,"qrReady"),"Boton decodifica QR cubo con ZXing");
     Physics.SyncTransforms();Vector2 point=camera.WorldToScreenPoint(new Vector3(-1,0,1));Call(root,"HandleTap",point);Require(Count()==1,"Colocacion de prefab A");Click(ui.secondary);
    }
    else if(step==2)
    {
     Require(Count()==1,"Toque en boton no coloca un objeto adicional");
     if(lab==6)Require((bool)Field(root,"qrReady"),"Boton decodifica QR esfera con ZXing");
     Physics.SyncTransforms();Vector2 point=camera.WorldToScreenPoint(new Vector3(1,0,1));Call(root,"HandleTap",point);Require(Count()==2,"Colocacion de prefab B conserva A");
     Physics.SyncTransforms();var item=UnityEngine.Object.FindObjectsByType<MonoBehaviour>(FindObjectsSortMode.None).First(x=>x.GetType().Name=="PlacedShape");point=camera.WorldToScreenPoint(item.transform.TransformPoint(Vector3.up*.1f));Call(root,"HandleTap",point);
    }
    else if(step==3){Click(ui.tertiary);}
    else if(step==4){Require(Count()==1,"Boton elimina solo la seleccion");Click(ui.quaternary);}
    else{Require(Count()==1&&!(bool)Field(root,"showSurfaces"),"Boton oculta superficies sin eliminar figuras");Finish(true,lab);return;}
   }
   SessionState.SetInt("CourseSmoke.Step",step+1);SessionState.SetFloat("CourseSmoke.Deadline",Time.time+delay);
  }
  catch(Exception ex){checks.Add(ex.ToString());Finish(false,lab);}
 }
 static void Finish(bool success,int lab)
 {
  SessionState.SetBool(Key,false);EditorApplication.update-=Tick;Application.logMessageReceived-=Log;
  Directory.CreateDirectory("Validacion");File.WriteAllText("Validacion/Editor.txt",(success?"PASSED":"FAILED")+"\nUnity "+Application.unityVersion+"\n"+string.Join("\n",checks));EditorApplication.Exit(success?0:1);
 }
}
