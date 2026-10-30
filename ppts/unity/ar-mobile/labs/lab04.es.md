# Práctica 4 · AR · Colocación sin marcador

Esta aplicación permite elegir un cubo o una esfera y colocarlos sobre superficies detectadas por la cámara. Cada figura queda asociada con un anclaje: puedes caminar a su alrededor, apartar la cámara y volver a buscarla en el lugar donde la colocaste. Al tocar una figura, se selecciona y puedes eliminarla.

El proyecto está preparado para Unity 6.3 LTS y Android con ARCore. Incluye una simulación para probar la interacción en el Editor y una escena AR para el celular. Usa figuras de 20 cm y una interfaz con cuatro controles.

## Alcance de la experiencia

Los objetos permanecen durante la misma sesión. Salir del cuadro de la cámara no los elimina y no hay una regla que los borre por alejarte. El sistema depende del rastreo de ARCore: una zona oscura, una superficie sin detalle o un recorrido largo pueden causar pérdida de seguimiento o desplazamientos de los anclajes.

La experiencia no garantiza conservación a cualquier distancia. Tampoco recupera la distribución después de cerrar la aplicación o reiniciar la sesión AR. Guardar coordenadas locales no proporciona una referencia física recuperable otro día. Esa extensión requiere un mecanismo de persistencia espacial y relocalización, que debe configurarse y probarse por separado.

Esta versión usa anclajes locales y no requiere una cuenta de Google Cloud, credenciales ni carga de mapas del entorno a un servicio externo. No incluye oclusión por profundidad: las paredes reales no tapan automáticamente las figuras virtuales.

## Antes de empezar

- Instala Unity 6.3 LTS con Android Build Support, Android SDK & NDK Tools y OpenJDK desde Unity Hub.
- Usa un celular compatible con ARCore y un cable USB que transfiera datos. Activa la depuración USB y autoriza la conexión a la computadora.
- Elige un espacio iluminado con piso, mesa o paredes que tengan detalle visual. Los reflejos, los vidrios y las superficies uniformes dificultan la detección.

La versión registrada en el proyecto es 6000.3.27f1. Los paquetes AR Foundation y Google ARCore XR Plugin están fijados en 6.3.5. También se incluyen XR Core Utils 2.5.1, XR Plug-in Management 4.5.3 e Input System 1.11.2. Universal Render Pipeline usa la versión 17.3.0, asociada a Unity 6.3.

## Parte 1 · Abrir el proyecto

1. Descomprime `markerless-place-unity-6.3.zip` en una carpeta independiente. Debes encontrar `Assets`, `Packages` y `ProjectSettings` en la carpeta que vas a abrir.
2. En Unity Hub, selecciona Add > Add project from disk, elige esa carpeta y ábrela con Unity 6.3 LTS. La primera importación necesita internet para descargar los paquetes.
3. Espera a que termine la compilación. El asistente prepara los materiales y los ajustes XR cuando falta el material de superficies o la configuración URP.
4. Si los recursos no se prepararon, ejecuta Tools > AR Place > Preparar proyecto. Usa este asistente en la copia independiente del proyecto entregado.
5. Abre `Assets/Scenes/Placement.unity`. La escena contiene un objeto llamado Colocar AR con el componente `PlacementBootstrap`.
6. Revisa Window > General > Console y resuelve los errores rojos antes de continuar. Los avisos de ARCore se revisan en los ajustes Android.

El proyecto usa URP. El asistente crea AR_URP y AR_Renderer en Assets/Settings, agrega AR Background Renderer Feature y asigna el pipeline a Graphics y a los niveles de Quality. Los materiales usan Universal Render Pipeline/Lit; el de superficies conserva transparencia. Si abres una copia de la versión anterior, ejecuta el asistente para convertir sus materiales. La cámara, la sesión AR, las figuras y los administradores se crean al ejecutar la escena. No agregues otra Main Camera ni el contenido del proyecto anterior de captura.

## Parte 2 · Probar en el Editor

7. Selecciona Colocar AR, deja activado Simulate In Editor y presiona Play. Aparecen un piso y una pared simulados.
8. Presiona Cubo y haz clic sobre el piso. La figura naranja se coloca donde hiciste clic; no se pega a la cámara.
9. Presiona Esfera y haz clic en otro punto. La esfera azul se agrega sin reemplazar el cubo anterior.
10. Haz clic sobre una figura. Cambia a amarillo para indicar que está seleccionada. Presiona Eliminar selección para quitarla; las demás figuras deben conservarse.
11. Vuelve a tocar una figura seleccionada para deseleccionarla. También puedes cambiar entre Cubo y Esfera para limpiar la selección sin eliminar objetos.
12. Haz clic en Game para darle el foco. Usa W, A, S y D para moverte; Q y E cambian la altura. Mantén presionado el botón derecho del mouse y muévelo para girar la cámara. Shift aumenta la velocidad de desplazamiento.
13. Coloca una figura, gira hasta dejarla fuera de cuadro y regresa. Debe seguir en la posición donde la colocaste. Camina alrededor de ella para observarla desde otro ángulo.
14. Presiona Ocultar superficies. Se oculta el dibujo del piso y la pared simulados, pero sus colliders siguen disponibles para colocar figuras. Al regresar a Mostrar superficies, los objetos colocados conservan su posición.

La simulación comprueba la interacción con superficies virtuales. No prueba el rastreo de ARCore, la estabilidad de los anclajes ni el permiso de cámara. Al salir de Play, la distribución se elimina.

## Parte 3 · Configurar Android

15. Abre File > Build Profiles, agrega o selecciona Android y presiona Switch Platform. Espera a que termine la importación para esa plataforma.
16. En Edit > Project Settings > Player, verifica que Active Input Handling use Input System Package (New) o Both. Reinicia el Editor si Unity lo solicita.
17. En Project Settings > XR Plug-in Management, abre Android y confirma que ARCore e Initialize XR on Startup estén activados.
18. En los ajustes de ARCore, deja Requirement en Required y Depth en Optional. Este ejercicio no requiere profundidad ni anclajes en la nube.
19. Abre XR Plug-in Management > Project Validation y revisa los requisitos pendientes. El asistente configura Minimum API Level en Android 7.0 (API 24), ARM64, IL2CPP y OpenGLES3 como única API gráfica.
20. Confirma que `Assets/Scenes/Placement.unity` sea la escena habilitada en Build Profiles. Conecta el celular y usa Build And Run.

## Parte 4 · Colocar y recorrer en el celular

21. Abre la aplicación y concede el permiso de cámara. Mueve el celular lentamente para observar una misma zona desde distintas posiciones.
22. Espera a que aparezcan superficies azules. Un disco verde señala una superficie detectada bajo el centro de la pantalla. Puedes tocar otro punto de una superficie detectada para colocar allí una figura.
23. Elige Cubo o Esfera y toca la superficie. La figura mide 20 cm y su centro queda a 10 cm de la superficie, de modo que descansa sobre ella. En una pared, se orienta según la normal del plano detectado.
24. Coloca ambas figuras en puntos separados. Camina despacio a su alrededor y comprueba que cambia la perspectiva sin que las figuras sigan al celular.
25. Aparta la cámara hasta que los objetos salgan del cuadro. Al volver a mirar la zona, deben seguir allí mientras ARCore conserve o recupere el rastreo de esa sesión.
26. Toca una figura para seleccionarla y presiona Eliminar selección. Comprueba que desaparezca únicamente esa figura y que el contador disminuya.
27. Oculta las superficies azules. Las figuras y sus anclajes permanecen; solo cambia la visualización de los planos. Vuelve a mostrar las superficies si necesitas encontrar una zona donde colocar otro objeto.
28. Cierra la aplicación por completo y vuelve a abrirla. La nueva sesión debe comenzar vacía, porque esta versión no guarda anclajes para otra sesión.

Si aparece el mensaje de rastreo limitado, deja de colocar objetos y enfoca una zona con detalle y buena iluminación. Las figuras cuyo anclaje deje de estar en Tracking se ocultan temporalmente, y se muestran cuando ese anclaje vuelve a tener seguimiento. El sistema no garantiza que cualquier pérdida de rastreo pueda recuperarse.

## Cómo se organiza el código

`PlacementBootstrap.cs` crea XR Origin, la cámara, AR Plane Manager, AR Raycast Manager y AR Anchor Manager. Escucha los cambios de planos para agregar su visualización y procesa los toques fuera de la interfaz.

Antes de colocar, revisa si el toque selecciona una figura existente mediante `Physics.Raycast`. Si no selecciona una figura, consulta `ARRaycastManager` con `TrackableType.PlaneWithinPolygon`. Esta consulta solo acepta posiciones dentro de un plano detectado y rastreado.

La colocación intenta crear un anclaje unido al plano con `AttachAnchor`. Si ese intento no devuelve un anclaje, usa `TryAddAnchorAsync`. La figura se crea como hija del anclaje, que es quien mantiene su pose dentro de la sesión. Si la creación falla, la aplicación informa el error y no conserva una entrada de objeto colocado.

`PlacedShape.cs` crea el cubo o la esfera, controla el material amarillo de selección y revisa el estado de su anclaje. El cambio de color es temporal: la figura recupera su material naranja o azul al deseleccionarla.

`PlacementRegistry.cs` conserva los tipos e identificadores de los objetos durante la sesión. Cambiar de figura no modifica las que ya existen. Eliminar la selección quita su registro; el controlador libera también el anclaje y el GameObject correspondiente.

`EditorWalkCamera.cs` proporciona los controles de recorrido de la simulación. `PlacementProjectSetup.cs` prepara los materiales, configura Android y registra ARCore. Este último script vive dentro de Editor y no corre en el celular.

No hay una biblioteca de imágenes ni un marcador que imprimir. La cámara tiene un plano de recorte lejano de 1000 m y el código no elimina objetos según su distancia. Ese ajuste de dibujo no garantiza que el rastreo físico conserve una referencia estable durante recorridos largos.

## Si algo sale mal

- Si la cámara muestra un fondo de color, revisa ARCameraBackground, AR Background Renderer Feature en AR_Renderer y el pipeline activo en Graphics y Quality.
- Si no aparecen planos, mueve el celular lentamente y enfoca una superficie con textura. Una mesa brillante o una pared completamente blanca pueden dificultar el seguimiento.
- Si un toque no coloca una figura, comprueba que esté fuera de los controles y dentro de un plano detectado. Tocar una figura existente la selecciona.
- Si el botón Eliminar está deshabilitado, selecciona primero una figura. Tocar por segunda vez la misma figura la deselecciona.
- Si cambia la posición de una figura, el sistema puede estar refinando su estimación del entorno. Evita movimientos bruscos y prueba en una zona pequeña antes de ampliar el recorrido.
- Si una figura deja de verse al perder el seguimiento, regresa a una zona reconocible y espera. Si la sesión se reinició, sus anclajes anteriores ya no están disponibles.
- Si una figura se ve a través de una pared real, recuerda que esta versión no usa oclusión por profundidad. La geometría del mundo real no forma una barrera de dibujo en este proyecto.
- Si la simulación no responde al teclado, haz clic dentro de Game. El botón derecho del mouse controla la orientación mientras lo mantienes presionado.

## Entregable y validación

Graba un video del celular que muestre la detección de una superficie, la colocación de un cubo y una esfera, un recorrido alrededor de ambas y el regreso después de dejarlas fuera de cuadro. Después elimina una figura y muestra que la otra permanece. Termina ocultando los planos sin quitar el objeto restante.

La lógica de inventario pasó 27 comprobaciones con .NET 10 y los cinco scripts de Unity se analizaron para Editor y Android. Esas pruebas no ejecutan Unity ni ARCore. La compilación, la interfaz renderizada, el comportamiento de los anclajes y el recorrido físico permanecen pendientes de validación en Unity 6.3 y en un celular.

## Referencias técnicas

- Unity, AR Foundation 6.3, anclajes: https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.3/manual/features/anchors/introduction.html
- Unity, AR Foundation 6.3, raycasts: https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.3/manual/features/raycasts.html
- Google, uso de anclajes en ARCore: https://developers.google.com/ar/develop/anchors
- Las firmas utilizadas se contrastaron con el código oficial de AR Foundation 6.3.5 y ARCore 6.3.5.
