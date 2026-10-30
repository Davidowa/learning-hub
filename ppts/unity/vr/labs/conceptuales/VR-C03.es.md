# VR-C03 | Locomoción y orientación espacial

Unity 6.3 LTS · URP · Meta Quest 3S · Montaje guiado y análisis

## Qué vas a construir

Montarás tres estaciones conectadas mediante teletransporte, con giros de 45 grados y un panel de instrucciones que responda al rayo de los controles. Configurarás tanto una superficie libre como destinos con posición y orientación definidas.

La parte conceptual explica cómo conservar la orientación y completar el recorrido sentado o de pie. La entrega es individual y vale 100 puntos. Tiempo estimado: dos sesiones de 80 minutos.

## Antes de empezar

- Utiliza el proyecto de VR-C02, con la base XR comprobada en VR-C01. Conserva Unity 6.3 LTS, URP, OpenXR y Starter Assets de XRI 3.3.2.
- Si no terminaste la lámpara, puedes partir de VR-C01. En ese caso usa el cubo inmóvil como objeto de referencia en la estación de herramienta e indica qué interacción quedó pendiente.
- Trabaja en una copia de la escena y utiliza el simulador para comprobar destinos antes de probarlos en Quest 3S.

## Parte 1: Reactivar la locomoción del prefab

1. Abre la escena anterior y guárdala como Assets/Scenes/VR-C03.unity. Activa el hijo Locomotion de XR Origin, que estaba desactivado en VR-C01.
2. En Locomotion revisa Locomotion Mediator y XR Body Transformer. El transformer debe referenciar el XR Origin de la escena y los proveedores deben utilizar ese mediador. Conserva las referencias del prefab. [1]
3. Localiza Locomotion/Turn y establece Turn Amount = 45 en Snap Turn Provider. Conserva sus acciones de Snap Turn de Starter Assets. No agregues un segundo proveedor de giro.
4. En cada Controller Input Action Manager de Left Controller y Right Controller deja Smooth Motion Enabled = false y Smooth Turn Enabled = false. En este prefab esas preferencias habilitan las acciones de teletransporte y snap turn, en lugar de las acciones de movimiento y giro continuos. [2]
5. Revisa Locomotion/Teleportation: debe tener Teleportation Provider. Conserva las referencias del prefab y deja Delay Time = 0 para comprobar primero el destino sin una transición adicional.
6. En Project Settings > XR Plug-in Management > XR Interaction Toolkit verifica que Interaction Layer 31 se llame Teleport. Si está libre y falta el nombre, utiliza el Fix de Starter Assets en Project Validation.
7. Expande cada control y localiza su Teleport Interactor. Debe utilizar un XR Ray Interactor con línea curva, Interaction Layer Mask = Teleport y las acciones de Teleport Mode del sample. No sustituyas el rayo normal de interacción por este rayo.

## Punto de comprobación

En los XRI Default Input Actions de 3.3.2, Teleport Mode utiliza el sector superior del joystick y Snap Turn utiliza sus sectores laterales. Con movimiento continuo desactivado, inclinar hacia delante permite apuntar un destino y soltar confirma cuando el interactuable usa On Select Exited. Revisa esas acciones si modificaste sus bindings.

::: pagebreak

## Parte 2: Crear la superficie de teletransporte

8. Cambia Piso a Position (0, -0.05, 2) y Scale (6, 0.1, 6). Su parte superior queda en Y = 0. Conserva Box Collider y no actives Is Trigger.
9. Agrega Teleportation Area al Piso. Asigna el Interaction Manager y el Teleportation Provider de Locomotion/Teleportation. En Interaction Layer Mask selecciona solo Teleport; en Colliders asigna el Box Collider del piso.
10. Establece Teleport Trigger = On Select Exited y Match Orientation = World Space Up. Desactiva Match Directional Input para conservar el rumbo al elegir una superficie libre. Mantén al Piso en la capa física Default; Teleport es una capa de interacción de XRI, no una capa física. [3]
11. Revisa que Raycast Mask del rayo de teletransporte incluya la capa física Default. La coincidencia del Interaction Layer Mask no reemplaza esta prueba física de geometría.

## Parte 3: Montar tres destinos definidos

12. Crea tres GameObjects vacíos bajo Entorno, con escala uno y los nombres y posiciones de la tabla. Usa Rotation Y para orientar cada destino.

| Destino | Position (X, Y, Z) | Rotation Y y propósito |
| --- | --- | --- |
| Inicio | (-1.5, 0, 0) | 0 grados, para mirar hacia instrucciones. |
| HerramientaDestino | (1.5, 0, 1) | 0 grados, para mirar hacia la mesa. |
| Revision | (0, 0, 3.8) | 180 grados, para mirar de regreso a la sala. |

13. Dentro de cada destino crea un Cylinder llamado Disco, con posición local (0, 0.01, 0) y escala local (0.6, 0.01, 0.6). Conserva su Collider. Crea también un hijo vacío PuntoLlegada, con posición local cero, rotación cero y escala uno.
14. En la raíz de cada destino agrega Teleportation Anchor. Asigna el Interaction Manager, el Teleportation Provider y el Collider del Disco. Selecciona Interaction Layer Mask = Teleport y Teleport Trigger = On Select Exited.
15. En Teleport Anchor Transform arrastra su propio PuntoLlegada. Usa Match Orientation = Target Up And Forward. El punto en Y = 0 define la llegada a nivel del piso; la altura visual del disco no debe utilizarse como altura del usuario. [3]
16. Mueve SuperficieMesa a (1.5, 0.70, 2) y Herramienta a (1.5, 0.85, 2). Si conservas la lámpara y su interruptor, desplaza sus objetos un mismo incremento para mantenerlos junto a esa mesa. Deja libre el espacio de llegada delante de ella.

En cada destino agrega un texto 3D con su nombre y una flecha o referencia que indique hacia dónde quedará mirando el usuario. Conserva una zona libre alrededor del punto de llegada.

::: pagebreak

## Parte 4: Crear una interfaz en el espacio virtual

17. Usa GameObject > XR > UI Canvas. El menú crea un Canvas World Space y prepara un EventSystem para XR si falta. Nombra el Canvas InstruccionesXR. Debe quedar un solo EventSystem con XR UI Input Module activo. No mantengas además otro módulo de entrada activo. [4]
18. Pon InstruccionesXR como hijo de Entorno, con Position (-1.5, 1.3, 1.5), Rotation (0, 0, 0) y Scale (0.002, 0.002, 0.002). En Rect Transform usa Width = 800 y Height = 450. Con esa escala, el panel mide aproximadamente 1.6 × 0.9 metros.
19. En Canvas revisa Render Mode = World Space y asigna Main Camera del XR Origin como Event Camera. Conserva Tracked Device Graphic Raycaster. Si se creó otro EventSystem automáticamente, conserva solo el configurado con XR UI Input Module.
20. Crea como hijo un UI > `Button - TextMeshPro` llamado MostrarAyuda. Si lo solicita, importa TMP Essential Resources. Usa anclaje central, Position (0, 130), Width = 650 y Height = 90. Cambia su texto a MOSTRAR INSTRUCCIONES y usa tamaño de fuente 32.
21. Crea un UI > Panel hijo del Canvas llamado Ayuda. Déjalo centrado, con Width = 700, Height = 220 y Position (0, -70). Dentro agrega `Text - TextMeshPro` con el texto: Apunta al disco. Inclina el joystick hacia delante. Suelta para viajar. Usa los lados para girar. Ajusta su Rect Transform para cubrir el panel, con fuente 30 y márgenes legibles.
22. En Ayuda crea un `Button - TextMeshPro` llamado CerrarAyuda, con texto CERRAR y tamaño (200, 60), en la parte inferior. Ajusta la altura del texto de instrucciones para que no se encimen.
23. En MostrarAyuda > Button > On Click() agrega una llamada a Ayuda > GameObject.SetActive(bool), con argumento verdadero. En CerrarAyuda agrega la misma llamada con argumento falso. Deja Ayuda desactivado antes de ejecutar; el botón MostrarAyuda debe permanecer activo.
24. En los interactores normales de los controles verifica Enable Interaction with UI GameObjects, o Enable UI Interaction en XR Ray Interactor, según el componente del prefab. Conserva sus acciones de UI Press. En Starter Assets 3.3.2 el gatillo ejecuta UI Press para XRController.

## Comprobación de interfaz

En Play apunta al botón con el rayo normal y pulsa UI Press. Debe abrirse Ayuda; CERRAR debe ocultar solo ese panel y dejar disponible MOSTRAR INSTRUCCIONES. El rayo de teletransporte y el rayo de UI cumplen funciones distintas. Suelta el joystick de teletransporte antes de operar el botón.

::: pagebreak

## Parte 5: Probar el recorrido

25. En el simulador comienza frente al panel. Abre y cierra Ayuda. Inclina el joystick simulado hacia delante y apunta al disco Inicio. Al soltar, debes llegar al punto indicado y mirar hacia el panel.
26. Viaja a HerramientaDestino. Toma y suelta Herramienta si completaste VR-C02. No intentes teletransportarte mientras mantienes un objeto seleccionado a distancia: el Controller Input Action Manager puede deshabilitar las acciones de locomoción para evitar conflictos de entrada.
27. Suelta la herramienta, apunta a Revision y confirma el viaje. Debes mirar de regreso a la sala, según el eje forward de PuntoLlegada. Comprueba la posición del usuario, no solo la ubicación del rayo.
28. Prueba un destino libre sobre Piso. Debes llegar al punto elegido sin imponer el rumbo de uno de los anchors. Compara este comportamiento con la orientación definida por los discos.
29. Ejecuta un snap turn hacia la izquierda y otro hacia la derecha. Deben ocurrir en pasos de 45 grados. Repite con otro valor únicamente en una copia de la escena y explica la diferencia.
30. Para Quest 3S, habilita solo VR-C03.unity en Scene List del perfil Meta Quest. Revisa Project Validation y usa Build And Run. Comprueba los mismos destinos y botones, sin exigir recorrer físicamente la sala virtual.
31. Si haces la prueba física, observa sentado o de pie según tus posibilidades, dentro de los límites del visor. Si aparece malestar, termina la prueba. Puedes completar el registro con la simulación y señalar la comprobación pendiente.

## Si algo sale mal

| Síntoma | Revisión concreta |
| --- | --- |
| No aparece el rayo curvo. | Revisa Teleport Mode, Smooth Motion Enabled = false y Teleport Interactor del control. |
| El rayo aparece, pero no viaja. | Comprueba Teleportation Provider, mediador, Collider y máscaras de interacción y físicas. |
| Llegas elevado o dentro de un objeto. | Revisa PuntoLlegada en Y = 0, XR Origin en Floor y espacio libre alrededor del destino. |
| Llegas mirando en otra dirección. | Revisa Target Up And Forward y el eje azul forward del PuntoLlegada. |
| El botón no responde. | Revisa World Space, Tracked Device Graphic Raycaster, XR UI Input Module, UI Press y el rayo normal. |
| Solo puedes mover el origen a mano. | Revisa el mediador y las referencias del prefab. No implementes locomoción moviendo la Main Camera directamente. |

## Registro de pruebas

Anota para Inicio, HerramientaDestino y Revision: posición esperada, dirección esperada, resultado observado y medio de comprobación. Agrega una prueba sobre el área libre y una de apertura y cierre del panel. Si algo falla, registra el cambio que hiciste y repite esa prueba.

::: pagebreak

## Análisis después del montaje

1. Dibuja un plano con las tres estaciones y flechas de llegada. Distingue el tamaño virtual de la sala del área física disponible.
2. Compara Teleportation Area y Teleportation Anchor utilizando una observación de cada uno. Explica el efecto de Match Orientation.
3. Describe un recorrido de seis acciones que incluya dos desplazamientos, un giro y una operación del panel. Indica cómo volverías a las instrucciones.
4. Explica qué ajustes o comprobaciones permitirían usar las mismas estaciones sentado y de pie. Diferencia altura, alcance de los controles y legibilidad.

## Entrega y rúbrica

Entrega Apellido_VR-C03.pdf, de 3 a 5 páginas, con el plano, Inspector de un área y un anchor, la configuración del Canvas, el registro de pruebas y las respuestas. Conserva VR-C03.unity y los recursos del proyecto para reproducirlo.

| Criterio | Puntos | Evidencia para obtener el total |
| --- | --- | --- |
| Configura locomoción y superficie. | 25 | Muestra mediador, proveedor, acciones, área y máscaras coherentes. |
| Monta los tres destinos. | 25 | Define posición, orientación y espacio de llegada libre en cada anchor. |
| Construye y comprueba la UI. | 25 | Abre y cierra instrucciones con UI XR y registra el recorrido. |
| Analiza orientación y alcance. | 25 | Presenta plano y seis acciones, y responde las cuatro preguntas. |
| Total | 100 | La evidencia corresponde al montaje propio. |

Cada criterio recibe el total si cumple la evidencia, la mitad si está parcial pero verificable y cero si falta o contradice el funcionamiento analizado.

## Referencias y alcance de la revisión

[1] Unity XRI 3.3. Consulta el sistema de locomoción.

[Locomotion overview](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.3/manual/locomotion.html)

[2] Unity XRI 3.3. Consulta Controller Input Action Manager, prefabs y acciones.

[Starter Assets](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.3/manual/samples-starter-assets.html)

[3] Unity XRI 3.3. Consulta superficies, destinos y orientación.

[Teleportation Area](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.3/manual/teleportation-area.html)

[Teleportation Anchor](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.3/manual/teleportation-anchor.html)

[4] Unity XRI 3.3. Consulta el montaje de Canvas y EventSystem para XR.

[Set up UI Canvases for XR](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.3/manual/ui-setup.html)

Los componentes y campos se contrastaron con el paquete oficial XRI 3.3.2. No se ejecutó una compilación en Unity ni una prueba física durante la elaboración de la guía.
