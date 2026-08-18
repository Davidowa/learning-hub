# Screenshots of the real product

Every image under `img/en/` that shows an Excel dialog, the ribbon or the VBA editor was
taken from the running application on Windows, by script, with no human at the keyboard. It
is worth writing down how, because the first answer you get when you ask whether this is
possible is usually no, and because the failure modes are specific, silent, and each one
produces a file that looks like a screenshot until you open it.

Nothing here needs a paid tool. It is PowerShell, the Excel COM object model, four
user32 calls and UI Automation, all of which ship with Windows.

## The short version

Three moving parts, and picking the wrong one for the window you are after is what wastes an
afternoon.

1. **Reach the thing.** Drive the ribbon through UI Automation, not keystrokes.
2. **Capture it.** `PrintWindow` for application windows, `CopyFromScreen` for dialogs.
3. **Check what you got.** Reject any frame that comes back mostly dark, before it reaches a
   slide.

## Choosing the capture call

| What you are after | Window class | Capture with | Why |
|---|---|---|---|
| Ribbon, worksheet, task pane, VBA editor | `XLMAIN`, `wndclass_desked_gsk` | `PrintWindow` with `PW_RENDERFULLCONTENT` (flag 2) | Renders the window into a bitmap without touching the z-order, so it works while another app owns the foreground |
| Excel's own dialogs | `bosa_sdm_XL9` (classic), `NUIDialog` (newer) | `CopyFromScreen` over the window rect | Modal dialogs take the foreground themselves, so the glass holds the truth |
| Windows common file dialogs | `#32770` | Neither, see the last section | |

Excel uses **two** dialog classes and this matters. `Format Cells` is `bosa_sdm_XL9`;
`New Formatting Rule` is `NUIDialog`. Search for only one and half the catalogue looks
unreachable. Enumerate on both:

```powershell
if (IsWindowVisible(h) && (cn.StartsWith("bosa_sdm") || cn == "NUIDialog")) { ... }
```

## Reaching the control

Use UI Automation and invoke the button by name. Two rules that are not obvious:

**A tab has to be selected before its buttons exist.** UI Automation only sees the ribbon tab
that is currently active, so `PivotTable` cannot be found while `Home` is showing. Select the
tab first, wait, then look for the button.

**The name is the literal caption, and a button that opens a dialog ends in three dots.** It
is `Sort...`, not `Sort`. It is `Text to Columns...`, `Consolidate...`, `Protect Sheet...`,
`Insert Function...`, `Define Name...`. Do not guess these. Dump them once and keep the list:

```powershell
$cond = New-Object System.Windows.Automation.PropertyCondition(
          $AE::ControlTypeProperty, [System.Windows.Automation.ControlType]::Button)
$root.FindAll([System.Windows.Automation.TreeScope]::Descendants, $cond) |
  ForEach-Object { $_.Current.Name }
```

Prefer `SelectionItemPattern.Select()` for tabs and `InvokePattern.Invoke()` for buttons, and
fall back to `ExpandCollapsePattern.Expand()` for anything that opens a gallery.

For the backstage, invoke the element named `File Tab`, then `Options`, and from inside the
Excel Options dialog invoke its pages by name: `Customize Ribbon`, `Trust Center`. That path
is how the "switch the Developer tab on" screenshot exists.

## The five failure modes

Each of these produced a file that looked fine in a directory listing.

**Keyboard navigation raises other applications.** Driving the ribbon with `Alt` sequences
fires whatever global hotkey another program has registered. A chat client was running here,
its window came to the front, and three captures went out with somebody's private task list
in them. They were deleted rather than shipped. This is the single strongest reason to use UI
Automation instead of `SendKeys`: no `Alt`, no hotkey, no intruder.

**Key tips paint over the ribbon.** Activating a tab with `Alt` leaves the little letter
badges drawn on top of every control. `{ESC}` does not clear them, it moves up one key-tip
layer, and a COM `Range.Select` does not clear them either because the layer belongs to the UI
thread. A real mouse click into the grid does. Or skip the whole problem with UI Automation.

**`SendKeys` cannot type code.** Parentheses are its grouping operators, so
`Range("A1:B1").Select` arrives in the VBA editor as `Range "A1:B1" = True` with a stray
`Select` on its own line. The first VBA editor capture shipped with mangled code. Put the text
on the clipboard and send `^v`.

**`PrintWindow` is blank for some surfaces and `CopyFromScreen` is blind to background
windows.** The ribbon and the VBA editor come back empty under a naive `PrintWindow`, which is
why flag 2, `PW_RENDERFULLCONTENT`, is not optional. Conversely `CopyFromScreen` photographs
whatever is actually on the glass, so if Excel is behind your editor you capture your editor.
`SetForegroundWindow` will not fix that: Windows refuses foreground changes requested by a
background process, and `SetWindowPos` with `HWND_TOPMOST` does not help either. Measured here:
the same crop was 98 per cent dark through `CopyFromScreen` and 2 per cent dark through
`PrintWindow`.

**A modal dialog freezes COM.** Anything that opens one, `ExecuteMso`, `Dialogs(...).Show`,
`GetSaveAsFilename`, blocks the COM call until the dialog closes, and the next COM call fails
with `RPC_E_CALL_REJECTED`. Two ways out. Reach the dialog with UI Automation instead of COM,
which does not block. Or run Excel inside a `Start-Job` and capture from the main thread while
the job sits in the dialog. Dismiss with `{ESC}` and confirm the dialog is gone before the
next COM call; invoking the dialog's own `Cancel` through UI Automation sometimes leaves it
alive.

## The guard that pays for itself

Sample the frame on a grid and refuse it if too much of it is dark. Dialogs and worksheets are
light surfaces, so a dark frame means one of three things: the desktop session is not
interactive, you captured a dark-themed window that was in front, or your crop is off the
window entirely. All three are worth failing loudly for.

```powershell
$step = 19; $dark = 0; $tot = 0
for ($x = 5; $x -lt $bmp.Width - 5; $x += $step) {
  for ($y = 5; $y -lt $bmp.Height - 5; $y += $step) {
    $tot++
    $px = $bmp.GetPixel($x, $y)
    if (($px.R + $px.G + $px.B) -lt 180) { $dark++ }
  }
}
if ($tot -gt 0 -and [double]$dark / $tot -gt 0.25) { throw "capture came back dark" }
```

This caught two frames that were the code editor rather than Excel, and it is what turned a
silent wrong answer into an error message. Run the same sweep over the whole set afterwards,
because it also catches a window that drifted in front of a single shot.

## Worksheet content is a different job

For a picture of cells rather than of the interface, do not screenshot at all. Export and
rasterise, which is deterministic and needs no visible window:

1. `PageSetup`: `PrintGridlines = $true`, `PrintHeadings = $true`, fit to one page, and set
   `PrintArea` to the used range. Headings matter: without them the image cannot say "cell E3".
2. `ExportAsFixedFormat(0, $pdf)`.
3. Rasterise with PyMuPDF at 170 dpi and trim the paper margin with Pillow.

The clipboard route, `Range.CopyPicture` into a chart object and `Chart.Export`, produces a
blank image when Excel is not visible. It is not worth debugging.

## What does not work here

**Windows common file dialogs**, class `#32770`. `Save As` and the `From Text/CSV` picker are
both refused: `PrintWindow` returns 92 to 95 per cent dark, and the window that enumerates
under that class reports a 1280x720 rect at the screen origin, which is not where the dialog
is. The visible dialog is composed elsewhere. Reachable in principle, not solved here.

**Anything needing a macro that has to be created first.** The security bar screenshot exists
because a workbook with macros already lived in the repository and was opened with
`AutomationSecurity = 2`, which makes COM respect the Trust Center the way a human open does.
Writing a macro from scratch needs "Trust access to the VBA project object model" switched on;
with it off, `Workbook.VBProject` is null. Note that `Application.VBE` still answers, so
checking that alone will tell you the door is open when it is not.

## One caveat about language

These images show an English interface, because that is what the editing language of this
machine is set to. The install language being Spanish does not change the captions, and
`FormulaLocal` follows the UI language too, so this machine cannot verify a single Spanish
menu string. Spanish screenshots need a machine with the Spanish language pack. Take them with
the same scripts and write them to `img/es/`.
