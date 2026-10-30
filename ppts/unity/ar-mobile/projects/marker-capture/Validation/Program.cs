using MarkerCapture;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;

var root = Path.GetFullPath(Path.Combine(AppContext.BaseDirectory, "../../../../"));
int assertions = 0;
void Check(bool condition, string message)
{
    if (!condition) throw new Exception(message);
    assertions++;
}

var store = new MemoryStore();
var game = new CaptureRegistry(store);
Check(!game.IsCaptured("image-a"), "A new image must start uncaptured.");
Check(game.TryCapture("image-a"), "The first hit must capture.");
Check(game.IsCaptured("image-a"), "The captured state must be readable.");
Check(!game.TryCapture("image-a"), "A repeated hit must not capture twice.");
Check(store.Writes == 1, "A repeated hit must not write twice.");
Check(!game.IsCaptured("image-b"), "Capturing A must not capture B.");
Check(game.TryCapture("image-b"), "Another reference image must be independent.");

// A fresh registry represents content recreated after tracking loss or app restart.
var recreated = new CaptureRegistry(store);
Check(recreated.IsCaptured("image-a"), "A fresh registry must restore an existing capture.");
recreated.Reset("image-a");
Check(!game.IsCaptured("image-a"), "Reset must restore the cube state.");
Check(game.IsCaptured("image-b"), "Resetting A must preserve B.");
Check(recreated.TryCapture("image-a"), "A reset target must be capturable again.");
foreach (string invalid in new[] { "", " ", null })
{
    bool rejected = false;
    try { game.TryCapture(invalid); }
    catch (ArgumentException) { rejected = true; }
    Check(rejected, "An empty image key must be rejected.");
}
bool rejectedNullStore = false;
try { _ = new CaptureRegistry(null); }
catch (ArgumentNullException) { rejectedNullStore = true; }
Check(rejectedNullStore, "The capture store must be required.");

int scripts = 0;
foreach (string file in Directory.GetFiles(Path.Combine(root, "Assets"), "*.cs", SearchOption.AllDirectories))
{
    // Syntax checking is separate from a Unity compilation and cannot replace it.
    foreach (string[] symbols in new[] { new[] { "UNITY_EDITOR" }, new[] { "UNITY_ANDROID" } })
    {
        var options = new CSharpParseOptions(LanguageVersion.CSharp9, preprocessorSymbols: symbols);
        var tree = CSharpSyntaxTree.ParseText(File.ReadAllText(file), options, file);
        var errors = tree.GetDiagnostics().Where(d => d.Severity == DiagnosticSeverity.Error).ToArray();
        if (errors.Length > 0) throw new Exception(string.Join("\n", errors.Select(e => e.ToString())));
    }
    scripts++;
}
Console.WriteLine($"PASS: {assertions} capture assertions; {scripts} Unity scripts parsed for Editor and Android.");
Console.WriteLine("Unity compilation, rendering, Android build and AR tracking require the Unity Editor and a device.");

sealed class MemoryStore : ICaptureStore
{
    readonly Dictionary<string, bool> values = new();
    public int Writes { get; private set; }
    public bool Read(string key) => values.TryGetValue(key, out bool captured) && captured;
    public void Write(string key, bool captured)
    {
        values[key] = captured;
        Writes++;
    }
}
