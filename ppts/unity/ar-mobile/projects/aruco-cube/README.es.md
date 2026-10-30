# Cubo sobre ArUco para Unity 6.3 LTS

Muestra un cubo de 5 cm que sigue al marcador DICT_4X4_50 ID 23. El detector C# incluido reconoce únicamente ese ID y usa su lado físico de 10 cm para estimar la pose. Los demás IDs y diccionarios quedan fuera del ejercicio.

## Abrir y ejecutar

1. Agrega esta carpeta desde Unity Hub y ábrela con Unity 6.3 LTS. La versión registrada es 6000.3.27f1.
2. Espera la descarga de paquetes y la compilación. El asistente crea los recursos de URP y configura Android, XR y las texturas de prueba.
3. Si no se preparan los recursos, ejecuta Tools > AR ArUco > Preparar proyecto. Revisa los errores de la consola antes de continuar.
4. Abre Assets/Scenes/Aruco.unity y presiona Play con Simulate In Editor activado para probar la simulación.
5. Para el celular, selecciona Android en Build Profiles, revisa XR Plug-in Management > Project Validation y usa Build And Run en un dispositivo compatible con ARCore.

El proyecto usa URP 17.3.0, AR Foundation 6.3.5 y ARCore 6.3.5. El asistente agrega AR Background Renderer Feature a AR_Renderer y asigna AR_URP en Graphics y Quality. Instala Android Build Support, SDK, NDK y OpenJDK desde Unity Hub antes de compilar.

## Marcadores y comportamiento

Imprime el marcador de Guia.es.pdf al 100 %. Mide el cuadrado negro, sin incluir el margen blanco: debe tener un lado de 10 cm. El detector usa coincidencia exacta de bits, sin la corrección de errores de OpenCV. Verifica los cuatro puntos verdes en el celular antes de aceptar la pose; el ajuste de inversión Y permite revisar la correspondencia de la imagen CPU con la pantalla. La simulación usa una imagen estática y no prueba una cámara real.

Guia.es.md y Guia.es.pdf contienen la práctica completa y las pruebas físicas. Las fuentes originales están en ../../labs/lab05.es.md. Los archivos del proyecto no deben combinarse con otra práctica: abre cada carpeta como proyecto independiente.

## Validación

Las pruebas automatizadas ejecutan 34 comprobaciones y analizan la sintaxis de 5 scripts para Editor y Android. Usa .NET 10 y ejecuta `dotnet run --project Validation/Validation.csproj` desde esta carpeta. La primera ejecución restaura las dependencias de validación y requiere internet.

VALIDACION.es.md describe los casos y los límites de esas pruebas. La importación y compilación en Unity, el render, el funcionamiento de la cámara y el comportamiento físico deben comprobarse en el Editor y en un celular. El paquete contiene fuentes y la guía; no incluye un APK compilado.
