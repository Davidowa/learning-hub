# Proyecto de la práctica 1: rastreo de imágenes con AR

Una imagen llamada cubo muestra un cubo naranja de 5 cm. El proyecto usa Unity 6.3 LTS (6000.3.27f1), Universal Render Pipeline (URP) 17.3.0, AR Foundation 6.3.5 y Google ARCore XR Plugin 6.3.5.

## Abrir el proyecto

1. Descomprime el ZIP y abre en Unity Hub la carpeta que contiene Assets, Packages y ProjectSettings. No lo importes dentro de otro proyecto.
2. Espera la descarga de paquetes y la compilación de scripts. Unity incluye URP como paquete asociado a su Editor; la primera importación también necesita los paquetes de AR Foundation.
3. El asistente configura URP y ARCore, agrega el seguimiento de la cámara y abre `Assets/Scenes/Practica1AR.unity`. Si no ocurre, ejecuta Tools > AR Imágenes > Preparar proyecto.
4. Revisa la consola y Project Settings > XR Plug-in Management > Project Validation > Android antes de Build And Run. Instala Android Build Support, SDK, NDK y OpenJDK desde Unity Hub si faltan.

Las escenas, los prefabs, los materiales y la biblioteca ya están en Assets. El asistente genera `Assets/Settings/AR_URP.asset` y `AR_Renderer.asset`, agrega AR Background Renderer Feature y registra el proveedor ARCore. Estos ajustes se completan al abrir el proyecto en Unity.

## Imágenes y tamaño físico

La biblioteca `BibliotecaBlancos` está en Assets/Resources. Cada entrada tiene un ancho de 0.16 m y usa una imagen PNG de Assets/Blancos. Muestra cada imagen con un ancho total de 16 cm y mídela con una regla. Si cambias el tamaño mostrado o la impresión, modifica Specify Size en la biblioteca.

No confundas el borde negro interior con el ancho del archivo: los 16 cm corresponden a toda la imagen. La calidad de reconocimiento debe probarse en el celular. La herramienta arcoreimg incluida en ARCore 6.3.5 para macOS es x86_64 y no se pudo ejecutar en este Mac sin Rosetta.

## Escena AR y vista previa

`Practica1AR.unity` contiene AR Session, XR Origin, Camera Offset, AR Camera Manager, AR Camera Background, AR Tracked Image Manager y el controlador de contenido. El asistente completa Tracked Pose Driver con enlaces de posición, rotación y estado del dispositivo. Esta es la única escena incluida en la compilación Android.

ImageContentController coincide con el código de la guía. Busca el nombre exacto de la imagen en Bindings y crea una instancia como hija de su ARTrackedImage. El contenido se muestra en Tracking y se oculta en Limited o None. Ese estado no equivale a una prueba exacta de visibilidad.

Para revisar los modelos en la computadora, abre `Assets/Scenes/VistaPrevia.unity` y presiona Play. Sus botones simulan Tracking y Limited para mostrar u ocultar cada figura. Usa W, A, S y D para moverte, Q y E para cambiar la altura y el botón derecho para girar la cámara. Esta vista previa no ejecuta el controlador AR ni prueba el reconocimiento de imágenes.

## Validación y entrega

La carpeta Validation permite ejecutar las comprobaciones del controlador con `dotnet run --project Validation/Validation.csproj`. Emplea sustitutos locales de las clases de Unity para revisar la selección de prefab, los cambios de estado, la eliminación y la recuperación sin duplicados. También analiza la sintaxis de los scripts para Editor y Android.

La compilación en Unity, el renderizado URP, la detección de imágenes y la aplicación Android siguen pendientes de prueba. No se generó un APK. El ZIP incluye la guía en Markdown y PDF; la práctica 2 incluye también la guía de la primera, necesaria para consultar el código completo del controlador.
