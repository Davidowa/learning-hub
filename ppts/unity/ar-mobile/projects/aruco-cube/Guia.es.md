# Práctica 5 · AR · Cubo sobre un marcador ArUco

Esta práctica muestra un cubo de 5 cm sobre un marcador ArUco. Al mover o girar la hoja, el cubo sigue la posición y orientación estimadas del marcador. Si el código deja de detectarse, el cubo se oculta después de 0.35 segundos; al reconocerlo otra vez, vuelve a aparecer.

El proyecto usa Unity 6.3 LTS, URP y AR Foundation para obtener la cámara del celular. El reconocimiento del marcador lo realiza un detector escrito en C#. Esta versión didáctica reconoce únicamente el ID 23 del diccionario DICT_4X4_50, con coincidencia exacta de sus bits. No implementa el diccionario completo ni la corrección de errores de OpenCV.

## Por qué usar un detector de códigos

Una biblioteca de imágenes de ARCore busca características visuales de una imagen de referencia. Google recomienda evitar códigos de barras, QR y patrones repetitivos para ese mecanismo. ArUco usa un borde y una cuadrícula codificada; un detector específico puede identificar el marcador y recuperar sus cuatro esquinas. Registrar el código como una imagen de referencia no equivale a decodificarlo.

En este proyecto, las esquinas se convierten a rayos de la cámara y una homografía permite estimar la pose a partir del tamaño físico del marcador. AR Foundation proporciona la imagen CPU y la proyección de la cámara. No agregues una Reference Image Library ni un AR Tracked Image Manager a esta escena.

## Antes de empezar

- Instala Unity 6.3 LTS con Android Build Support, Android SDK & NDK Tools y OpenJDK desde Unity Hub.
- Usa un celular Android compatible con ARCore, con depuración USB activada y permiso de cámara disponible.
- Imprime el marcador de la última página en tamaño real, sin ajustar a la hoja. El lado del cuadrado negro debe medir 10 cm; el margen blanco queda fuera de esa medida.

El proyecto registra Unity 6000.3.27f1, URP 17.3.0, AR Foundation 6.3.5, ARCore 6.3.5, XR Core Utils 2.5.1, XR Plug-in Management 4.5.3 e Input System 1.11.2. La descarga inicial de paquetes requiere internet. El detector no necesita un servicio externo ni un plugin nativo de OpenCV.

## Parte 1 · Abrir y preparar

1. Descomprime `aruco-cube-unity-6.3.zip` en una carpeta independiente. En Unity Hub, usa Add > Add project from disk y selecciona la carpeta que contiene Assets, Packages y ProjectSettings.
2. Abre el proyecto con Unity 6.3 LTS y espera a que termine la importación y compilación de scripts.
3. El asistente prepara materiales, texturas, URP y ajustes XR. Si no se ejecuta, abre Tools > AR ArUco > Preparar proyecto. Revisa la consola antes de continuar.
4. Abre `Assets/Scenes/Aruco.unity` y selecciona el objeto ArUco AR. El componente ArucoBootstrap debe mostrar Simulate In Editor activado y Marker Side Meters en 0.1.
5. En Project Settings > Graphics y Quality, confirma que AR_URP sea el pipeline activo. Abre Assets/Settings/AR_Renderer y verifica AR Background Renderer Feature. El asistente configura estos recursos.

No hace falta agregar otra cámara. La escena crea la sesión AR, XR Origin, la cámara y el cubo al ejecutarse. La carpeta Marcadores contiene una imagen con margen blanco para imprimir; Assets/Resources/Aruco23.png contiene el cuadrado del marcador sin margen.

## Parte 2 · Simular en el Editor

6. Configura Game con relación 4:3 y presiona Play. Aparece una imagen estática de prueba con el marcador y un cubo superpuesto.
7. Comprueba que el mensaje indique ID 23 reconocido y que los cuatro puntos verdes coincidan con las esquinas exteriores del cuadrado negro. Estos puntos ayudan a revisar la conversión entre imagen y pantalla.
8. Presiona Simular pérdida y espera al menos medio segundo. El cubo debe ocultarse. Presiona Volver a detectar para mostrarlo otra vez.
9. Presiona Ocultar puntos de diagnóstico y vuelve a mostrarlos. El control solo cambia los puntos verdes; no modifica el reconocimiento.
10. Detén Play. Si aparece un error de textura no legible, ejecuta nuevamente Preparar proyecto; el asistente activa Read/Write para las imágenes de prueba.

La simulación usa el mismo detector sobre una imagen fija. No usa la cámara de la computadora ni comprueba el seguimiento físico, el movimiento del papel o la conversión de imagen CPU de un celular.

## Parte 3 · Configurar Android

11. En File > Build Profiles, agrega o selecciona Android y presiona Switch Platform. Instala los módulos Android si Unity no los encuentra.
12. En Project Settings > Player, confirma Input System Package (New) o Both en Active Input Handling. El proyecto configura ARM64, IL2CPP, Minimum API Level 24 y OpenGLES3 como única API gráfica.
13. En XR Plug-in Management > Android, activa ARCore e Initialize XR on Startup. En los ajustes de ARCore, deja Requirement en Required y Depth en Optional.
14. Revisa XR Plug-in Management > Project Validation y resuelve los requisitos pendientes. Esta versión está configurada para orientación vertical.
15. Confirma que Aruco.unity sea la escena habilitada, conecta el celular y selecciona Build And Run. Concede el permiso de cámara cuando se solicite.

## Parte 4 · Verificar el marcador físico

16. Mide con una regla el lado del cuadrado negro impreso. Si no mide 10 cm, corrige la impresión o cambia Marker Side Meters al valor real en metros antes de compilar. Una medida incorrecta cambia la escala y distancia estimadas.
17. Coloca la hoja plana sobre una mesa mate y bien iluminada. Apunta el celular en vertical y deja visibles el borde negro completo y el margen blanco. Acércate hasta que el código ocupe una parte apreciable de la cámara.
18. Espera a que el rastreo AR esté disponible. Comprueba primero los cuatro puntos verdes sobre las esquinas físicas. Si aparecen reflejados verticalmente, prueba el botón Invertir Y de la imagen CPU y conserva la opción que los alinee.
19. Si ninguna opción alinea las esquinas, no des por válida la pose. Revisa la matriz de visualización del proveedor y la orientación del dispositivo antes de continuar; esa correspondencia requiere validación en cada configuración de cámara.
20. Con las esquinas alineadas, observa el cubo sobre el centro del marcador. Mueve la hoja despacio y gírala sobre la mesa: el cubo debe acompañarla, sin quedarse fijo en el entorno.
21. Tapa el código o sácalo del cuadro. El cubo debe ocultarse después de 0.35 segundos sin una detección válida. Vuelve a mostrar todo el marcador para recuperarlo.
22. Prueba una inclinación moderada y luego una mayor distancia. Registra el punto donde se pierde la detección. Una imagen pequeña, desenfocada, reflejada, tapada o muy inclinada puede dejar de reconocerse.

El botón de inversión Y es un ajuste de diagnóstico temporal y vuelve al valor del componente al reiniciar la aplicación. Una vez verificado el celular, puedes guardar la opción en Flip Cpu Image Y del Inspector y compilar de nuevo. El cubo no se guarda al cerrar la app y no permanece visible cuando falta el marcador.

## Cómo se organiza el código

CpuGrayCamera adquiere imágenes CPU de AR Foundation, las convierte a escala de grises y limita su lado mayor a 640 píxeles. El procesamiento se solicita cada 0.2 segundos. La interfaz informa si todavía no hay imagen CPU o si el proveedor no admite la conversión R8.

Aruco23Detector aplica un umbral local, busca componentes y aproxima cuadriláteros. Muestrea una cuadrícula de 6 × 6: borde negro y contenido de 4 × 4. Compara los bits con el ID 23 en cuatro giros y devuelve las esquinas en orden canónico. Solo se usa el marcador reconocido de mayor área.

MarkerGeometry contiene la homografía, la inversión de coordenadas de visualización y la estimación de pose para un cuadrado de tamaño conocido. ArucoBootstrap transforma esa pose al espacio de Unity, coloca el centro del cubo a 2.5 cm sobre el marcador y suaviza los cambios. El asistente ArucoProjectSetup configura URP, Android y ARCore al importar el proyecto.

El detector acepta coincidencias exactas y usa una aproximación planar. No incluye refinamiento subpíxel ni modelado propio de distorsión de lente. Para ampliar el diccionario o mejorar tolerancia a ruido, integra un detector ArUco completo y conserva las pruebas de esquinas, escala y orientación.

## Si algo sale mal

- Si no se reconoce el código, verifica DICT_4X4_50 e ID 23. Otro ID queda fuera del detector de este ejercicio, aunque también sea ArUco.
- Si la detección falla al imprimir, revisa contraste, enfoque y margen blanco. Evita papel brillante y no recortes el borde negro.
- Si el cubo aparece del lado equivocado o desplazado, revisa primero los puntos verdes y el tamaño físico. No compenses ese error moviendo manualmente el cubo.
- Si la cámara tiene un fondo de color, revisa ARCameraBackground, AR Background Renderer Feature y el pipeline asignado en Graphics y Quality.
- Si la interfaz indica rastreo limitado, mueve el celular lentamente por una zona iluminada con detalle antes de volver a enfocar la hoja.
- Si el resultado tiembla, reduce movimiento e inclinación y acerca el marcador. El suavizado disminuye cambios visibles, pero no corrige una detección equivocada.

## Entregable y estado de validación

Entrega un video del celular que muestre la alineación de las cuatro esquinas, el cubo siguiendo la hoja y la pérdida y recuperación del marcador. Incluye una foto de la medida física y anota el ajuste Y usado, el modelo del celular y las condiciones que causaron fallos.

Las pruebas automatizadas ejecutan 34 comprobaciones de detección, esquinas, pose métrica y conversión UV. Incluyen imágenes sintéticas con cuatro giros, perspectiva, desenfoque, ruido, menor iluminación, otro ID, reflexión, oclusión y una imagen vacía. Los cinco scripts pasan el análisis de sintaxis para Editor y Android. La compilación en Unity, la superposición con cámara real, el rendimiento y el APK permanecen pendientes de validación; el ZIP contiene fuentes y no incluye un APK compilado.

## Referencias técnicas

- OpenCV, detección y pose de ArUco: https://docs.opencv.org/4.13.0/d5/dae/tutorial_aruco_detection.html
- Unity, acceso a imágenes CPU de AR Foundation 6.3: https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.3/manual/features/camera/image-capture.html
- Google, selección de imágenes para Augmented Images: https://developers.google.com/ar/develop/augmented-images
