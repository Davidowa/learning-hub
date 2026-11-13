# Laboratorios de realidad aumentada 03 a 06: memoria de trabajo

Fecha de cierre de esta revisión: 12 de noviembre de 2026.

Esta memoria recoge la revisión de los proyectos Unity, las guías, las compilaciones, la infografía y la publicación en Blackboard. Documenta también los límites de la validación y los problemas que todavía requieren información de los alumnos. Los trabajos del chat sobre alumnos, hojas de cálculo y otros repositorios no forman parte de estos materiales del curso.

## Ubicación y contenido

La carpeta se preparó en `F:/David/Downloads/Laboratorios-03-a-06`. Por solicitud del docente se trasladó completa a `ppts/unity/ar-mobile/labs/Laboratorios-03-a-06` dentro del repositorio `Davidowa/learning-hub`.

Cada laboratorio conserva una base para el alumno y una solución de referencia. Las bases contienen los scripts, los paquetes y la configuración de partida; el alumno construye la escena, los prefabs y las conexiones del Inspector. Las soluciones incluyen `Assets/Scenes/Laboratorio.unity` con las referencias resueltas. No se requiere escribir C# para completar estas actividades.

| Carpeta | Resultado esperado |
| --- | --- |
| `Lab03-Base` y `Lab03-Solucion` | Se reconoce una imagen, se lanza una esfera y se conserva localmente la captura del objetivo. |
| `Lab04-Base` y `Lab04-Solucion` | Se colocan dos tipos de contenido sobre superficies, se seleccionan y eliminan figuras y se ocultan las superficies. |
| `Lab05-Base` y `Lab05-Solucion` | Se reconoce ArUco DICT_4X4_50 ID23 y se verifica la alineación de sus cuatro esquinas con la imagen de cámara. |
| `Lab06-Base` y `Lab06-Solucion` | Un QR selecciona el contenido y un toque posterior sobre una superficie permite colocarlo. |
| `Entregas` | Contiene los ocho ZIP publicados, los cuatro PDF R2, los hashes y el paquete de guías. |
| `Infografia` | Conserva el PDF de dos páginas sobre OnGUI y Canvas y las vistas previas de sus páginas. |
| `Soporte-tecnico` | Conserva los generadores y las pruebas de preparación del docente. No forma parte del trabajo del alumno. |

Los archivos `Guia.md` son las fuentes editables de las guías. Cada `Guia.pdf` corresponde al Markdown de su proyecto. Las versiones incluidas en los ZIP coinciden con los PDF publicados por separado.

## Versiones y configuración que se conservaron

Se utilizó Unity 6000.3.27f1 con Universal RP 17.3.0, AR Foundation 6.3.5, ARCore XR Plugin 6.3.5, XR Core Utils 2.5.1, XR Plug-in Management 4.5.3, Input System 1.11.2 y uGUI 2.0.0. La configuración Android usa IL2CPP, ARM64, OpenGLES3, API mínima 25 y API destino 36.

Los archivos `Packages/manifest.json` y `packages-lock.json` se conservan juntos. URP debe estar asignado en Graphics y no tener un override incompatible en Quality. El renderer incluye AR Background Renderer Feature. Se conserva `Assets/link.xml` y Strip Engine Code permanece desactivado.

## Validación de los proyectos y compilación Android

Las cuatro soluciones se importaron en copias de trabajo y aprobaron las pruebas de escena, interfaz y simulación en Unity 6000.3.27f1. Las cuatro bases también se importaron sin errores de compilación. Las pruebas de entrada sintética se ejecutan dentro del PlayerLoop; ejecutarlas desde EditorApplication.update puede utilizar otro estado del Input System y producir un fallo del test que no equivale a un fallo del botón en el dispositivo.

Se compilaron los cuatro APK con IL2CPP para ARM64 y resultado Succeeded, con cero errores de Unity. El comando principal `Tools > Laboratorio > Compilar APK Android` usa el flujo directo de BuildPipeline.BuildPlayer. Guarda el APK y el registro `.build.txt` en la carpeta APK situada junto a la raíz del proyecto. El comando `Tools > Laboratorio > Exportar y compilar con Gradle (alternativo)` conserva la exportación para quien la necesite.

En esta computadora, Windows bloqueó una copia de `il2cpp.dll` dentro de una exportación Gradle. El flujo directo utilizó la herramienta instalada de Unity y permitió completar la compilación. No se modificaron las políticas de seguridad de Windows para resolverlo. Ese problema de compilación debe distinguirse de los errores de interacción o rastreo.

En un Pixel 9 con Android 17 se comprobaron la instalación y el arranque de Lab06. El docente confirmó que detectó el QR. No quedó documentada en esta revisión una prueba física completa de colocación, selección y eliminación de Lab06, ni las pruebas físicas completas de Lab03, Lab04 y Lab05. Los registros de versiones anteriores no validan automáticamente la edición actual con Canvas.

Los APK son productos de compilación y pueden regenerarse desde las soluciones. Los proyectos y los registros de validación se conservan en el repositorio; los APK no se añaden al historial Git.

## Problemas de interfaz que se distinguieron

Las versiones anteriores combinaban OnGUI con lectura manual del toque. La edición actual usa Canvas, Button.onClick, un EventSystem e InputSystemUIInputModule. En los laboratorios de colocación, el código comprueba si el toque está sobre la UI antes de procesarlo en el mundo. GraphicRaycaster, por sí solo, no cancela el código personalizado que lee toques para colocar objetos.

La documentación oficial de Input System 1.11 indica que OnGUI no recibe eventos de entrada en ejecución cuando Active Input Handling usa únicamente Input System Package. Both permite ejecutar el ejemplo didáctico de OnGUI mediante la entrada anterior. Esa configuración del ejemplo no exige cambiar los laboratorios, que conservan Input System Package (New).

Un botón dibujado tampoco garantiza que tenga callback, que las acciones de entrada estén asignadas o que una Image transparente no lo cubra. Eliminar selección requiere una figura seleccionada. Lanzar requiere un objetivo rastreado sin capturar. En Lab06, detectar el QR selecciona contenido; colocarlo requiere además seguimiento y un plano detectado.

El historial del APK original de Lab04 registró la eliminación de CapsuleCollider y un fallo en MakePreview antes de completar la inicialización. Se conservaron link.xml y Strip Engine Code desactivado para atender esa causa. No se atribuyen todos los problemas de los alumnos a ese fallo ni a la incompatibilidad de OnGUI sin revisar Console o Logcat.

## Auditoría y corrección de las guías R2

El docente informó que los alumnos tenían problemas para completar la práctica 4. La comparación de los ZIP confirmó que los nueve scripts de Lab04 eran idénticos en base y solución. La guía anterior contenía las piezas principales, pero pedía conectar botones con Laboratorio antes de explicar cómo crearlo; también utilizaba XR Origin antes de construirlo.

El verificador de escena resultó parcial. Puede omitir botones sin asignar, no comprueba las referencias Planes, Raycasts y Anchors y no confirma que cada botón tenga el método esperado. Su mensaje CONFIGURACION CORRECTA no sustituye una revisión de las conexiones y la prueba de cada acción. La corrección de las guías no modificó ese verificador ni el comportamiento de los proyectos.

Las cuatro guías se contrastaron con los controladores, los catálogos, las escenas y los prefabs de sus respectivas soluciones. Se reorganizaron para crear primero los objetos, construir después los recursos y la interfaz, conectar las referencias y, por último, ejecutar las pruebas y compilar.

La revisión añadió tablas de callbacks, acciones de InputSystemUIInputModule, referencias de Laboratorio, campos de ContenidoLab y estados activo/inactivo. También añadió la jerarquía final, la obligación de crear los botones como hijos directos del Canvas y comprobaciones manuales que complementan el verificador. Las pruebas Android se colocaron después de la compilación; cada guía conserva solo las instrucciones de su laboratorio.

| Guía R2 | Páginas | Archivos de Assets, Packages y ProjectSettings de la base comprobados sin cambios |
| --- | --- | --- |
| Lab03 | 9 | 96 |
| Lab04 | 10 | 90 |
| Lab05 | 9 | 93 |
| Lab06 | 10 | 111 |

Se revisaron la redacción con the-writer, el texto extraído, los márgenes y las páginas renderizadas. Los cuatro documentos quedaron sin hallazgos HIGH del lint de redacción. En los ocho ZIP solo cambiaron Guia.md y Guia.pdf; los scripts, las escenas, los prefabs, los paquetes y la configuración se conservaron. Quien ya empezó puede usar el PDF nuevo sin reiniciar su proyecto.

Esta revisión contrasta documentación y archivos finales. No equivale a una reconstrucción manual independiente de las cuatro actividades por un alumno ni a nuevas pruebas físicas completas en Android.

## LabContent y el menú Contenido

Los alumnos preguntaron cómo crear LabContent y después informaron que tampoco veían Contenido en el menú. Las cuatro guías incluyen ahora una explicación explícita en la sección 5.

1. En Project, se abre o crea Assets/Configuracion.
2. Con clic derecho dentro de esa carpeta se elige Create > Laboratorios > Contenido. También está disponible la ruta Assets > Create > Laboratorios > Contenido del menú superior.
3. Se conserva el nombre ContenidoLab del asset creado. LabContent es su tipo; ContenidoLab.asset es el archivo que almacena referencias.
4. Se llenan los campos propios del laboratorio y se arrastra el asset al campo Content del controlador en Laboratorio. LabContent no se añade con Add Component.

El archivo `Assets/Scripts/Course/LabContent.cs` ya está en las ocho carpetas. Su atributo CreateAssetMenu declara `menuName="Laboratorios/Contenido"` y `fileName="ContenidoLab"`.

En una copia de la base de Lab04 se comprobó con Unity 6000.3.27f1 que ExecuteMenuItem reconoce `Assets/Create/Laboratorios/Contenido`. El comando devolvió True. En modo batch no se completó el flujo interactivo de nombrar el asset; una creación directa del ScriptableObject mediante AssetDatabase se guardó y volvió a cargar correctamente. Eso confirma el tipo y el registro del comando en la copia probada, no el estado del proyecto de cada alumno.

Sigue pendiente recibir el primer error rojo completo de Console y confirmar si el alumno ve LabContent.cs en Project. Sin esa información no se determinó por qué el menú falta en sus equipos. No se indicó crear otra clase con el mismo nombre ni sustituir los proyectos por la solución para ocultar el problema.

## Infografía de OnGUI y Canvas

Se preparó una primera infografía y después una versión de dos páginas con el estilo de Learning Hub. Tras la observación de que el material parecía demasiado genérico, se rehízo como un ejercicio de nueve pasos: construir un botón Lanzar con OnGUI, conservar la acción, crear el botón en Canvas, conectar On Click y comprobar el mensaje en Console.

La versión conservada está en `Infografia/OnGUI-y-Canvas-Learning-Hub.pdf`. Utiliza los recursos gráficos de Learning Hub, tipografía editorial y redacción trabajada con the-writer. El ejemplo OnGUI se plantea en un proyecto aparte para no alterar la configuración de los laboratorios que ya usan los alumnos.

La página 1 explica la compatibilidad entre OnGUI y el sistema de entrada. La infografía no contiene una cronología completa del error histórico de CapsuleCollider de Lab04; ese antecedente queda documentado en esta memoria y en la guía de la práctica 4. Si se amplía la explicación del error anterior, deben distinguirse ambas causas.

## Estado publicado en Blackboard

Se actualizaron las actividades y los documentos existentes; se conservaron sus instrucciones de entrega, puntos y ajustes de evaluación. Cada actividad de las prácticas 3 a 6 contiene un ZIP de base y su guía R2. Los ocho ZIP de solución también contienen las guías corregidas.

| Curso | Identificador | Visibilidad de actividades 3 y 4 | Visibilidad de actividades 5 y 6 |
| --- | --- | --- | --- |
| Realidad Virtual | `_106272_1` | Visibles | Ocultas, por indicación del docente |
| Temas Selectos de Ingeniería V | `_106070_1` | Visibles | Visibles, por indicación del docente |

Cada solución tiene una regla de actividad con requisito Intento enviado sobre su práctica correspondiente y la opción Ocultar hasta cumplir las condiciones. Durante la comprobación se encontraron soluciones sin la regla esperada o con disponibilidad distinta de la indicada anteriormente. Se corrigieron y las ocho reglas se comprobaron de nuevo después de recargar la página. No basta con observar una regla recién editada antes de confirmar que persiste.

| Práctica | Actividad en Realidad Virtual | Solución en Realidad Virtual | Actividad en Temas Selectos | Solución en Temas Selectos |
| --- | --- | --- | --- | --- |
| 3 | `_4672830_1` | `_4704961_1` | `_4672992_1` | `_4704983_1` |
| 4 | `_4672838_1` | `_4704941_1` | `_4686657_1` | `_4704950_1` |
| 5 | `_4672844_1` | `_4704971_1` | `_4672998_1` | `_4704986_1` |
| 6 | `_4672846_1` | `_4704979_1` | `_4673000_1` | `_4704991_1` |

La infografía está oculta en ambos cursos. Sus documentos son `_4704996_1` en Realidad Virtual y `_4704993_1` en Temas Selectos. La carpeta de soluciones se llama Soluciones de laboratorios 03 a 06 y permite que cada documento aplique su propia condición.

Para localizar una actividad se usa `https://blackboard.up.edu.mx/ultra/courses/ID_CURSO/assessment/test/ID_ACTIVIDAD?gradeitemView=details`. Para una solución se usa `https://blackboard.up.edu.mx/ultra/courses/ID_CURSO/document/ID_DOCUMENTO?view=content&state=view`. Los identificadores anteriores son referencias de mantenimiento; el acceso sigue dependiendo de la sesión y los permisos del usuario.

## Pendientes y continuidad

El diagnóstico del menú Contenido en los equipos de los alumnos necesita el error de Console o la confirmación de que el script falta. La validación física completa de la edición actual sigue pendiente en los términos descritos antes. También debe comprobarse la alineación física de las cuatro esquinas de ArUco en Lab05; su simulación estática no demuestra esa alineación.

El archivo CONTEXTO-PARA-OTRO-AGENTE.txt se conserva como historial del 5 de noviembre. Sus indicaciones de no compilar APK o no publicar en Blackboard fueron sustituidas por autorizaciones posteriores del docente. Para el estado de esta revisión deben consultarse esta memoria, las guías R2 y los registros actuales de Validacion.

Las copias de trabajo, los logs completos y el proyecto temporal usado para probar el menú se mantuvieron fuera de los proyectos que se entregan al alumno. Las pruebas y los generadores docentes no deben convertirse en un botón que resuelva automáticamente la actividad del alumno.

## Fuentes técnicas

- [Unity: ScriptableObject y CreateAssetMenu](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ScriptableObject.html).
- [Input System 1.11: soporte de UI e IMGUI](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.11/manual/UISupport.html).
- [AR Foundation 6.3](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.3/manual/index.html).
- [ReportLab: tablas](https://docs.reportlab.com/reportlab/userguide/ch7_tables/).
