# Práctica 2 · AR · Dos imágenes y dos figuras

Esta práctica amplía el proyecto de la práctica 1. Una imagen muestra un cubo y otra imagen muestra una esfera, cada figura con su propio color y sobre la imagen correspondiente. Ambas pueden aparecer en el mismo cuadro.

La guía conserva Unity 6.3 LTS, Universal 3D, AR Foundation 6.3.5 y Google ARCore XR Plugin 6.3.5. Reutiliza ImageContentController de la guía revisada de la práctica 1 y agrega una segunda relación entre imagen y prefab en el Inspector.

## Alcance de la experiencia

Cada figura sigue a su imagen durante la sesión. El contenido se oculta cuando su ARTrackedImage deja de estar en Tracking. Ese estado no equivale a una prueba exacta de visibilidad: ARCore puede mantener una pose estimada después de que una imagen sale del cuadro.

La práctica usa dos imágenes diferentes. Dos copias de la misma imagen no sirven para verificar este reparto. Las imágenes pueden estar impresas o mostrarse juntas en una pantalla; su tamaño físico debe coincidir con la biblioteca en la disposición final.

## Antes de empezar

- Termina la guía revisada de la práctica 1 y verifica que el cubo aparezca sobre la imagen `cubo`. Conserva sus ajustes de cámara, URP y Android.
- Prepara una segunda imagen con detalles distintos. Evita usar dos versiones que solo cambien de color, porque ARCore extrae características en escala de grises.
- Usa una regla, un celular compatible con ARCore y una impresión o una segunda pantalla. Deja espacio entre las dos imágenes para observarlas juntas.

## Parte 1: Preparar la escena y la biblioteca

1. Abre el proyecto de la práctica 1 y guarda una copia de su escena con File > Save As, como `Assets/Scenes/Practica2AR.unity`. Trabaja en esta copia para conservar la primera práctica.
2. Selecciona el XR Origin y verifica que tenga un solo ImageContentController con Images asignado. Tracked Image Prefab debe estar vacío. Si partes de las guías anteriores, sustituye TrackedImageVisibility o PrefabPerImage por el código completo de la práctica 1 revisada.
3. Duplica el asset BibliotecaBlancos en Project y nombra la copia BibliotecaDosImagenes. Así puedes modificar esta biblioteca sin alterar la escena anterior.
4. Importa la segunda imagen en `Assets/Blancos`. Abre BibliotecaDosImagenes, conserva la primera entrada con Name `cubo`, agrega otra con Add Image y escribe `esfera` en Name. Asigna a cada entrada su textura correspondiente.
5. Prepara las dos imágenes en su disposición final. Si se muestran lado a lado en una pantalla, fija el tamaño de ambas antes de medir; al reducir la primera para hacer espacio, su medida anterior deja de servir.
6. Mide el ancho visible de cada dibujo, sin márgenes ajenos a su textura. En cada entrada activa Specify Size y registra su propio ancho en metros. Por ejemplo, una imagen de 12 cm requiere 0.12 m, aunque la otra mida 15 cm.
7. En el AR Tracked Image Manager de esta escena, asigna BibliotecaDosImagenes en Serialized Library y solicita 2 en Max Number Of Moving Images. El campo pide al proveedor capacidad para imágenes en movimiento; no representa el número de entradas de la biblioteca ni garantiza por sí solo que ambas se detecten.

## Parte 2: Crear la esfera

8. En la jerarquía crea un GameObject vacío ContenidoEsfera. Usa Reset en su Transform para dejar posición y rotación en cero y escala en uno.
9. Agrega un Sphere como hijo. Pon su posición local en `0, 0.025, 0`, su rotación local en cero y su escala en `0.05, 0.05, 0.05`. Su diámetro será de 5 cm y quedará apoyada sobre el plano de la imagen.
10. Crea un material con shader Universal Render Pipeline/Lit y un color distinto del cubo. Asígnalo a la esfera para reconocer el reparto desde otro ángulo.
11. Arrastra ContenidoEsfera a `Assets/Prefabs` y elimina la copia de la escena. Comprueba que ContenidoCubo también tenga una raíz con escala uno y un hijo Cube de 5 cm.

## Parte 3: Relacionar cada imagen con su contenido

12. En ImageContentController, establece dos entradas en Bindings. Conserva `cubo` en Image Name de la primera entrada y asigna el asset ContenidoCubo en Prefab.
13. En la segunda entrada escribe `esfera` en Image Name y asigna ContenidoEsfera en Prefab. Los nombres deben coincidir con los de BibliotecaDosImagenes, incluidas las minúsculas y la ausencia de espacios.
14. Revisa que las dos entradas tengan nombres distintos y prefabs asignados. El orden de Bindings no determina la figura: el script busca por nombre. Una entrada desconocida no recibe una esfera automáticamente.
15. Confirma que Tracked Image Prefab siga vacío y que no haya cubos ni esferas de prueba en la jerarquía. Guarda Practica2AR.unity.

## Cómo se organiza el código

ImageContentController obtiene `referenceImage.name` de cada imagen rastreada y busca ese nombre en Bindings. `cubo` devuelve ContenidoCubo y `esfera` devuelve ContenidoEsfera. La biblioteca identifica la imagen reconocida; el controlador decide qué contenido crear.

El diccionario spawned guarda una instancia por TrackableId. Dos imágenes reconocidas generan dos identificadores y dos objetos independientes. Una actualización de pose o estado reutiliza la instancia existente, de modo que las actualizaciones repetidas no crean copias.

Cada figura es hija del ARTrackedImage correspondiente. Desactivar el contenido por rastreo limitado conserva ese objeto del proveedor y permite recibir nuevas actualizaciones. Cuando la imagen vuelve a Tracking, reaparece su figura. Eliminar un trackable retira su instancia; desactivar el controlador limpia todas sus instancias.

## Parte 4: Compilar y probar en el celular

16. Revisa Project Settings > XR Plug-in Management > Project Validation > Android. Conserva ARCore activo, IL2CPP, ARM64 y OpenGLES3. Corrige los errores antes de compilar; los pasos de URP de la práctica 1 siguen vigentes.
17. En File > Build Profiles, deja Practica2AR.unity como única escena habilitada para esta prueba. Si el perfil tiene una lista propia, verifica esa lista. Así la aplicación abre la escena nueva al usar Build And Run.
18. Compila, abre la aplicación y concede el permiso de cámara si lo solicita. El entorno debe verse desde el arranque, sin figuras antes de reconocer sus imágenes.
19. Muestra únicamente la imagen `cubo`. Comprueba que aparezca el cubo y que conserve su tamaño de 5 cm. Después apunta únicamente a `esfera` y revisa la esfera del mismo diámetro.
20. Encuadra ambas imágenes, separadas y enfocadas. Ajusta lentamente la distancia para que cada una tenga suficiente detalle en el cuadro. Deben aparecer dos figuras, cada una sobre su imagen y con su propio color.
21. Cambia el ángulo despacio. Verifica la posición y orientación de ambas figuras, sin intercambios ni duplicados. No cambies el zoom o el tamaño de los dibujos en la otra pantalla.
22. Cubre una imagen para degradar su rastreo, manteniendo visible la otra. Cuando la primera pase a Limited o None, su contenido debe ocultarse y la segunda figura debe conservarse si sigue en Tracking. Descubre la imagen y revisa que su figura vuelva sin duplicarse.
23. Aparta la cámara y vuelve a encuadrar las dos imágenes. Registra si el proveedor conserva alguna pose mientras están fuera del cuadro. Cierra la app y ábrela otra vez para confirmar que la nueva sesión comienza sin contenido.

## Si algo sale mal

- Si ambas imágenes muestran la misma figura, revisa los nombres y los prefabs de Bindings. Comprueba también que Tracked Image Prefab siga vacío y que no haya un segundo controlador activo.
- Si falta una figura, verifica su textura, nombre, ancho físico y prefab. Solicitar 2 imágenes en movimiento no resuelve reflejos, desenfoque ni falta de detalle.
- Si las figuras están intercambiadas, corrige los prefabs de las entradas `cubo` y `esfera`. No necesitas intercambiar las texturas de la biblioteca.
- Si una figura cambia de escala o parece desplazada, vuelve a medir ambas imágenes en la disposición final. Revisa el Transform de su prefab y conserva la escala uno en el XR Origin.
- Si una figura tarda en ocultarse al sacar su imagen del cuadro, considera el estado reportado por ARCore. La prueba se basa en Tracking, Limited y None; no en una señal exacta de visibilidad.
- Si la aplicación sigue mostrando solo el cubo de la primera práctica, verifica la escena incluida en Build Profiles y la biblioteca asignada a la escena nueva.

## Entregable y validación

Graba un video que muestre el arranque sin contenido, cada imagen por separado, ambas juntas y la recuperación de una imagen después de cubrirla. Incluye el Inspector con las dos entradas de la biblioteca y sus medidas, las dos relaciones de Bindings y una consola sin errores.

Los pasos se contrastaron con la documentación y el código oficial de AR Foundation 6.3.5. Se revisó la sintaxis de ImageContentController, compartido con la práctica 1. La compilación en Unity, el reconocimiento simultáneo y la recuperación física del rastreo requieren validación en un celular; esas pruebas no se ejecutaron en este Mac.

## Referencias técnicas

- Unity, biblioteca de imágenes: https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.3/manual/features/image-tracking/reference-images.html
- Unity, AR Tracked Image Manager: https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.3/manual/features/image-tracking/artrackedimagemanager.html
- Unity, estado de rastreo: https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.3/manual/features/image-tracking/artrackedimage.html
- Google, imágenes aumentadas: https://developers.google.com/ar/develop/augmented-images
