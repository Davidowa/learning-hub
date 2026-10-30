using System.Text.Json;
using ArucoExample;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
string root=Path.GetFullPath(Path.Combine(AppContext.BaseDirectory,"../../../../"));
int count=0;void Check(bool ok,string message){count++;if(!ok)throw new Exception(message);}
var detector=new Aruco23Detector();
using var cases=JsonDocument.Parse(File.ReadAllText(Path.Combine(root,"Validation/Fixtures/cases.json")));
foreach(var test in cases.RootElement.EnumerateArray())
{
 string name=test.GetProperty("name").GetString();
 byte[] bytes=File.ReadAllBytes(Path.Combine(root,"Validation/Fixtures",name+".gray"));
 var found=detector.Detect(bytes,640,480);
 bool positive=test.GetProperty("positive").GetBoolean();
 Check((found!=null)==positive,"Detection mismatch: "+name);
 if(found!=null)
 {
  var corners=test.GetProperty("corners").EnumerateArray().Select(x=>new P2(x[0].GetDouble(),x[1].GetDouble())).ToArray();
  double error=found.Corners.Select((p,i)=>(p-corners[i]).Length).Average();
  Check(error<7,"Corner order or geometry mismatch: "+name+" "+error);
 }
 Console.WriteLine(name+": "+(found!=null?"ID23":"none"));
}
var normalized=new[]{new P2(-.1,-.1),new P2(.1,-.1),new P2(.1,.1),new P2(-.1,.1)};
Check(PlanarPose.TrySolve(normalized,.1,out var pose),"Front pose solves.");
Check(Math.Abs(pose.Translation.Z-.5)<1e-9,"Metric depth uses marker side.");
Check(Math.Abs(pose.Right.X-1)<1e-9 && Math.Abs(pose.Down.Y-1)<1e-9,"Pose axes follow marker.");
Check(PlanarPose.TrySolve(normalized,.2,out var doubled)&&Math.Abs(doubled.Translation.Z-1)<1e-9,"Physical side scales metric depth.");
Check(!PlanarPose.TrySolve(normalized,0,out _),"Reject zero physical size.");
Check(!PlanarPose.TrySolve(new[]{new P2(0,0),new P2(0,0),new P2(0,0),new P2(0,0)},.1,out _),"Reject degenerate pose.");
var right=new P3(Math.Cos(.35),0,-Math.Sin(.35));var down=new P3(0,1,0);var t=new P3(.04,-.02,.6);
var projected=Homography.UnitSquare.Select(p=>{var v=t+right*(p.X*.1)+down*(p.Y*.1);return new P2(v.X/v.Z,v.Y/v.Z);}).ToArray();
Check(PlanarPose.TrySolve(projected,.1,out pose),"Oblique pose solves.");
Check((pose.Translation-t).Length<1e-9 && P3.Dot(pose.Right,right)>.99999,"Oblique pose preserves metric position and rotation.");
Check(UvTransform.TryInverse(1,0,0,0,1,0,new P2(.2,.7),out var uv)&&(uv-new P2(.2,.7)).Length<1e-9,"Identity display UV.");
Check(UvTransform.TryInverse(0,-1,1,1,0,0,new P2(.3,.2),out uv)&&(uv-new P2(.2,.7)).Length<1e-9,"Portrait rotation UV.");
Check(UvTransform.TryInverse(.8,0,.1,0,.6,.2,new P2(.3,.5),out uv)&&(uv-new P2(.25,.5)).Length<1e-9,"Cropped display UV.");
Check(!UvTransform.TryInverse(0,0,0,0,0,0,new P2(.2,.7),out _),"Reject singular display UV.");
int scripts=0;
foreach(var file in Directory.GetFiles(Path.Combine(root,"Assets"),"*.cs",SearchOption.AllDirectories))
{
 foreach(var symbol in new[]{"UNITY_EDITOR","UNITY_ANDROID"})
 {
  var tree=CSharpSyntaxTree.ParseText(File.ReadAllText(file),new CSharpParseOptions(LanguageVersion.CSharp9,preprocessorSymbols:new[]{symbol}));
  var errors=tree.GetDiagnostics().Where(d=>d.Severity==DiagnosticSeverity.Error).ToArray();
  if(errors.Length>0)throw new Exception(string.Join("\n",errors.Select(e=>e.ToString())));
 }
 scripts++;
}
Console.WriteLine($"PASS: {count} detector and pose checks; {scripts} scripts parsed. Unity and device tests remain pending.");
