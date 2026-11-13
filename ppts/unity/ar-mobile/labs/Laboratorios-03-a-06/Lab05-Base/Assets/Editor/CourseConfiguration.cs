using System;
using System.Linq;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;
using UnityEngine.InputSystem.UI;
using UnityEngine.Rendering;
using UnityEngine.Rendering.Universal;
using UnityEngine.XR.ARFoundation;

public static class CourseConfiguration
{
 [MenuItem("Tools/Laboratorios/Verificar escena (sin modificar)")]
 public static void VerifyMenu()
 {
  var problems=Problems();
  if(problems.Count==0)Debug.Log("CONFIGURACION CORRECTA: referencias, prefabs, URP e interfaz. Falta probar Play y Android.");
  else foreach(var item in problems)Debug.LogError("CONFIGURACION: "+item);
 }
 public static List<string> Problems()
 {
  var p=new List<string>();
  var refs=UnityEngine.Object.FindObjectsByType<LabSceneReferences>(FindObjectsInactive.Include,FindObjectsSortMode.None).FirstOrDefault();
  if(refs==null){p.Add("Agrega LabSceneReferences al objeto Laboratorio y asigna sus campos.");return p;}
  if(refs.arCamera==null||refs.arOrigin==null||refs.arSession==null||refs.simulationCamera==null||refs.simulationWorld==null)p.Add("Faltan referencias AR o de simulación en Laboratorio.");
  var ui=UnityEngine.Object.FindObjectsByType<LabUI>(FindObjectsInactive.Include,FindObjectsSortMode.None).FirstOrDefault();
  var events=UnityEngine.Object.FindObjectsByType<EventSystem>(FindObjectsInactive.Include,FindObjectsSortMode.None);
  if(events.Length!=1)p.Add("Debe haber exactamente un EventSystem en la escena.");
  if(events.Length==1)
  {
   var input=events[0].GetComponent<InputSystemUIInputModule>();
   if(input==null||input.actionsAsset==null||input.point==null||input.leftClick==null)p.Add("EventSystem necesita InputSystemUIInputModule con Actions Asset, Point y Left Click.");
   if(events[0].GetComponent<StandaloneInputModule>()!=null)p.Add("Elimina StandaloneInputModule al usar Input System (New).");
  }
  if(ui==null||ui.status==null)p.Add("Asigna LabUI y su texto Estado.");
  if(ui!=null)
  {
   if(ui.GetComponent<GraphicRaycaster>()==null)p.Add("Falta GraphicRaycaster en el Canvas.");
   foreach(var b in new[]{ui.primary,ui.secondary,ui.tertiary,ui.quaternary,ui.simulation})
   {
    if(b==null||!b.gameObject.activeSelf)continue;
    if(b.onClick.GetPersistentEventCount()!=1||b.onClick.GetPersistentTarget(0)==null||string.IsNullOrEmpty(b.onClick.GetPersistentMethodName(0)))p.Add(b.name+": configura un solo On Click con objeto y método válidos.");
   }
  }
  var pipeline=GraphicsSettings.defaultRenderPipeline as UniversalRenderPipelineAsset;
  if(pipeline==null)p.Add("Asigna AR_URP en Project Settings > Graphics.");
  var renderer=AssetDatabase.LoadAssetAtPath<UniversalRendererData>("Assets/Settings/AR_Renderer.asset");
  if(renderer==null||!renderer.rendererFeatures.Any(x=>x is ARBackgroundRendererFeature))p.Add("El renderer URP necesita AR Background Renderer Feature.");
  foreach(var behaviour in UnityEngine.Object.FindObjectsByType<MonoBehaviour>(FindObjectsInactive.Include,FindObjectsSortMode.None))
  {
   var field=behaviour.GetType().GetField("content");if(field==null)continue;
   var content=field.GetValue(behaviour) as LabContent;
   if(content==null){p.Add("Asigna ContenidoLab al controlador.");continue;}
   string name=behaviour.GetType().Name;
   if(name=="CaptureBootstrap"&&(content.captureTarget==null||content.projectile==null))p.Add("Asigna prefabs Objetivo y Proyectil en ContenidoLab.");
   if((name=="PlacementBootstrap"||name=="QrPlacementBootstrap")&&(content.contentA==null||content.contentB==null||content.indicator==null||content.selectedMaterial==null))p.Add("Asigna Contenido A/B, Indicador y Selected Material.");
   if(name=="ArucoBootstrap"&&content.arucoVisual==null)p.Add("Asigna el prefab Aruco Visual.");
   if(behaviour.GetType().GetField("scene").GetValue(behaviour)==null||behaviour.GetType().GetField("ui").GetValue(behaviour)==null)p.Add("Asigna Scene y UI en el controlador.");
  }
  return p;
 }
}
