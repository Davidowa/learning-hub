using QrPlace;
using System.Text.Json;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;

int count = 0;
void Check(bool condition, string message)
{
    if (!condition) throw new Exception(message);
    count++;
}
var inventory = new PlacementRegistry();
Check(inventory.Items.Count == 0, "A session must start empty.");
Check(inventory.CurrentShape == ShapeKind.Cube, "The default choice must be Cube.");
Check(!inventory.SelectedId.HasValue, "A new session must have no selection.");
Check(!inventory.RemoveSelected().HasValue, "Deleting without a selection must do nothing.");
inventory.Choose(ShapeKind.Sphere);
Check(inventory.CurrentShape == ShapeKind.Sphere, "A shape choice must be retained.");
int sphere = inventory.Add(inventory.CurrentShape);
Check(inventory.Items[sphere] == ShapeKind.Sphere, "The placed type must match the choice.");
Check(!inventory.SelectedId.HasValue, "New placements must not select an unrelated object.");
inventory.Choose(ShapeKind.Cube);
Check(inventory.Items[sphere] == ShapeKind.Sphere, "Changing the choice must not change placed objects.");
int cube = inventory.Add(inventory.CurrentShape);
Check(cube != sphere, "Every placement must get a distinct identifier.");
Check(inventory.Select(cube), "An existing object must be selectable.");
Check(inventory.SelectedId == cube, "The chosen identifier must become the selection.");
Check(!inventory.Select(9999), "An unknown identifier must not be selected.");
Check(inventory.SelectedId == cube, "A failed selection must preserve the current selection.");
Check(inventory.Remove(sphere), "An unselected object can be removed during anchor cleanup.");
Check(inventory.SelectedId == cube, "Removing another object must preserve the selection.");
Check(inventory.RemoveSelected() == cube, "Delete must return the selected identifier.");
Check(inventory.Items.Count == 0, "Only the two created entries should have been removed.");
Check(!inventory.SelectedId.HasValue, "Deleting the selected object must clear selection.");
Check(!inventory.Remove(cube), "Deleting twice must be harmless.");
int next = inventory.Add(ShapeKind.Cube);
Check(next > cube, "Deleted identifiers must not be reused for pending operations.");
inventory.Select(next);
inventory.Deselect();
Check(!inventory.SelectedId.HasValue, "Deselect must clear the identifier.");
Check(inventory.Items.ContainsKey(next), "Deselect must not delete the object.");
var frozenChoice = inventory.CurrentShape;
inventory.Choose(ShapeKind.Sphere);
int pending = inventory.Add(frozenChoice);
Check(inventory.Items[pending] == ShapeKind.Cube, "An asynchronous placement must retain its original choice.");
bool rejectedChoice = false;
try { inventory.Choose((ShapeKind)999); }
catch (ArgumentOutOfRangeException) { rejectedChoice = true; }
Check(rejectedChoice, "An invalid choice must be rejected.");
bool rejectedAdd = false;
try { inventory.Add((ShapeKind)999); }
catch (ArgumentOutOfRangeException) { rejectedAdd = true; }
Check(rejectedAdd, "An invalid placement must be rejected.");
Check(inventory.Items.Count == 2, "Rejected placement must not add a phantom object.");
var exposed = (IDictionary<int, ShapeKind>)inventory.Items;
bool readOnly = false;
try { exposed.Add(100, ShapeKind.Cube); }
catch (NotSupportedException) { readOnly = true; }
Check(readOnly, "External callers must not mutate the inventory view.");

string root = Path.GetFullPath(Path.Combine(AppContext.BaseDirectory, "../../../../"));
using var cases = JsonDocument.Parse(File.ReadAllText(Path.Combine(root,"Validation/Fixtures/cases.json")));
var decoder = new PureQrDecoder();
foreach(var test in cases.RootElement.EnumerateArray())
{
    string name=test.GetProperty("name").GetString();
    string expected=test.GetProperty("payload").ValueKind==JsonValueKind.Null ? null : test.GetProperty("payload").GetString();
    var pixels=File.ReadAllBytes(Path.Combine(root,"Validation/Fixtures",name+".gray"));
    string actual=decoder.Decode(pixels,640,480);
    Check(actual==expected,"QR decode mismatch: "+name+" actual="+actual);
    Console.WriteLine(name+": "+(actual??"none"));
}
Check(QrPayload.TryGetShape("AR:CUBO",out var cubeKind)&&cubeKind==ShapeKind.Cube,"Cube QR maps correctly.");
Check(QrPayload.TryGetShape("AR:ESFERA",out var sphereKind)&&sphereKind==ShapeKind.Sphere,"Sphere QR maps correctly.");
foreach(var invalid in new string[]{null,"","ar:cubo","AR:CUBO ","https://example.com","AR:OTRO"})
    Check(!QrPayload.TryGetShape(invalid,out _),"Unknown payload must be ignored.");
bool invalidImage=false;
try { decoder.Decode(new byte[2],640,480); } catch(ArgumentException) { invalidImage=true; }
Check(invalidImage,"Reject malformed image buffer.");
int scripts = 0;
foreach (var path in Directory.GetFiles(Path.Combine(root, "Assets"), "*.cs", SearchOption.AllDirectories))
{
    foreach (string[] symbols in new[] { new[] { "UNITY_EDITOR" }, new[] { "UNITY_ANDROID" } })
    {
        var options = new CSharpParseOptions(LanguageVersion.CSharp9, preprocessorSymbols: symbols);
        var tree = CSharpSyntaxTree.ParseText(File.ReadAllText(path), options, path);
        var errors = tree.GetDiagnostics().Where(d => d.Severity == DiagnosticSeverity.Error).ToArray();
        if (errors.Length > 0) throw new Exception(string.Join("\n", errors.Select(e => e.ToString())));
    }
    scripts++;
}
Console.WriteLine($"PASS: {count} placement, QR and payload assertions; {scripts} Unity scripts parsed for Editor and Android.");
Console.WriteLine("Unity compilation, AR anchor behavior, rendering and Android build remain device/Editor checks.");
