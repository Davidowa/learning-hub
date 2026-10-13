Attribute VB_Name = "RuntimeSmoke"
Public Sub SmokeTest()
    Range("A1").Value = "VBA runtime smoke test"
    Range("B1").Value = Application.Version
    Range("C1").Value = 2 + 2
End Sub
