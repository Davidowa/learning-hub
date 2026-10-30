# VR-C01 | Presencia, escala y seguimiento

Unity 6.3 LTS · URP · Meta Quest 3S · Montaje guiado y análisis

## Qué vas a construir

Montarás una sala virtual con un piso, una mesa, un cubo de 20 cm y una referencia de altura. Configurarás la cámara y los controles mediante OpenXR y XR Interaction Toolkit (XRI). Al mover la cabeza debe cambiar la perspectiva de los objetos; estos deben permanecer en la sala.

Este es el proyecto base de la serie. Los laboratorios VR-C02 y VR-C03 agregan interacción y locomoción. VR-C04 es opcional. El montaje se realiza en Unity; después se entrega un reporte individual con evidencia y respuestas. Valor: 100 puntos. Tiempo estimado: dos sesiones de 80 minutos.

## Antes de empezar

- Instala Unity 6.3 LTS desde Unity Hub, con Android Build Support, Android SDK & NDK Tools y OpenJDK. Utiliza un parche reciente de la rama 6000.3 y registra su número completo.
- Para la prueba física, prepara Quest 3S con sus controles, un cable USB de datos, modo de desarrollador habilitado y depuración USB autorizada. Sigue la configuración de cuenta y dispositivo de Meta si todavía no están preparados. [1]
- El montaje y las interacciones se pueden revisar con el simulador de XRI. Esa revisión no acredita seguimiento físico, comodidad ni funcionamiento del APK. Si no tienes visor, documenta esa limitación.
- Los nombres de menús corresponden al Editor en inglés. Trabaja en un proyecto nuevo de VR; conserva las prácticas de AR por separado.

## Parte 1: Crear el proyecto y configurar los paquetes

1. En Unity Hub crea un proyecto Universal 3D llamado LaboratoriosVR. Espera la importación. Crea las carpetas Assets/Scenes, Assets/Materials y Assets/Scripts.
2. Guarda la escena como Assets/Scenes/VR-C01.unity. Conserva una copia antes de modificarla en otro laboratorio.
3. Abre File > Build Profiles > Add Build Profile. Elige Meta Quest y agrega el perfil. Selecciónalo y usa Switch Platform. Unity instala el OpenXR requerido por esa plataforma. No necesitas agregar los paquetes opcionales de Meta para esta serie. [2]
4. En Window > Package Manager instala XR Interaction Toolkit 3.3.2. Si no aparece en la lista inicial, usa Install package by name con com.unity.xr.interaction.toolkit y versión 3.3.2. Acepta las dependencias que requiere el paquete.
5. En Player Settings > Other Settings establece Active Input Handling en Input System Package (New). Reinicia el Editor si lo solicita. Conserva URP y Shader Graph de la plantilla.
6. Selecciona XRI en Package Manager > Samples e importa Starter Assets y XR Interaction Simulator, ambos de 3.3.2. La guía utiliza esos recursos concretos. Si tienes otra versión, no mezcles muestras de versiones distintas.

::: pagebreak

## Parte 2: Preparar OpenXR y la cámara

7. Abre Edit > Project Settings > XR Plug-in Management. En la pestaña Android activa OpenXR e Initialize XR on Startup. Conserva OpenXR como proveedor de esta práctica.
8. En los ajustes OpenXR de Android activa Meta Quest Support. En Enabled Interaction Profiles agrega Oculus Touch Controller Profile, que proporciona la ruta de entrada para los controles de este ejercicio. Revisa los avisos de Project Validation. [3]
9. En XR Plug-in Management > Project Validation selecciona Android. Resuelve errores del proyecto y de Starter Assets. La regla del sample reserva Interaction Layer 31 para Teleport; aplica su corrección si está libre. Estas capas son de XRI, distintas de las capas físicas.
10. En Project busca el prefab exacto XR Origin (XR Rig), dentro de Assets/Samples/XR Interaction Toolkit/3.3.2/Starter Assets/Prefabs. Arrástralo a la jerarquía. Elimina la Main Camera original de la plantilla y conserva la Directional Light.
11. Agrega GameObject > XR > XR Interaction Manager si no existe. Debe quedar un solo manager en la escena.
12. Selecciona la raíz XR Origin (XR Rig). Pon Position y Rotation en cero y Scale en (1, 1, 1). En XR Origin establece Requested Tracking Origin Mode en Floor. Confirma que Camera referencia la Main Camera dentro de Camera Offset.
13. Revisa Input Action Manager en la raíz. Action Assets debe contener XRI Default Input Actions del mismo Starter Assets. El prefab ya tiene las referencias de seguimiento de cabeza y controles; no sustituyas esos campos por acciones vacías. [4]
14. Expande Camera Offset. La Main Camera debe tener Camera, Audio Listener y Tracked Pose Driver (Input System). Conserva sus acciones de posición y rotación. No agregues otra cámara ni un script que anime su Transform.
15. Localiza el hijo Locomotion del XR Origin y desactiva ese GameObject para este primer laboratorio. Así se observa el seguimiento sin desplazamiento por joystick. En cada Controller Input Action Manager conserva Smooth Motion Enabled y Smooth Turn Enabled desactivados.

## Punto de comprobación

Antes de continuar deben existir una cámara XR y un XR Interaction Manager. Las acciones deben estar asignadas y la consola no debe tener errores de compilación. El modo Floor permite que la altura venga de la referencia de piso; evita añadir una altura fija adicional a la cámara.

## URP y el fondo de la experiencia

16. Abre Project Settings > Graphics y Quality. Identifica el URP Asset efectivo del perfil Meta Quest y su nivel de calidad. Si el perfil tiene overrides, revisa también esos campos. Anota el nombre del asset y la versión de URP.
17. Conserva un Universal Renderer de la plantilla y materiales Universal Render Pipeline/Lit. Esta experiencia muestra una sala virtual completa. No agregues AR Session, AR Camera Background ni AR Background Renderer Feature.

::: pagebreak

## Parte 3: Montar la sala con medidas

18. Crea un GameObject vacío Entorno, con posición y rotación cero y escala uno. Crea sus objetos con GameObject > 3D Object > Cube y asigna los valores de la tabla. Todas las medidas usan una unidad por metro.

| Objeto | Position (X, Y, Z) | Scale (X, Y, Z) |
| --- | --- | --- |
| Piso | (0, -0.05, 1) | (4, 0.1, 4) |
| SuperficieMesa | (0, 0.70, 1.2) | (1.2, 0.1, 0.6) |
| ReferenciaAltura | (-1.2, 0.5, 1.2) | (0.05, 1, 0.05) |
| CuboMedida | (0, 0.85, 1.2) | (0.2, 0.2, 0.2) |

19. Conserva los Box Collider. En este laboratorio no agregues Rigidbody al cubo: será una referencia inmóvil. La mesa termina en Y = 0.75 y el cubo comienza en esa misma altura.
20. Crea tres materiales URP/Lit: PisoGris, MesaClara y CuboNaranja. Asígnalos desde Project. Elige un color diferente para ReferenciaAltura y conserva la luz direccional.
21. Crea un `Text - TextMeshPro` desde el menú de objetos 3D, como hijo de Entorno. Si Unity lo pide, importa TMP Essential Resources. Nómbralo Medida1m, escribe 1 metro y colócalo junto a ReferenciaAltura, orientado hacia el origen. Ajusta su tamaño para leerlo desde el punto inicial.
22. Guarda la escena. Selecciona cada objeto y verifica que sus dimensiones no dependan de un padre escalado. El XR Origin y Entorno deben conservar escala uno.

## Jerarquía que debes obtener

```text
VR-C01
  Directional Light
  XR Interaction Manager
  XR Origin (XR Rig)
    Camera Offset
      Main Camera
      Left Controller / Right Controller
    Locomotion [desactivado]
  Entorno
    Piso
    SuperficieMesa
    ReferenciaAltura
    CuboMedida
    Medida1m
```

El prefab contiene otros hijos y componentes que no aparecen en este esquema. Consérvalos. El esquema destaca las referencias necesarias para comprobar el montaje.

## Qué representa cada elemento

URP dibuja la sala. OpenXR conecta con el entorno de ejecución del visor. XR Origin relaciona el espacio de seguimiento con la escena y XRI aporta interacción y locomoción. La cámara sigue a la cabeza; el cubo pertenece a Entorno y no debe quedar como hijo de la cámara.

::: pagebreak

## Parte 4: Comprobar el montaje en el Editor

23. Abre Project Settings > XR Plug-in Management > XR Interaction Toolkit. Activa Use XR Interaction Simulator in scenes y deja Instantiate In Editor Only habilitado. Selecciona el prefab XR Interaction Simulator del sample si no aparece asignado. No agregues además una segunda copia manual a la escena. [5]
24. Presiona Play y da foco a Game. Usa la ayuda que muestra el simulador para mover la cabeza y seleccionar un control. Tab alterna sus modos y los corchetes seleccionan dispositivos; consulta las indicaciones de la versión importada antes de cambiar sus bindings.
25. Acércate virtualmente a la mesa y cambia la altura con los controles del simulador. El cubo debe seguir en el mismo lugar de la sala y cambiar su perspectiva. Registra la altura y escala observadas; no cambies la escala del XR Origin para ajustar la vista.
26. Detén Play. La simulación alimenta dispositivos de entrada; mover el mouse únicamente en Scene no verifica el seguimiento XR.

## Parte 5: Compilar y probar en Quest 3S

27. En Build Profiles selecciona el perfil Meta Quest. En Player Settings verifica IL2CPP y ARM64. Conserva Vulkan, que utiliza ese perfil, y los niveles de API compatibles con el OpenXR instalado y Project Validation. No copies el Target API de una guía antigua para publicar en una tienda.
28. Agrega VR-C01.unity a Scene List con Add Open Scenes y déjala como única escena habilitada en ese perfil. Guarda el proyecto. Si usas una lista propia del perfil, verifica esa lista.
29. Conecta Quest 3S con el cable de datos, enciéndelo y autoriza la depuración USB dentro del visor. En Run Device selecciona el dispositivo. Activa Development Build para la revisión y usa Build And Run. La aplicación debe ejecutarse en el visor, no como una ventana plana del escritorio.
30. Dentro de un área despejada y respetando los límites del visor, mira la mesa, inclina la cabeza y desplázala ligeramente hacia los lados. Comprueba que el cubo se mantenga en la sala. No necesitas recorrer físicamente todo el espacio virtual.
31. Comprueba que la parte superior de la referencia de un metro y la mesa tengan una escala coherente. Si la altura no corresponde, revisa el piso definido en Quest y el modo Floor antes de mover la cámara manualmente.
32. Cierra y vuelve a abrir la aplicación. Debe aparecer la misma sala, sin necesitar una imagen o un marcador. Guarda una grabación breve o describe la comprobación pendiente si no tienes visor.

Build And Run permite probar una aplicación autónoma desde Windows o macOS. Meta Horizon Link es una ruta distinta y requiere Windows; no es un requisito de este laboratorio. [1]

::: pagebreak

## Si algo sale mal

| Síntoma | Revisión concreta |
| --- | --- |
| La imagen aparece como una pantalla plana. | Comprueba OpenXR y Meta Quest Support en Android, perfil activo y ejecución del APK dentro del visor. |
| La cámara no sigue la cabeza. | Revisa Tracked Pose Driver, acciones asignadas y el XR Origin. En el Editor verifica que el simulador esté activo. |
| Los controles no aparecen o no responden. | Revisa Oculus Touch Controller Profile, las acciones del prefab y que no haya errores. Usa los controles físicos para esta serie. |
| Hay altura duplicada o escala exagerada. | Revisa Floor, el piso del visor y las escalas de XR Origin, Entorno y sus padres. |
| Los materiales se ven magenta. | Comprueba el URP Asset efectivo y el shader de los materiales. |
| Quest no aparece en Run Device. | Revisa cable de datos, modo desarrollador y autorización USB. Desconecta y vuelve a autorizar antes de recompilar. |
| El simulador aparece dos veces. | Conserva la instancia automática para Editor y elimina la copia manual de la escena. |

## Análisis después del montaje

1. Explica qué diferencia observaste entre girar la cabeza y cambiar su posición. Usa el cubo y la mesa como referencias.
2. Predice el efecto de cambiar la escala del XR Origin de uno a diez. Analízalo sin utilizar esa modificación en el visor.
3. Distingue un error de escala de un error de altura. Indica qué campo y qué medida revisarías en cada caso.
4. Explica qué quedó comprobado en Unity, en el simulador y en Quest 3S. Señala las pruebas que no pudiste realizar.

::: pagebreak

## Entrega y rúbrica

Entrega Apellido_VR-C01.pdf, de 3 a 5 páginas. Incluye las versiones, la jerarquía, los ajustes OpenXR y URP, la sala con medidas, los resultados y las respuestas. Conserva Assets, Packages y ProjectSettings para reproducir el montaje. No subas Library ni un APK en lugar del reporte.

| Criterio | Puntos | Evidencia para obtener el total |
| --- | --- | --- |
| Monta la base XR. | 35 | Muestra paquetes, perfil, acciones, cámara y referencia Floor configurados. |
| Construye la sala. | 25 | Presenta los objetos con las dimensiones y la jerarquía indicadas. |
| Comprueba el comportamiento. | 20 | Registra pruebas del simulador o visor y diferencia resultados de predicciones. |
| Explica escala y seguimiento. | 20 | Responde las cuatro preguntas con referencias al montaje propio. |
| Total | 100 | La evaluación utiliza la evidencia del reporte y del proyecto conservado. |

Cada criterio recibe el total si cumple la evidencia, la mitad si está parcial pero verificable y cero si falta o contradice el funcionamiento analizado. La falta de un visor no impide entregar: documenta el montaje y la simulación, y explica qué queda pendiente.

## Referencias y alcance de la revisión

Los pasos se contrastaron con la documentación y los assets oficiales de XRI 3.3.2, incluidos el prefab XR Origin (XR Rig), sus acciones y las reglas de validación de Starter Assets. Este documento no acredita una compilación ejecutada en Unity ni una prueba física del autor con Quest 3S. La comprobación de cada montaje forma parte de la práctica.

[1] Meta. Consulta la preparación del equipo y del visor, y la configuración de software.

[Hardware Setup](https://developers.meta.com/vr/documentation/unity/unity-env-device-setup/)

[Software Setup](https://developers.meta.com/vr/documentation/unity/unity-software-setup/)

[2] Unity 6.3. Consulta el perfil Meta Quest y sus ajustes.

[Meta Quest build profile](https://docs.unity.com/en-us/engine/6000.3/manual/xr/configuring-project-for/meta-quest-develop/build-profile)

[3] Unity OpenXR. Consulta Meta Quest Support y el perfil de controladores.

[Meta Quest Support](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.16/manual/features/metaquest.html)

[Oculus Touch Controller Profile](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.16/manual/features/oculustouchcontrollerprofile.html)

[4] Unity XRI 3.3. Consulta los prefabs, acciones y jerarquía de Starter Assets.

[Starter Assets](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.3/manual/samples-starter-assets.html)

[5] Unity XRI 3.3. Consulta la instalación y el uso del simulador.

[XR Interaction Simulator](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.3/manual/xr-interaction-simulator-overview.html)
