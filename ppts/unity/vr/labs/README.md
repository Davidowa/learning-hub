# Prácticas guiadas de VR

Dos guías paso a paso, autocontenidas: la primera parte de un proyecto vacío de Unity 6 y la
segunda parte de la primera. La numeración de pasos es corrida dentro de cada guía, para que
una duda en clase se resuelva diciendo un número.

Las dos arman el banco de bandas, que es el ejemplo que corre por las cinco sesiones del curso.
Cada quien hace su propio proyecto y entrega el suyo. El visor del salón se comparte en parejas
para las pruebas del final, porque quien lo trae puesto no puede ver la consola.

- [lab01.es.md](lab01.es.md): el banco, y un torquímetro que se levanta. Del proyecto vacío
  hasta una app en el visor con el piso, la mesa de trabajo, el motor y el torquímetro
  agarrable, más el log que dice cuál mano lo tomó. Cuida las dos fallas clásicas: la app que
  abre como ventana plana, que es OpenXR marcado en la pestaña equivocada, y las manos que se
  ven pero no responden, que es el perfil de interacción o el Input Action Manager. Trae un
  apéndice con el modo desarrollador, para quien vaya a preparar un visor de cero.
- [lab02.es.md](lab02.es.md): cruzar el taller, y un paro que se queda abajo. Teletransporte
  con dos anclas, giro en pasos, y el paro de emergencia del motor escrito como clase propia
  que hereda de `XRBaseInteractable`, con el estado que sobrevive a que el dedo se vaya y una
  reposición que está deliberadamente al otro lado del cuarto.

Meta Quest Link no hace falta para ninguna de las dos. Link sirve para darle Play en el editor
y ver la escena en el visor sin compilar. Ahorra minutos y solo existe en Windows. Las guías
compilan por cable, que es lo que hay en el salón.

Los datos técnicos vienen del manual del XR Interaction Toolkit 3.5, del manual de Unity 6
para el build profile de Meta Quest, y de la documentación de Meta para el modo desarrollador.
