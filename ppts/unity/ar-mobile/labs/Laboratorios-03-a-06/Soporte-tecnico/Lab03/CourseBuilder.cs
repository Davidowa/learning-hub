using System;
using System.IO;
using System.Linq;
using UnityEditor;
using UnityEditor.SceneManagement;
using UnityEditor.Events;
using UnityEditor.Build;
using UnityEngine;
using UnityEngine.Events;
using UnityEngine.UI;
using UnityEngine.EventSystems;
using UnityEngine.InputSystem;
using UnityEngine.InputSystem.UI;
using UnityEngine.InputSystem.XR;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;
using Unity.XR.CoreUtils;

public static class CourseBuilder
{
 static int lab;static string ns,controllerName;static LabContent content;
 static Type Script(string name)=>Type.GetType(name+", Assembly-CSharp",true);
 static Component Add(GameObject go,string name)=>go.AddComponent(Script(name));
 static void Field(UnityEngine.Object obj,string key,UnityEngine.Object value)
 {var so=new SerializedObject(obj);so.FindProperty(key).objectReferenceValue=value;so.ApplyModifiedPropertiesWithoutUndo();}
 static Material Mat(string name)=>AssetDatabase.LoadAssetAtPath<Material>("Assets/Resources/"+name+".mat");
 static GameObject Save(GameObject go,string name)
 {var result=PrefabUtility.SaveAsPrefabAsset(go,"Assets/Prefabs/"+name+".prefab");UnityEngine.Object.DestroyImmediate(go);return result;}
 static GameObject Primitive(PrimitiveType kind,string name,Material material,Vector3 scale)
 {var go=GameObject.CreatePrimitive(kind);go.name=name;go.transform.localScale=scale;go.GetComponent<Renderer>().sharedMaterial=material;return go;}
 public static void Create()
 {
  lab=int.Parse(File.ReadAllText("LAB.txt").Trim());
  ns=lab==3?"MarkerCapture":lab==4?"MarkerlessPlace":lab==5?"ArucoExample":"QrPlace";
  controllerName=lab==3?"CaptureBootstrap":lab==4?"PlacementBootstrap":lab==5?"ArucoBootstrap":"QrPlacementBootstrap";
  string setup=lab==3?"MarkerCapture.Editor.CaptureProjectSetup":lab==4?"MarkerlessPlace.Editor.PlacementProjectSetup":lab==5?"ArucoExample.Editor.ArucoProjectSetup":"QrPlace.Editor.QrPlacementProjectSetup";
  typeof(CourseBuilder).Assembly.GetType(setup).GetMethod("Prepare").Invoke(null,null);
  Directory.CreateDirectory("Assets/Prefabs");Directory.CreateDirectory("Assets/Input");Directory.CreateDirectory("Assets/Configuracion");AssetDatabase.Refresh();
  foreach(var file in Directory.GetFiles("Assets/Resources","*.png"))
  {var importer=AssetImporter.GetAtPath(file.Replace('\\','/')) as TextureImporter;if(importer==null)continue;importer.npotScale=TextureImporterNPOTScale.None;importer.isReadable=true;importer.textureCompression=TextureImporterCompression.Uncompressed;importer.mipmapEnabled=false;importer.maxTextureSize=1024;importer.SaveAndReimport();}
  content=ScriptableObject.CreateInstance<LabContent>();AssetDatabase.CreateAsset(content,"Assets/Configuracion/ContenidoLab.asset");
  content.contentA=Save(Primitive(PrimitiveType.Cube,"ContenidoA",Mat("CubeMaterial"),Vector3.one),"ContenidoA");
  content.contentB=Save(Primitive(PrimitiveType.Sphere,"ContenidoB",Mat(lab==3?"CapturedMaterial":"SphereMaterial"),Vector3.one),"ContenidoB");
  content.selectedMaterial=Mat("SelectedMaterial");
  if(lab==3)
  {
   var root=new GameObject("Objetivo");var target=Add(root,ns+".CaptureTarget");var visual=new GameObject("Visuales");visual.transform.SetParent(root.transform,false);
   var cube=Primitive(PrimitiveType.Cube,"SinCapturar",Mat("CubeMaterial"),Vector3.one*.06f);cube.transform.SetParent(visual.transform,false);cube.transform.localPosition=Vector3.up*.03f;
   var sphere=Primitive(PrimitiveType.Sphere,"Capturado",Mat("CapturedMaterial"),Vector3.one*.055f);sphere.transform.SetParent(visual.transform,false);sphere.transform.localPosition=Vector3.up*.0275f;sphere.GetComponent<Collider>().enabled=false;sphere.SetActive(false);
   Field(target,"cube",cube);Field(target,"capturedSphere",sphere);Field(target,"visuals",visual);content.captureTarget=Save(root,"Objetivo");
   var ball=Primitive(PrimitiveType.Sphere,"Proyectil",Mat("ProjectileMaterial"),Vector3.one*.04f);ball.GetComponent<Collider>().enabled=false;Add(ball,ns+".CaptureProjectile");
   var trail=ball.AddComponent<TrailRenderer>();trail.sharedMaterial=Mat("ProjectileMaterial");trail.startWidth=.028f;trail.endWidth=.002f;trail.time=.25f;trail.minVertexDistance=.005f;
   content.projectile=Save(ball,"Proyectil");
  }
  else if(lab==5)
  {var cube=Primitive(PrimitiveType.Cube,"ContenidoArUco",Mat("CubeMaterial"),Vector3.one);cube.GetComponent<Collider>().enabled=false;content.arucoVisual=Save(cube,"ContenidoArUco");}
  else
  {var indicator=Primitive(PrimitiveType.Cylinder,"Indicador",Mat("PreviewMaterial"),new Vector3(.1f,.001f,.1f));indicator.GetComponent<Collider>().enabled=false;indicator.layer=2;content.indicator=Save(indicator,"Indicador");}
  GameObject planePrefab=null;
  if(lab==4||lab==6)
  {var plane=new GameObject("PlanoAR",typeof(ARPlane),typeof(MeshFilter),typeof(MeshRenderer),typeof(ARPlaneMeshVisualizer));plane.GetComponent<MeshRenderer>().sharedMaterial=Mat("PlaneMaterial");planePrefab=Save(plane,"PlanoAR");}
  EditorSceneManager.NewScene(NewSceneSetup.EmptyScene,NewSceneMode.Single);
  var manager=new GameObject("Laboratorio");var controller=Add(manager,ns+"."+controllerName);var references=manager.AddComponent<LabSceneReferences>();
  var rig=new GameObject("SistemaAR");
  var session=new GameObject("AR Session",typeof(ARSession),typeof(ARInputManager));session.transform.SetParent(rig.transform,false);
  var originGO=new GameObject("XR Origin");originGO.transform.SetParent(rig.transform,false);var origin=originGO.AddComponent<XROrigin>();
  var offset=new GameObject("Camera Offset");offset.transform.SetParent(originGO.transform,false);var camera=CameraObject("AR Camera",offset.transform);
  camera.gameObject.AddComponent<ARCameraManager>();camera.gameObject.AddComponent<ARCameraBackground>();
  var driver=camera.gameObject.AddComponent<TrackedPoseDriver>();
  var pos=new InputAction("Position",InputActionType.Value,"<HandheldARInputDevice>/devicePosition",expectedControlType:"Vector3");pos.AddBinding("<XRHMD>/centerEyePosition");
  var rot=new InputAction("Rotation",InputActionType.Value,"<HandheldARInputDevice>/deviceRotation",expectedControlType:"Quaternion");rot.AddBinding("<XRHMD>/centerEyeRotation");
  var state=new InputAction("Tracking State",InputActionType.Value,"<HandheldARInputDevice>/trackingState",expectedControlType:"Integer");state.AddBinding("<XRHMD>/trackingState");
  driver.positionInput=new InputActionProperty(pos);driver.rotationInput=new InputActionProperty(rot);driver.trackingStateInput=new InputActionProperty(state);
  origin.Camera=camera;origin.CameraFloorOffsetObject=offset;origin.CameraYOffset=0;
  if(lab==3){var images=originGO.AddComponent<ARTrackedImageManager>();images.referenceLibrary=AssetDatabase.LoadAssetAtPath<XRReferenceImageLibrary>("Assets/Resources/MarkerLibrary.asset");images.requestedMaxNumberOfMovingImages=1;Add(originGO,ns+".TrackedCaptureManager");}
  if(lab==4||lab==6){var planes=originGO.AddComponent<ARPlaneManager>();planes.requestedDetectionMode=PlaneDetectionMode.Horizontal|PlaneDetectionMode.Vertical;planes.planePrefab=planePrefab;originGO.AddComponent<ARRaycastManager>();originGO.AddComponent<ARAnchorManager>();}
  if(lab==5)Add(camera.gameObject,"CodeMarkerExamples.CpuGrayCamera");
  if(lab==6)Add(camera.gameObject,ns+".QrScanner");
  originGO.SetActive(false);session.SetActive(false);
  var savedRig=PrefabUtility.SaveAsPrefabAssetAndConnect(rig,"Assets/Prefabs/SistemaAR.prefab",InteractionMode.AutomatedAction);
  references.arOrigin=originGO;references.arSession=session;references.arCamera=camera;
  references.trackedImages=originGO.GetComponent<ARTrackedImageManager>();references.planes=originGO.GetComponent<ARPlaneManager>();references.raycasts=originGO.GetComponent<ARRaycastManager>();references.anchors=originGO.GetComponent<ARAnchorManager>();
  var simulation=new GameObject("Simulacion");var simCamera=CameraObject("CamaraSimulada",simulation.transform);
  if(lab==4||lab==6)
  {
   simCamera.transform.SetPositionAndRotation(new Vector3(0,1.6f,-2),Quaternion.Euler(27,0,0));Add(simCamera.gameObject,ns+".EditorWalkCamera");
   var floor=Primitive(PrimitiveType.Plane,"Piso",Mat("SimulationMaterial"),new Vector3(2,1,2));floor.transform.SetParent(simulation.transform,false);floor.layer=8;
   var wall=Primitive(PrimitiveType.Cube,"Pared",Mat("SimulationMaterial"),new Vector3(10,3,.05f));wall.transform.SetParent(simulation.transform,false);wall.transform.localPosition=new Vector3(0,1.5f,5);wall.layer=8;
  }
  else if(lab==3)
  {
   var marker=new GameObject("MarcadorSimulado");marker.transform.SetParent(simulation.transform,false);marker.transform.localPosition=new Vector3(0,0,.65f);marker.transform.localRotation=Quaternion.Euler(-90,0,0);
   var card=Primitive(PrimitiveType.Quad,"ImagenMarcador",Mat("MarkerMaterial"),Vector3.one*.16f);card.transform.SetParent(marker.transform,false);card.transform.localRotation=Quaternion.Euler(90,0,0);card.GetComponent<Collider>().enabled=false;references.simulatedMarker=marker.transform;
  }
  else
  {
   var material=new Material(Shader.Find("Universal Render Pipeline/Unlit"));material.mainTexture=AssetDatabase.LoadAssetAtPath<Texture2D>("Assets/Resources/SimulationFrame.png");AssetDatabase.CreateAsset(material,"Assets/Configuracion/SimulationFrame.mat");
   float depth=(480f/(2*Mathf.Tan(30*Mathf.Deg2Rad)))*.1f/220f;float height=2*depth*Mathf.Tan(30*Mathf.Deg2Rad);
   var card=Primitive(PrimitiveType.Quad,"ImagenEstatica",material,new Vector3(height*4/3,height,1));card.transform.SetParent(simulation.transform,false);card.transform.localPosition=new Vector3(0,0,depth);card.GetComponent<Collider>().enabled=false;
  }
  simulation.SetActive(false);PrefabUtility.SaveAsPrefabAssetAndConnect(simulation,"Assets/Prefabs/Simulacion.prefab",InteractionMode.AutomatedAction);references.simulationWorld=simulation;references.simulationCamera=simCamera;
  var uiGO=CreateUI();PrefabUtility.SaveAsPrefabAssetAndConnect(uiGO,"Assets/Prefabs/Interfaz.prefab",InteractionMode.AutomatedAction);var ui=uiGO.GetComponent<LabUI>();
  Connect(ui.primary,controller,lab==3?"LaunchButton":lab==4?"ChooseA":lab==5?"CornersButton":"ReadA");
  Connect(ui.secondary,controller,lab==3?"ResetButton":lab==4?"ChooseB":lab==5?"FlipButton":"ReadB");
  if(lab==4||lab==6){Connect(ui.tertiary,controller,"DeleteButton");Connect(ui.quaternary,controller,"SurfacesButton");}
  if(lab==3||lab==5)Connect(ui.simulation,controller,"TrackingButton");
  Field(controller,"scene",references);Field(controller,"content",content);Field(controller,"ui",ui);
  var light=new GameObject("Luz",typeof(Light));light.GetComponent<Light>().type=LightType.Directional;light.GetComponent<Light>().intensity=.9f;light.transform.rotation=Quaternion.Euler(45,-35,0);RenderSettings.ambientLight=new Color(.65f,.65f,.65f);
  string path="Assets/Scenes/Laboratorio.unity";EditorSceneManager.SaveScene(EditorSceneManager.GetActiveScene(),path);EditorBuildSettings.scenes=new[]{new EditorBuildSettingsScene(path,true)};
  PlayerSettings.SetApplicationIdentifier(NamedBuildTarget.Android,"edu.learninghub.editorlab"+lab.ToString("00"));PlayerSettings.productName="Lab"+lab.ToString("00")+" Prefabs";PlayerSettings.Android.targetSdkVersion=(AndroidSdkVersions)36;PlayerSettings.stripEngineCode=false;
  EditorUtility.SetDirty(content);AssetDatabase.SaveAssets();Debug.Log("COURSE_CREATED Lab"+lab);EditorApplication.Exit(0);
 }
 static Camera CameraObject(string name,Transform parent)
 {var go=new GameObject(name,typeof(Camera),typeof(AudioListener));go.transform.SetParent(parent,false);go.tag="MainCamera";var cam=go.GetComponent<Camera>();cam.nearClipPlane=.01f;cam.farClipPlane=1000;cam.clearFlags=CameraClearFlags.SolidColor;cam.backgroundColor=new Color(.07f,.09f,.12f);return cam;}
 static void Connect(Button button,Component controller,string method)
 {UnityEventTools.AddPersistentListener(button.onClick,(UnityAction)Delegate.CreateDelegate(typeof(UnityAction),controller,method));PrefabUtility.RecordPrefabInstancePropertyModifications(button);}
 static RectTransform Rect(string name,Transform parent,Vector2 min,Vector2 max,Vector2 pos,Vector2 size)
 {var go=new GameObject(name,typeof(RectTransform));go.transform.SetParent(parent,false);var r=(RectTransform)go.transform;r.anchorMin=min;r.anchorMax=max;r.anchoredPosition=pos;r.sizeDelta=size;return r;}
 static Text TextAt(string name,Transform parent,string label,Vector2 min,Vector2 max,Vector2 pos,Vector2 size,int font=22)
 {var r=Rect(name,parent,min,max,pos,size);var t=r.gameObject.AddComponent<Text>();t.font=Resources.GetBuiltinResource<Font>("LegacyRuntime.ttf");t.fontSize=font;t.text=label;t.color=Color.white;t.alignment=TextAnchor.MiddleCenter;t.raycastTarget=false;return t;}
 static Button ButtonAt(string name,Transform parent,Vector2 pos)
 {var r=Rect(name,parent,new Vector2(.5f,0),new Vector2(.5f,0),pos,new Vector2(480,58));var image=r.gameObject.AddComponent<Image>();image.color=new Color(.08f,.3f,.4f,.96f);var b=r.gameObject.AddComponent<Button>();b.targetGraphic=image;TextAt("Texto",r,name,Vector2.zero,Vector2.one,Vector2.zero,Vector2.zero);return b;}
 static GameObject CreateUI()
 {
  var root=new GameObject("Interfaz",typeof(RectTransform),typeof(Canvas),typeof(CanvasScaler),typeof(GraphicRaycaster),typeof(LabUI));root.GetComponent<Canvas>().renderMode=RenderMode.ScreenSpaceOverlay;
  var scaler=root.GetComponent<CanvasScaler>();scaler.uiScaleMode=CanvasScaler.ScaleMode.ScaleWithScreenSize;scaler.referenceResolution=new Vector2(540,960);scaler.screenMatchMode=CanvasScaler.ScreenMatchMode.MatchWidthOrHeight;scaler.matchWidthOrHeight=.5f;
  var ui=root.GetComponent<LabUI>();
  var panel=Rect("PanelEstado",root.transform,new Vector2(.5f,1),new Vector2(.5f,1),new Vector2(0,-90),new Vector2(516,130));panel.gameObject.AddComponent<Image>().color=new Color(.02f,.04f,.08f,.85f);panel.GetComponent<Image>().raycastTarget=true;
  ui.status=TextAt("Estado",panel,"Sigue la guía del laboratorio",Vector2.zero,Vector2.one,Vector2.zero,new Vector2(-20,-12),21);
  ui.primary=ButtonAt("Accion1",root.transform,new Vector2(0,245));ui.secondary=ButtonAt("Accion2",root.transform,new Vector2(0,175));
  ui.tertiary=ButtonAt("Eliminar",root.transform,new Vector2(0,105));ui.quaternary=ButtonAt("Superficies",root.transform,new Vector2(0,35));ui.simulation=ButtonAt("SimularPerdida",root.transform,new Vector2(0,105));
  ui.tertiary.gameObject.SetActive(lab==4||lab==6);ui.quaternary.gameObject.SetActive(lab==4||lab==6);ui.simulation.gameObject.SetActive(lab==3||lab==5);
  if(lab==3)TextAt("Mira",root.transform,"+",new Vector2(.5f,.5f),new Vector2(.5f,.5f),Vector2.zero,new Vector2(40,40),28);
  ui.cornerDots=new RectTransform[4];for(int i=0;i<4;i++){var dot=Rect("Esquina"+i,root.transform,Vector2.zero,Vector2.zero,Vector2.zero,new Vector2(10,10));var image=dot.gameObject.AddComponent<Image>();image.color=Color.green;image.raycastTarget=false;ui.cornerDots[i]=dot;dot.gameObject.SetActive(false);}
  var events=new GameObject("EventSystem",typeof(EventSystem),typeof(InputSystemUIInputModule));events.transform.SetParent(root.transform,false);
  var module=events.GetComponent<InputSystemUIInputModule>();var actions=new DefaultInputActions().asset;actions.name="AccionesUI";AssetDatabase.CreateAsset(actions,"Assets/Input/AccionesUI.asset");module.actionsAsset=actions;
  Func<string,InputActionReference> reference=(name)=>{var r=InputActionReference.Create(actions.FindAction(name,true));r.name=name.Replace('/','_');AssetDatabase.AddObjectToAsset(r,actions);return r;};
  module.point=reference("UI/Point");module.leftClick=reference("UI/Click");module.rightClick=reference("UI/RightClick");module.middleClick=reference("UI/MiddleClick");module.scrollWheel=reference("UI/ScrollWheel");module.move=reference("UI/Navigate");module.submit=reference("UI/Submit");module.cancel=reference("UI/Cancel");
  return root;
 }
}

