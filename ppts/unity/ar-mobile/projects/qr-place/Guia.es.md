# Práctica 6 · AR · Lectura de QR y colocación de figuras

Esta aplicación lee un QR que selecciona un cubo o una esfera. Después de reconocerlo, permite colocar figuras de 20 cm al tocar superficies detectadas por ARCore. Puedes caminar alrededor de los objetos, seleccionarlos y eliminarlos durante la misma sesión.

El QR identifica el contenido. La posición de cada figura se obtiene al tocar un plano detectado y crear un anclaje local, igual que en la práctica 4. Mover o retirar el papel del QR no mueve los objetos colocados. Para un cubo que siga al papel, usa la práctica 5 con ArUco.

## Códigos y alcance

El lector acepta dos textos exactos: AR:CUBO y AR:ESFERA. El primero habilita la colocación de cubos naranjas; el segundo habilita esferas azules. La lectura utiliza ZXing.Net 0.16.11, una biblioteca administrada incluida con su licencia Apache 2.0 y su procedencia. No requiere un plugin de pago ni envía imágenes a un servicio de lectura.

Una vez reconocido un código válido, se pausa el lector para evitar cambios repetidos mientras colocas figuras. El botón Leer otro QR reactiva la lectura; las figuras anteriores permanecen. Un código desconocido muestra un aviso y se ignora. La aplicación no abre enlaces ni ejecuta instrucciones contenidas en el QR.

Los anclajes se conservan durante la sesión mientras ARCore mantiene o recupera el rastreo. No se eliminan por salir del cuadro, pero no hay garantía de estabilidad a cualquier distancia. Cerrar la aplicación o reiniciar la sesión elimina la distribución. Esta versión no implementa oclusión por profundidad ni persistencia para otro día.

## Antes de empezar

- Instala Unity 6.3 LTS con Android Build Support, Android SDK & NDK Tools y OpenJDK desde Unity Hub.
- Usa un celular Android compatible con ARCore, depuración USB y cable de datos. Prepara una mesa o un piso con detalle visual e iluminación suficiente.
- Imprime los dos QR de la última página o muéstralos en otra pantalla. Mantén visible el margen blanco y evita reflejos. No tienen un tamaño físico de calibración obligatorio, porque se usan como identificadores.

La versión registrada es Unity 6000.3.27f1. El proyecto fija URP 17.3.0, AR Foundation 6.3.5, ARCore 6.3.5, XR Core Utils 2.5.1, XR Plug-in Management 4.5.3 e Input System 1.11.2. La primera importación necesita internet para los paquetes; la decodificación del QR ocurre en el dispositivo.

## Parte 1 · Abrir el proyecto

1. Descomprime `qr-place-unity-6.3.zip` en una carpeta independiente. En Unity Hub, usa Add > Add project from disk y selecciona la carpeta con Assets, Packages y ProjectSettings.
2. Abre el proyecto con Unity 6.3 LTS y espera la importación y compilación de los scripts. Revisa los errores de la consola antes de ejecutar.
3. El asistente crea materiales, configura las texturas de ejemplo y prepara URP y XR. Si no se ejecuta, usa Tools > AR QR > Preparar proyecto.
4. Abre `Assets/Scenes/QrPlacement.unity`. Selecciona QR AR y confirma que el componente QrPlacementBootstrap tenga Simulate In Editor activado.
5. En Assets/Settings, revisa AR_URP y AR_Renderer. El renderer debe contener AR Background Renderer Feature y el pipeline debe estar asignado en Graphics y Quality.

No agregues una biblioteca de imágenes para los QR. La lectura se realiza sobre la imagen CPU de la cámara. La escena crea XR Origin, la cámara y los administradores de planos, raycasts y anclajes al ejecutarse.

## Parte 2 · Probar la lectura en el Editor

6. Presiona Play. Aparecen un piso y una pared simulados. Antes de leer un código, un clic sobre el piso debe mostrar el aviso de que primero hace falta un QR.
7. Presiona Leer QR cubo. El botón decodifica el archivo de ejemplo con ZXing; no se limita a cambiar directamente el tipo de figura. Haz clic sobre el piso para colocar un cubo.
8. Presiona Leer QR esfera y haz clic en otro punto. Debe aparecer una esfera sin reemplazar el cubo anterior.
9. Toca una figura para seleccionarla. Cambia a amarillo; usa Eliminar selección para quitarla. Tocar de nuevo una figura seleccionada limpia la selección.
10. Haz clic en Game para darle el foco. Usa W, A, S y D para caminar, Q y E para cambiar la altura, y mantén el botón derecho del mouse para girar. Shift aumenta la velocidad.
11. Aparta la cámara y vuelve a mirar las figuras. Deben permanecer en sus posiciones dentro de la simulación. Oculta y muestra las superficies para comprobar que el control no elimina los objetos.
12. Detén Play. La simulación decodifica los PNG incluidos y comprueba la interacción; no usa una cámara real ni valida los anclajes de ARCore.

Las imágenes de prueba están en Assets/Resources/QrCube.png y QrSphere.png. La carpeta Marcadores contiene copias para imprimir. Si Unity informa que una textura no es legible, ejecuta nuevamente Preparar proyecto para activar Read/Write en estos recursos.

## Parte 3 · Configurar Android

13. En File > Build Profiles, agrega o selecciona Android y presiona Switch Platform. Espera a que termine la importación para esa plataforma.
14. En Project Settings > Player, confirma Input System Package (New) o Both en Active Input Handling. El asistente configura IL2CPP, ARM64, Minimum API Level 24, OpenGLES3 y orientación vertical.
15. Abre XR Plug-in Management > Android y confirma ARCore e Initialize XR on Startup. Deja Requirement en Required y Depth en Optional.
16. Revisa Project Validation y resuelve los requisitos pendientes. Confirma que QrPlacement.unity sea la escena habilitada para la compilación.
17. Conecta el celular, selecciona Build And Run y concede el permiso de cámara. Espera a que la sesión indique rastreo disponible.

## Parte 4 · Leer y colocar en el celular

18. Muestra el QR AR:CUBO completo ante la cámara. Mantén el celular estable y acerca el código si ocupa muy pocos píxeles. La interfaz debe anunciar que el QR de cubo fue leído.
19. Retira la hoja y mueve lentamente el celular para detectar una mesa o el piso. Los planos aparecen en azul y un disco verde marca una superficie bajo el centro de la pantalla.
20. Toca una superficie detectada fuera de los botones. Aparece un cubo de 20 cm apoyado en ella. Puedes colocar otros cubos mientras ese tipo esté activo.
21. Presiona Leer otro QR y muestra AR:ESFERA. Coloca una esfera en un punto diferente. Los cubos anteriores deben conservar su forma y posición.
22. Camina alrededor de las figuras, déjalas fuera de cuadro y vuelve a la zona. Deben reaparecer mientras el rastreo de sus anclajes esté disponible durante la sesión.
23. Selecciona una figura y presiona Eliminar selección. Comprueba que disminuya el contador y que solo desaparezca el objeto seleccionado.
24. Retira o gira el papel del QR después de colocarlas. Las figuras deben permanecer en sus anclajes; el papel ya no controla su posición.
25. Reactiva la lectura y muestra un QR con un texto diferente. Debe aparecer el aviso de contenido no configurado; el código no debe colocar figuras ni abrir enlaces. Usa uno de los ejemplos válidos para continuar.
26. Cierra la aplicación por completo y vuelve a abrirla. La nueva sesión comienza sin figuras y solicita leer un QR otra vez.

La estabilidad depende del entorno y del seguimiento. Si se pierde el rastreo, las figuras cuyos anclajes no estén en Tracking se ocultan temporalmente. Regresa a una zona con detalle y espera; una sesión reiniciada no recupera los objetos anteriores.

## Cómo se organiza el código

CpuGrayCamera obtiene la imagen CPU, la convierte a escala de grises y limita su lado mayor a 640 píxeles. QrScanner solicita la decodificación cada 0.2 segundos mientras la lectura está activa y la sesión tiene seguimiento.

PureQrDecoder configura ZXing para reconocer únicamente QR, con rotación automática y TryHarder. QrPayload acepta los textos exactos configurados y los convierte en Cube o Sphere. Para añadir otro contenido, genera su QR y modifica esa relación; cambiar solo el texto impreso debajo del código no cambia sus datos.

QrPlacementBootstrap coordina lectura, interfaz y colocación. Al tocar un objeto existente, lo selecciona mediante un raycast físico. Para colocar uno nuevo, exige un QR válido y consulta ARRaycastManager dentro de un plano detectado. Intenta AttachAnchor y después TryAddAnchorAsync si hace falta.

PlacedShape crea la geometría y controla selección y seguimiento. PlacementRegistry conserva los identificadores sin modificar las figuras anteriores al leer otro código. QrPlacementProjectSetup configura materiales, texturas, Android, ARCore y URP durante la preparación del proyecto.

La biblioteca administrada está en Assets/Plugins/ZXing. El archivo link.xml conserva la biblioteca durante el stripping de IL2CPP. LICENSE.txt y PROVENANCE.txt registran licencia, versión, descarga y hash del DLL. No sustituyas el archivo por una biblioteca nativa de otra plataforma.

## Si algo sale mal

- Si no se lee el QR, muestra sus cuatro lados y el margen blanco, mejora la iluminación y espera a que la cámara enfoque. Un código pequeño o desenfocado puede no aportar suficientes píxeles.
- Si aparece Sin imagen CPU disponible, espera a que inicie la cámara y revisa el permiso. La vista de cámara y la disponibilidad de una imagen CPU son condiciones distintas.
- Si el lector informa contenido no configurado, comprueba los datos del QR con otro lector. La aplicación distingue mayúsculas y no acepta espacios adicionales.
- Si no cambia de figura al mostrar otro código, presiona Leer otro QR. La pausa después de una lectura válida es parte de la interacción.
- Si se lee el código pero no aparece una figura, toca un plano detectado fuera de la interfaz. La lectura selecciona contenido; el toque determina la posición.
- Si no aparecen planos, enfoca una superficie con detalle y mueve el celular lentamente. El lector de QR y el rastreo de superficies cumplen funciones distintas.
- Si la cámara aparece como un fondo de color, verifica ARCameraBackground, AR Background Renderer Feature y el pipeline asignado.

## Entregable y estado de validación

Entrega un video del celular que muestre ambos QR, la colocación de las dos figuras, un recorrido alrededor de ellas y la eliminación de una. Retira el papel después de colocar para evidenciar que la posición depende del anclaje. Incluye una prueba con un código desconocido y anota el modelo del celular.

Las pruebas automatizadas ejecutan 48 comprobaciones de lectura, datos admitidos e inventario. Incluyen ambos QR en cuatro giros, perspectiva con desenfoque, un QR desconocido, imagen vacía y un búfer inválido. Los nueve scripts pasan el análisis de sintaxis para Editor y Android. La compilación en Unity, el render, el stripping de IL2CPP y los anclajes físicos siguen pendientes de validación en el Editor y en un celular; el ZIP no incluye un APK compilado.

## Referencias técnicas

- ZXing.Net, código y licencia: https://github.com/micjahn/ZXing.Net
- Unity, acceso a imágenes CPU de AR Foundation 6.3: https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.3/manual/features/camera/image-capture.html
- Unity, anclajes de AR Foundation 6.3: https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.3/manual/features/anchors/introduction.html
- Google, selección de imágenes para Augmented Images: https://developers.google.com/ar/develop/augmented-images
