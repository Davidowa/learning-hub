# Validación del proyecto de colocación

El proyecto usa Unity 6.3 LTS, con AR Foundation y Google ARCore XR Plugin fijados en 6.3.5. El Editor registrado es 6000.3.27f1.

La clase PlacementRegistry pasó 27 comprobaciones con .NET 10. Se probaron la elección de figura, los identificadores únicos, la selección, la eliminación y el rechazo de tipos inválidos. También se revisaron la protección del inventario y la conservación de la elección original durante una colocación pendiente.

Roslyn analizó los cinco scripts de Unity con la sintaxis de C# 9. Se ejecutó el análisis para Editor y Android por separado. La sintaxis no comprueba que todas las referencias se resuelvan dentro del Editor.

Las firmas de AttachAnchor, TryAddAnchorAsync, TryRemoveAnchor, Raycast, GetPlane y trackablesChanged se revisaron en los paquetes oficiales de AR Foundation 6.3.5. La configuración del proveedor se contrastó con el código oficial de ARCore 6.3.5.

## Pruebas pendientes

Unity Editor no está instalado en este Mac. Permanecen pendientes la importación, la compilación, Play Mode, el renderizado de la interfaz y la compilación Android.

La detección de superficies, la estabilidad de los anclajes y el regreso después de caminar requieren pruebas en un celular. La guía describe los pasos para revisar esos comportamientos antes de entregar una aplicación compilada.

Esta versión conserva objetos durante la misma sesión y no los elimina al salir del cuadro ni por su distancia. No garantiza seguimiento a cualquier distancia y no recupera una distribución después de cerrar la aplicación.

El entregable contiene el proyecto fuente y la guía. No se generó un APK.

La guía PDF tiene cuatro páginas. Se revisaron sus páginas renderizadas para comprobar la lectura, los saltos de página y la ausencia de texto cortado.

La configuración se convirtió a URP 17.3.0. Se revisaron el renderer feature del fondo de cámara y los shaders de materiales; la importación y el renderizado dentro de Unity siguen pendientes de prueba.
