# Práctica 3 · AR · Captura con esfera

En esta práctica, un marcador muestra un cubo naranja. Al apuntarle y presionar Lanzar, una esfera azul sale desde la cámara. Si acierta, el cubo desaparece y una esfera verde ocupa su lugar. La captura se conserva al apartar la cámara y al cerrar la aplicación.

El proyecto está preparado para Unity 6.3 LTS y Android con ARCore. Incluye una escena, los scripts, un marcador de prueba y un asistente que crea la biblioteca y los materiales al importar. La simulación del Editor permite revisar la mecánica; la detección de la imagen se prueba en el celular.

## Antes de empezar

- Instala Unity 6.3 LTS con Android Build Support, Android SDK & NDK Tools y OpenJDK desde Unity Hub.
- Usa un celular Android compatible con ARCore y un cable USB que transfiera datos. Activa la depuración USB.
- Ten una segunda pantalla para mostrar el marcador o una impresión de la imagen incluida.
- Conserva una copia del proyecto de la práctica 1. Este proyecto de captura se abre en una carpeta independiente.

La versión registrada es 6000.3.27f1. Si ya tienes otro parche de Unity 6.3 LTS, trabaja sobre una copia y deja que el Editor actualice los archivos del proyecto cuando lo solicite. Los paquetes fijados en `Packages/manifest.json` son AR Foundation 6.3.5, Google ARCore XR Plugin 6.3.5, XR Core Utils 2.5.1, XR Plug-in Management 4.5.3 e Input System 1.11.2. Universal Render Pipeline usa la versión 17.3.0, asociada a Unity 6.3.

## Parte 1 · Abrir el proyecto

1. Descomprime `marker-capture-unity-6.3.zip` en una carpeta donde tengas permiso de escritura. La carpeta que debes abrir contiene `Assets`, `Packages` y `ProjectSettings`.
2. En Unity Hub, selecciona Add > Add project from disk y elige esa carpeta. Asígnale Unity 6.3 LTS y ábrela.
3. Espera a que Package Manager descargue los paquetes y a que termine la compilación de scripts. La primera importación necesita conexión a internet.
4. El asistente prepara los recursos cuando falta la biblioteca o la configuración URP. Si la escena no se abre o aparecen mensajes de recursos faltantes, ejecuta Tools > AR Capture > Preparar proyecto.
5. Abre `Assets/Scenes/Capture.unity`. La escena guardada contiene un objeto llamado Captura AR con el componente `CaptureBootstrap`. La cámara, las figuras y los componentes de rastreo se crean al entrar en Play.
6. Abre Window > General > Console. Resuelve los errores rojos antes de continuar. Un aviso de ARCore sin asignar se revisa en la parte de Android.

El proyecto usa URP. El asistente crea AR_URP y AR_Renderer en Assets/Settings, agrega AR Background Renderer Feature y asigna el pipeline a Graphics y a los niveles de Quality. Los materiales de figuras usan Universal Render Pipeline/Lit y el marcador simulado usa Universal Render Pipeline/Unlit. Ejecuta el asistente únicamente en esta copia independiente; si abres una copia de la versión anterior, vuelve a ejecutarlo para convertir sus materiales.

## Parte 2 · Probar la captura en el Editor

7. Selecciona Captura AR y deja activado Simulate In Editor en su componente. Cambia a la pestaña Game y presiona Play.
8. La simulación muestra un marcador fijo y un cubo naranja en el centro. Presiona Lanzar o la barra espaciadora. La esfera azul avanza en línea recta desde la cámara.
9. Al acertar, el cubo se sustituye por una esfera verde. El botón Lanzar queda deshabilitado porque el objetivo ya está capturado.
10. Presiona Simular pérdida de rastreo. Las figuras se ocultan. Después presiona Volver a detectar marcador: debe reaparecer la esfera verde.
11. Sal de Play y vuelve a entrar. La esfera verde debe conservarse porque el estado se guardó en `PlayerPrefs`.
12. Presiona Reiniciar captura visible. Regresa el cubo naranja y puedes repetir el lanzamiento. El botón borra únicamente la captura de la imagen visible.

La simulación usa una clave de guardado propia, `editor-simulation`. Capturar el cubo en la computadora no captura el marcador en Android. Tampoco prueba el permiso de cámara, el rastreo ni la compilación para el celular.

## Parte 3 · Preparar el marcador

13. Abre `Assets/Resources/Marker.png` en la segunda pantalla. Muestra la imagen completa, sin recortarla, y deja fijos el zoom y el brillo durante la prueba.
14. Mide con una regla el ancho de toda la imagen mostrada, de borde a borde. La biblioteca se prepara con 0.16 m, que equivale a 16 cm. Si el ancho real es otro, captura su valor en metros en el siguiente paso.
15. En Unity, selecciona `Assets/Resources/MarkerLibrary.asset`. Expande su entrada `blanco`, deja activado Specify Size y corrige Physical Size según la medida real. Por ejemplo, 20 cm de ancho se capturan como 0.20 m.
16. Para imprimir, usa el archivo `Marker-16cm.pdf` y selecciona tamaño real o escala de 100%. Mide el resultado antes de usarlo. Si la impresora ajustó el tamaño, corrige la biblioteca con la medida de la impresión.

Para usar el marcador de la práctica 1, importa su imagen como textura y asígnala al campo de textura de la entrada `blanco` en `MarkerLibrary`. Conserva Specify Size y vuelve a medir el ancho. Reinicia la captura antes de cambiar la textura, porque la entrada conserva su identificador y, con él, su estado guardado. La esfera verde seguirá apareciendo para esa entrada hasta que reinicies la captura.

Evita reflejos sobre la imagen y patrones con poco detalle. Si la detección falla con la imagen de prueba, compara con la imagen que ya funcionó en la práctica 1. La calidad del marcador incluido todavía requiere validación en un dispositivo con ARCore.

## Parte 4 · Configurar Android

17. Abre File > Build Profiles, agrega o selecciona Android y presiona Switch Platform. Espera a que termine la importación de recursos para esa plataforma.
18. En Edit > Project Settings > Player, verifica que Active Input Handling use Input System Package (New) o Both. Acepta el reinicio del Editor si Unity lo solicita.
19. En Project Settings > XR Plug-in Management, abre la pestaña Android y confirma que ARCore esté activado y que Initialize XR on Startup permanezca habilitado.
20. En los ajustes de ARCore, deja Requirement en Required y Depth en Optional. El ejercicio usa rastreo de imágenes y no necesita un sensor de profundidad.
21. Abre Project Settings > XR Plug-in Management > Project Validation y revisa los requisitos pendientes. El asistente configura Minimum API Level en Android 7.0 (API 24), Scripting Backend en IL2CPP, ARM64 y OpenGLES3 como única API gráfica. Conserva esos valores para esta práctica.
22. En Build Profiles, confirma que `Assets/Scenes/Capture.unity` sea la escena habilitada. Conecta el celular, autoriza la depuración USB y usa Build And Run.

Si compilas desde una Mac con Apple Silicon y Unity informa que no puede ejecutar `arcoreimg`, revisa la arquitectura de esa herramienta del paquete ARCore. La distribución 6.3.5 consultada incluye un ejecutable macOS x86_64, por lo que puede necesitar Rosetta 2. Ese error pertenece a la herramienta de compilación de la biblioteca y ocurre antes de instalar la app en el celular.

## Parte 5 · Probar en el celular

23. Abre la aplicación y concede el permiso de cámara. Debes ver el entorno sin un cubo flotando desde el arranque.
24. Encuadra el marcador a unos 30 a 80 cm, con luz suficiente y sin reflejos. Cuando el rastreo esté activo, aparecerá el cubo naranja sobre la imagen.
25. Mueve el celular hasta que la mira central quede sobre el cubo y presiona Lanzar. El disparo sigue la dirección de la cámara en el momento de lanzarlo. Si después giras el celular, la esfera continúa su trayectoria original.
26. Si fallas, la esfera se elimina después de tres segundos y puedes intentarlo otra vez. Si aciertas, aparece la esfera verde y se guarda la captura.
27. Aparta la cámara hasta perder el rastreo. Al volver al marcador, debe aparecer la esfera verde. El proyecto oculta el contenido cuando el proveedor reporta un estado distinto de Tracking; ese cambio puede tardar después de que la imagen salga del cuadro.
28. Cierra la aplicación por completo y vuelve a abrirla. Apunta al marcador: la esfera verde debe conservarse en ese celular. Presiona Reiniciar captura visible para recuperar el cubo.

El guardado es local. Borrar los datos de la aplicación elimina las capturas. El proyecto no sincroniza dispositivos ni envía las capturas a un servidor.

## Cómo se organiza el código

`CaptureBootstrap.cs` crea la escena de simulación o la escena AR, solicita el permiso de cámara en Android y dibuja los botones. En el celular crea AR Session, XR Origin, la cámara y AR Tracked Image Manager. Los enlaces de posición y rotación del Tracked Pose Driver siguen la configuración del paquete AR Foundation.

`TrackedCaptureManager.cs` escucha `trackablesChanged`. Cuando una imagen se agrega o se actualiza, crea o recupera su contenido. Usa `trackableId` para encontrar la instancia de esa sesión y `referenceImage.guid` para consultar la captura guardada. Si el proveedor elimina una instancia, el script destruye su contenido; el estado de captura permanece en el almacenamiento.

`CaptureTarget.cs` crea el cubo naranja y la esfera verde. Solo una figura queda activa. Al capturar, apaga el GameObject completo del cubo, incluido su collider, y activa la esfera verde. Una actualización de rastreo cambia la visibilidad del conjunto sin volver a encender el cubo capturado.

`CaptureProjectile.cs` mueve la esfera azul a 1.5 m/s. En cada cuadro usa `Physics.SphereCastAll` para revisar el volumen recorrido por la esfera. Ordena los impactos por distancia y captura el primer objetivo válido. Por eso este proyectil no necesita Rigidbody ni eventos `OnCollisionEnter`; la detección se calcula mediante un barrido de esfera.

`CaptureRegistry.cs` contiene la decisión de captura y evita registrar dos veces la misma imagen. `PlayerPrefsCaptureStore.cs` guarda el resultado con una clave propia y llama a `PlayerPrefs.Save()` después de cada cambio. El botón de reinicio elimina esa clave; no usa `PlayerPrefs.DeleteAll()`.

`CaptureProjectSetup.cs`, dentro de Editor, prepara la biblioteca, los materiales y la configuración Android. Sus instrucciones se ejecutan en el Editor y no forman parte del código que corre en el celular.

## Si algo sale mal

- Si Lanzar está deshabilitado, busca un objetivo que tenga rastreo activo y no esté capturado. También hay una pausa de 0.4 s entre disparos.
- Si aparece una esfera verde desde el primer intento, esa imagen ya tiene una captura guardada. Usa Reiniciar captura visible mientras el marcador esté rastreado.
- Si el marcador nunca se detecta, revisa su textura y su tamaño en MarkerLibrary, el brillo de la pantalla, los reflejos y la compatibilidad del celular con ARCore.
- Si las figuras tienen un tamaño o una distancia extraños, vuelve a medir el ancho mostrado. El tamaño registrado en la biblioteca debe coincidir con la imagen física.
- Si la pantalla permanece negra, revisa el permiso de cámara y la activación de ARCore. Revisa ARCameraBackground y AR Background Renderer Feature en AR_Renderer, además del pipeline activo en Graphics y Quality.
- Si aparecen dos cubos o dos cámaras, revisa la escena. Esta versión crea sus objetos desde CaptureBootstrap y no debe combinarse con los managers ni con ImageContentController de la práctica 1.
- Si el cubo reaparece después de capturarlo, comprueba que estés ejecutando esta escena y que no hayas agregado un script que reactive todos los renderers sin consultar el estado de captura.

## Entregable y revisión

Graba un video del celular que muestre el arranque limpio, la detección del cubo, un lanzamiento acertado, la pérdida de rastreo y el regreso de la esfera verde. Después muestra que la esfera sigue presente al cerrar y abrir la aplicación. Termina reiniciando la captura para recuperar el cubo.

El código fuente incluye validaciones de estado y revisión de sintaxis. La carpeta Validation ejecuta 15 comprobaciones sobre captura inicial, impactos repetidos, imágenes independientes, recuperación del estado, reinicio e identificadores inválidos. Esas pruebas se ejecutan con .NET 10 y son opcionales para quien solo abre el proyecto en Unity.

Antes de entregar una versión compilada, completa las pruebas de Android de esta guía. El proyecto se preparó sin Unity Editor disponible en el entorno de autoría; su compilación en Unity 6.3, su renderizado y su rastreo en el celular permanecen pendientes de validación.

## Referencias técnicas

- AR Foundation 6.3, rastreo de imágenes: https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.3/manual/features/image-tracking.html
- Unity 6.3, Physics.SphereCastAll: https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Physics.SphereCastAll.html
- Unity 6.3, PlayerPrefs: https://docs.unity3d.com/6000.3/Documentation/ScriptReference/PlayerPrefs.html
- Las firmas de las API del proyecto también se revisaron en el código de los paquetes oficiales AR Foundation 6.3.5, ARCore 6.3.5 y XR Plug-in Management 4.5.3.
