# Prácticas guiadas de rastreo de imágenes

Dos guías paso a paso, autocontenidas: la primera parte de un proyecto vacío de Unity 6 y
la segunda parte de la primera. La numeración de pasos es corrida dentro de cada guía, para
que una duda en clase se resuelva diciendo un número.

- [lab01.es.md](lab01.es.md): una imagen impresa produce un cubo. La guía cuida las dos
  fallas clásicas: la pantalla de un solo color al compilar, que se arregla con el AR
  Background Renderer Feature antes de tocar el rastreo, y el cubo visible desde el
  arranque, que se evita sacando el prefab de la escena.
- [lab02.es.md](lab02.es.md): dos imágenes, y cada una produce una figura distinta, cubo o
  esfera. El campo de prefab del manager se vacía y un script reparte por
  `referenceImage.name`.

Los datos técnicos vienen del manual de AR Foundation 6.0.
