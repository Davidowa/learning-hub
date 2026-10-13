VERSION 1.0 CLASS
BEGIN
  MultiUse = -1
END
Attribute VB_Name = "Empleado"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
Private pSueldo As Double
Public Nombre As String

Public Property Get Sueldo() As Double
    Sueldo = pSueldo
End Property

Public Property Let Sueldo(valor As Double)
    If valor < 0 Then pSueldo = 0 Else pSueldo = valor
End Property

Public Function Anual() As Double
    Anual = pSueldo * 12
End Function
