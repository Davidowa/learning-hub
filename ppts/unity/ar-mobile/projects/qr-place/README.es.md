# Lectura de QR y colocación para Unity 6.3 LTS

Lee los QR AR:CUBO y AR:ESFERA con ZXing.Net 0.16.11 y toca un plano detectado para colocar figuras de 20 cm. El QR selecciona el contenido; los anclajes locales conservan su posición durante la sesión.

## Abrir y ejecutar

1. Agrega esta carpeta desde Unity Hub y ábrela con Unity 6.3 LTS. La versión registrada es 6000.3.27f1.
2. Espera la descarga de paquetes y la compilación. El asistente crea los recursos de URP y configura Android, XR y las texturas de prueba.
3. Si no se preparan los recursos, ejecuta Tools > AR QR > Preparar proyecto. Revisa los errores de la consola antes de continuar.
4. Abre Assets/Scenes/QrPlacement.unity y presiona Play con Simulate In Editor activado para probar la simulación.
5. Para el celular, selecciona Android en Build Profiles, revisa XR Plug-in Management > Project Validation y usa Build And Run en un dispositivo compatible con ARCore.

El proyecto usa URP 17.3.0, AR Foundation 6.3.5 y ARCore 6.3.5. El asistente agrega AR Background Renderer Feature a AR_Renderer y asigna AR_URP en Graphics y Quality. Instala Android Build Support, SDK, NDK y OpenJDK desde Unity Hub antes de compilar.

## Marcadores y comportamiento

Las imágenes de la carpeta Marcadores y la última página de Guia.es.pdf contienen los QR de ejemplo. En el Editor, los botones decodifican los PNG incluidos y permiten colocar sobre superficies simuladas. En Android, Leer otro QR reactiva el lector; cambiar de código no modifica los objetos colocados. Mover el papel no mueve las figuras y cerrar la aplicación elimina la distribución.

Guia.es.md y Guia.es.pdf contienen la práctica completa y las pruebas físicas. Las fuentes originales están en ../../labs/lab06.es.md. Los archivos del proyecto no deben combinarse con otra práctica: abre cada carpeta como proyecto independiente.

## Validación

Las pruebas automatizadas ejecutan 48 comprobaciones y analizan la sintaxis de 9 scripts para Editor y Android. Usa .NET 10 y ejecuta `dotnet run --project Validation/Validation.csproj` desde esta carpeta. La primera ejecución restaura las dependencias de validación y requiere internet.

VALIDACION.es.md describe los casos y los límites de esas pruebas. La importación y compilación en Unity, el render, el funcionamiento de la cámara y el comportamiento físico deben comprobarse en el Editor y en un celular. El paquete contiene fuentes y la guía; no incluye un APK compilado.
