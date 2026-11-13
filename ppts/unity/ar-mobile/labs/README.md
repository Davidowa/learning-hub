# Prácticas guiadas de realidad aumentada

Las prácticas utilizan Unity 6000.3.27f1, URP 17.3.0, AR Foundation 6.3.5 y Google ARCore XR Plugin 6.3.5. Las pruebas físicas requieren un celular Android compatible con ARCore.

## Laboratorios 03 a 06: revisión R2

La [carpeta de materiales revisados](Laboratorios-03-a-06/) contiene una base para el alumno y una solución de referencia por laboratorio. El alumno construye la escena, los prefabs y las conexiones del Inspector con los scripts proporcionados. Las guías explican también cómo crear el asset ContenidoLab, conectar la interfaz y comprobar el resultado por etapas.

| Práctica | Guía editable | PDF | Base del alumno | Referencia del docente |
| --- | --- | --- | --- | --- |
| 3. Captura con una esfera | [Markdown](Laboratorios-03-a-06/Lab03-Base/Guia.md) | [PDF](Laboratorios-03-a-06/Entregas/Lab03-Guia.pdf) | [ZIP](Laboratorios-03-a-06/Entregas/Lab03-Editor-Base.zip) | [Solución](Laboratorios-03-a-06/Lab03-Solucion/) |
| 4. Colocación sin marcador | [Markdown](Laboratorios-03-a-06/Lab04-Base/Guia.md) | [PDF](Laboratorios-03-a-06/Entregas/Lab04-Guia.pdf) | [ZIP](Laboratorios-03-a-06/Entregas/Lab04-Editor-Base.zip) | [Solución](Laboratorios-03-a-06/Lab04-Solucion/) |
| 5. Contenido sobre ArUco | [Markdown](Laboratorios-03-a-06/Lab05-Base/Guia.md) | [PDF](Laboratorios-03-a-06/Entregas/Lab05-Guia.pdf) | [ZIP](Laboratorios-03-a-06/Entregas/Lab05-Editor-Base.zip) | [Solución](Laboratorios-03-a-06/Lab05-Solucion/) |
| 6. QR y colocación | [Markdown](Laboratorios-03-a-06/Lab06-Base/Guia.md) | [PDF](Laboratorios-03-a-06/Entregas/Lab06-Guia.pdf) | [ZIP](Laboratorios-03-a-06/Entregas/Lab06-Editor-Base.zip) | [Solución](Laboratorios-03-a-06/Lab06-Solucion/) |

La [memoria de trabajo](Laboratorios-03-a-06/MEMORIA-DE-TRABAJO.md) registra los cambios, las pruebas, el estado publicado en Blackboard y los pendientes. El [paquete de las cuatro guías R2](Laboratorios-03-a-06/Entregas/Guias-Laboratorios-03-a-06-R2.zip) permite descargar los PDF juntos. Quien ya empezó conserva su proyecto y utiliza el PDF actualizado; esta revisión de las guías no cambia scripts, escenas ni prefabs.

La [infografía de OnGUI y Canvas](Laboratorios-03-a-06/Infografia/OnGUI-y-Canvas-Learning-Hub.pdf) explica en dos páginas cómo construir el mismo botón con ambas opciones. El ejemplo de OnGUI se realiza en un proyecto aparte.

Las cuatro soluciones aprobaron las pruebas de escena e interacción en Editor y su compilación Android. La validación física completa de la edición actual sigue pendiente en los términos de la memoria. Leer un QR no equivale a completar las pruebas de colocación, selección y eliminación.

## Prácticas 1 y 2

- La [práctica 1: un cubo sobre una imagen](lab01.es.md) configura URP, registra el ancho físico de la imagen y crea el contenido mediante ImageContentController. Conserva su [proyecto fuente](../projects/image-cube/README.es.md).
- La [práctica 2: dos imágenes y dos figuras](lab02.es.md) amplía la primera escena con una segunda biblioteca y dos relaciones entre imagen y prefab. Conserva su [proyecto fuente](../projects/image-pair/README.es.md).

El [script de las prácticas 1 y 2](scripts/ImageContentController.cs) coincide con el código de la primera guía. Sus pasos se contrastaron con las API oficiales; su compilación y rastreo en Android no se validaron como parte de la revisión R2 de los laboratorios 03 a 06.

Los archivos anteriores lab03.es.md a lab06.es.md y los proyectos de `../projects/` se conservan como antecedentes. Para la edición de construcción en el Editor publicada en Blackboard se utilizan los materiales R2 enlazados en la tabla.
