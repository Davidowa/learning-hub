# Captura AR para Unity 6.3 LTS

El marcador muestra un cubo naranja. La esfera azul lo captura al acertar y una esfera verde ocupa su lugar. El estado se conserva al volver a detectar la imagen y al cerrar la aplicación.

## Abrir y probar

1. Abre esta carpeta desde Unity Hub con Unity 6.3 LTS. La versión registrada es 6000.3.27f1.
2. Espera la descarga de paquetes y la compilación de scripts. La primera importación necesita internet.
3. Ejecuta Tools > AR Capture > Preparar proyecto si el asistente no preparó los recursos automáticamente.
4. Abre Assets/Scenes/Capture.unity y presiona Play. Usa Lanzar o la barra espaciadora para capturar el cubo.
5. Prueba los botones de pérdida de rastreo y reinicio. La simulación del Editor usa un estado separado del celular.

La guía completa está en `Guia.es.md` y `Guia.es.pdf` dentro del paquete de entrega. En el repositorio, su fuente está en `../../labs/lab03.es.md`.

## Android y marcador

El proyecto usa URP 17.3.0 y ARCore; instala Android Build Support, SDK, NDK y OpenJDK desde Unity Hub. Selecciona Android en Build Profiles y revisa Project Validation antes de Build And Run.

Muestra `Assets/Resources/Marker.png` en otra pantalla o imprime `Marker-16cm.pdf` al 100%. Mide el ancho real de la imagen y corrige el tamaño de la entrada `blanco` en `Assets/Resources/MarkerLibrary.asset`. La biblioteca se crea con un ancho de 0.16 m.

Puedes reemplazar la textura de esa entrada por el marcador de la práctica 1. Reinicia su captura y vuelve a medir el ancho antes de compilar.

## Archivos generados en Unity

La primera importación crea MarkerLibrary, cuatro materiales dentro de Resources y los ajustes XR dentro de Assets/XR. El asistente conserva la biblioteca existente para mantener sus identificadores. Se incluye la escena de arranque y el código que crea sus objetos durante la ejecución.

El estado se asocia con el identificador de la imagen en la biblioteca, por lo que conviene conservar esa entrada al ajustar su tamaño. Volver a crear la entrada produce otro identificador y la aplicación puede tratarla como un objetivo nuevo.

## Validación disponible

Desde esta carpeta, ejecuta la siguiente instrucción si tienes .NET 10 y deseas revisar la lógica sin abrir Unity:

```sh
dotnet run --project Validation/Validation.csproj
```

Las pruebas comprueban el estado de captura y analizan la sintaxis de los scripts para Editor y Android. No sustituyen la compilación de Unity ni las pruebas de cámara, renderizado o rastreo. Consulta `VALIDACION.es.md` para conocer el alcance de la revisión realizada.

El paquete contiene código fuente y recursos. No incluye un APK compilado. El avance se guarda de forma local en PlayerPrefs y no se sincroniza entre dispositivos.

El asistente prepara AR_URP y AR_Renderer en Assets/Settings y agrega AR Background Renderer Feature. Ejecuta Preparar proyecto si abres una copia anterior para convertir sus materiales a URP. Revisa Graphics, Quality y la consola antes de compilar.
