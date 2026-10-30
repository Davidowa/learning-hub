using System.Reflection;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using UnityEngine;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;
using Object = UnityEngine.Object;
int checks = 0;
void Check(bool value,string reason) { checks++; if (!value) throw new Exception(reason); }
void Set(object target,string field,object value) => target.GetType().GetField(field,BindingFlags.Instance|BindingFlags.NonPublic).SetValue(target,value);
void Call(object target,string method) => target.GetType().GetMethod(method,BindingFlags.Instance|BindingFlags.NonPublic).Invoke(target,null);
Dictionary<TrackableId,GameObject> Contents(ImageContentController c) => (Dictionary<TrackableId,GameObject>) typeof(ImageContentController).GetField("spawned",BindingFlags.Instance|BindingFlags.NonPublic).GetValue(c);
ARTrackedImage Image(ulong id,string name,TrackingState state) => new() { trackableId = new(id), referenceImage = new() { name = name }, trackingState = state };
var manager = new ARTrackedImageManager();
var controller = new ImageContentController();
Set(controller,"images",manager);
Set(controller,"bindings",new[] {
 new ImageContentController.ImageBinding { imageName="cubo",prefab=new("cube") },
 new ImageContentController.ImageBinding { imageName="esfera",prefab=new("sphere") }
});
Call(controller,"OnEnable");
Check(manager.trackablesChanged.Count == 1,"Subscribe once.");
var cube = Image(1,"cubo",TrackingState.Limited);
void Added(ARTrackedImage image) => manager.trackablesChanged.Invoke(new() { added = { image } });
void Updated(ARTrackedImage image) => manager.trackablesChanged.Invoke(new() { updated = { image } });
Added(cube);
Check(Contents(controller).Count == 0,"Do not spawn on initial Limited.");
cube.trackingState = TrackingState.Tracking;
Updated(cube);
Check(Contents(controller).Count == 1,"Spawn on recovery even when first event was Limited.");
var first = Contents(controller)[cube.trackableId];
Check(first.name == "cube","Choose the cube mapping.");
Check(first.transform.parent == cube.transform,"Follow the image transform.");
Check(first.transform.localPosition == Vector3.zero,"Reset root position.");
Check(first.transform.localRotation == Quaternion.identity,"Reset root rotation.");
Check(first.transform.localScale == Vector3.one,"Reset root scale.");
Added(cube);Updated(cube);
Check(Contents(controller).Count == 1 && ReferenceEquals(first,Contents(controller)[cube.trackableId]),"No duplicates on repeated events.");
cube.trackingState = TrackingState.Limited;Updated(cube);
Check(!first.activeSelf,"Hide Limited.");
cube.trackingState = TrackingState.None;Updated(cube);
Check(!first.activeSelf,"Hide None.");
cube.trackingState = TrackingState.Tracking;Updated(cube);
Check(first.activeSelf,"Recover existing content.");
var sphere=Image(2,"esfera",TrackingState.Tracking);Added(sphere);
Check(Contents(controller)[sphere.trackableId].name == "sphere","Choose sphere explicitly.");
Added(Image(3,"Cubo",TrackingState.Tracking));
Check(Contents(controller).Count == 2,"Names are case sensitive.");
Added(Image(4,"desconocido",TrackingState.Tracking));
Check(Contents(controller).Count == 2,"Unknown image must not fall back to sphere.");
Object.Destroy(first);Updated(cube);
Check(!ReferenceEquals(first,Contents(controller)[cube.trackableId]),"Replace externally destroyed content.");
var lastCube=Contents(controller)[cube.trackableId];
manager.trackablesChanged.Invoke(new() { removed = { new(cube.trackableId,null) } });
Check(lastCube.destroyed && !Contents(controller).ContainsKey(cube.trackableId),"Remove by identifier without dereferencing trackable.");
Check(Contents(controller).ContainsKey(sphere.trackableId),"Removal preserves other image.");
var lastSphere=Contents(controller)[sphere.trackableId];
Call(controller,"OnDisable");
Check(lastSphere.destroyed && Contents(controller).Count == 0,"Disable clears owned instances.");
Check(manager.trackablesChanged.Count == 0,"Disable unsubscribes.");
manager.trackables.Add(sphere);Call(controller,"OnEnable");
Check(Contents(controller).Count == 1,"Re-enable handles already tracked images.");
Check(manager.trackablesChanged.Count == 1,"No duplicate subscription after re-enable.");
Call(controller,"OnDisable");
var empty=new ImageContentController();Call(empty,"OnEnable");
Check(!empty.enabled && Debug.Errors==1,"Missing assignments fail with a diagnostic.");
Call(empty,"OnDisable");
Check(Contents(empty).Count == 0,"Cleanup handles an invalid setup.");
string root=Path.GetFullPath(Path.Combine(AppContext.BaseDirectory,"../../../../"));
int scripts=0;
foreach(var file in Directory.GetFiles(Path.Combine(root,"Assets"),"*.cs",SearchOption.AllDirectories))
{
 foreach(var symbol in new[]{"UNITY_EDITOR","UNITY_ANDROID"})
 {
  var tree=CSharpSyntaxTree.ParseText(File.ReadAllText(file),new CSharpParseOptions(LanguageVersion.CSharp9,preprocessorSymbols:new[]{symbol}));
  var errors=tree.GetDiagnostics().Where(x=>x.Severity==DiagnosticSeverity.Error).ToArray();
  if(errors.Length>0)throw new Exception(string.Join("\n",errors.Select(x=>x.ToString())));
 }
 scripts++;
}
Console.WriteLine($"PASS: {checks} controller assertions with local doubles; {scripts} Unity scripts parsed for Editor and Android.");
Console.WriteLine("Unity compilation, rendering, ARCore and Android build remain untested.");
