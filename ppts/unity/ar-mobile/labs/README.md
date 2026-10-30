# Prácticas guiadas de realidad aumentada

Las seis guías y sus proyectos usan Unity 6.3 LTS, URP 17.3.0, AR Foundation 6.3.5 y Google ARCore XR Plugin 6.3.5.
La numeración de pasos es continua dentro de cada guía. Las pruebas físicas requieren un celular Android compatible con ARCore.

- [Práctica 1: un cubo sobre una imagen](lab01.es.md). Configura URP, registra el ancho físico de la imagen y crea el contenido mediante ImageContentController. Incluye el [proyecto fuente](../projects/image-cube/README.es.md).
- [Práctica 2: dos imágenes y dos figuras](lab02.es.md). Amplía la primera escena con una segunda biblioteca y dos relaciones entre imagen y prefab. Incluye el [proyecto fuente](../projects/image-pair/README.es.md).
- [Práctica 3: captura con una esfera](lab03.es.md). Una esfera captura el cubo del marcador y lo sustituye por una esfera verde. Incluye el [proyecto fuente](../projects/marker-capture/README.es.md), una simulación y guardado local por imagen.
- [Práctica 4: colocación sin marcador](lab04.es.md). Permite colocar cubos o esferas, seleccionarlos y eliminarlos. Incluye el [proyecto fuente](../projects/markerless-place/README.es.md), una simulación y anclajes locales durante la misma sesión.

El [script de las prácticas 1 y 2](scripts/ImageContentController.cs) coincide con el código de la primera guía. Sus pasos se contrastaron con las API oficiales; la compilación en Unity y el rastreo en Android siguen pendientes de validación en el dispositivo.

- [Práctica 5: cubo sobre ArUco](lab05.es.md). Reconoce DICT_4X4_50 ID 23 y estima la pose de un marcador de 10 cm. Incluye el [proyecto fuente](../projects/aruco-cube/README.es.md), una simulación estática y el marcador para imprimir.
- [Práctica 6: QR y colocación](lab06.es.md). Lee AR:CUBO y AR:ESFERA con ZXing y permite colocar las figuras sobre planos detectados. Incluye el [proyecto fuente](../projects/qr-place/README.es.md), ambos QR y una simulación.
