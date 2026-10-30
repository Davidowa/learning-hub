# Laboratorios guiados de VR

Esta serie utiliza Unity 6.3 LTS, URP, OpenXR y XR Interaction Toolkit 3.3.2 para Meta Quest 3S. VR-C00 adapta el antiguo Labo 03 como introducción; VR-C01 a VR-C04 continúan la serie. Las prácticas AR se conservan por separado.

Cada guía explica qué construir, qué preparar, cómo configurar la escena y el Inspector, cómo probarla y qué revisar si falla. Después del montaje se solicita un análisis conceptual y evidencia. VR-C02 y VR-C03 parten de una copia de la escena anterior, como la práctica 2 de AR.

| Código | Montaje | Configuración en Blackboard |
| --- | --- | --- |
| VR-C00 | Configura XR y construye un banco con torquímetro, agarre, diagnóstico y evento de selección. | Actividad existente renombrada, oculta, 100 puntos. |
| VR-C01 | Prepara paquetes, perfil Meta Quest, OpenXR, XR Origin, sala con medidas, simulador y compilación. | Actividad oculta, 100 puntos, sin fecha. |
| VR-C02 | Agrega una herramienta que se toma, eventos de hover, interruptor, luz y script de estado. | Actividad oculta, 100 puntos, sin fecha. |
| VR-C03 | Configura área y anchors de teletransporte, snap turn y Canvas con UI XR. | Actividad oculta, 100 puntos, sin fecha. |
| VR-C04 | Agrega un menú de preferencias con restauración de valores y salida; analiza cibermareo. | Recurso opcional oculto, sin columna de calificación. |

Las fuentes editables son los cinco archivos `.es.md`; los scripts completos están en `scripts/` y dentro de las guías. `render_guides.py` genera los PDF tamaño carta en `output/pdf/`, con la paleta Unity de `ppts/kit/tokens.py`. Requiere ReportLab; `--output-dir` permite elegir otra carpeta.

La estructura de las seis guías AR locales se comprobó en sus fuentes y PDF: incluyen preparación, montaje o apertura del proyecto, configuración Android, pruebas y solución de problemas. La primera versión de VR se amplió para incluir ese procedimiento, además del análisis.

Los componentes, las acciones, los campos y las propiedades públicas de ControllerInputActionManager se contrastaron con el paquete oficial XRI 3.3.2. Las guías enlazan documentación oficial de Unity y Meta. No se ejecutó Unity ni se probó físicamente Quest 3S durante esta revisión; las guías explicitan ese límite.

Los materiales pertenecen a Laboratorios del curso Realidad Virtual_164956_M26PRIMAVERA_MEING2438520. Los reportes de VR-C01 a VR-C03 tienen una extensión de 3 a 5 páginas; VR-C00 solicita de 2 a 3 páginas y un video. Las cuatro rúbricas suman 100 puntos cada una. El simulador permite registrar comprobaciones cuando no se dispone de visor; no acredita seguimiento físico ni comodidad.

- [VR-C00 en Blackboard](https://blackboard.up.edu.mx/ultra/courses/_106272_1/assessment/test/_4638903_1?gradeitemView=details).
- [VR-C01 en Blackboard](https://blackboard.up.edu.mx/ultra/courses/_106272_1/assessment/test/_4672532_1?gradeitemView=details).
- [VR-C02 en Blackboard](https://blackboard.up.edu.mx/ultra/courses/_106272_1/assessment/test/_4672540_1?gradeitemView=details).
- [VR-C03 en Blackboard](https://blackboard.up.edu.mx/ultra/courses/_106272_1/assessment/test/_4672544_1?gradeitemView=details).
- [VR-C04 opcional en Blackboard](https://blackboard.up.edu.mx/ultra/courses/_106272_1/file/_4672547_1?courseId=_106272_1).

Las versiones ampliadas se reemplazaron el 30 de octubre de 2026. Se comprobaron en Blackboard los adjuntos guardados y la visibilidad oculta. Las tres actividades conservan 100 puntos y no tienen fecha de entrega; el PDF de cibermareo sigue como recurso opcional.

## Proyectos fuente de Unity

Los cinco proyectos se empaquetaron en Downloads, dentro de `Learning Hub - VR Conceptual - Quest 3S - URP/Proyectos Unity`. Cada ZIP incluye Assets, Packages, ProjectSettings, los samples oficiales de XRI 3.3.2, la guía y un LEEME. El asistente del Editor genera la escena editable al abrir el proyecto; no se incluye un APK ni una escena probada en el visor.

El código reproducible del asistente y del empaquetador está en project-kit. Para regenerar las carpetas y los ZIP, ejecuta package_projects.py con `--xri-package` apuntando al paquete oficial extraído y `--output-dir` apuntando a una carpeta nueva. El script evita sobrescribir proyectos existentes.

Se comprobaron 473 archivos por ZIP, la integridad de los cuatro archivos comprimidos, la ausencia de GUID duplicados y la sintaxis C# de los cuatro scripts propios en cada proyecto. La comprobación sintáctica utiliza Tree-sitter; no sustituye la compilación de Unity ni verifica todas las referencias de ensamblados.

Los cuatro ZIP se cargaron el 30 de octubre de 2026 en la carpeta Laboratorios de Blackboard, cada uno debajo de su actividad o guía correspondiente. Se comprobó en el listado que los cuatro archivos están ocultos para los estudiantes. Sus identificadores de contenido son `_4672749_1` (VR-C01), `_4672760_1` (VR-C02), `_4672771_1` (VR-C03) y `_4672782_1` (VR-C04 opcional). Las guías PDF también están cargadas y ocultas.

## Introducción VR-C00

El 30 de octubre de 2026 se revisó la guía del antiguo Labo 03 y se preparó VR-C00 como introducción. Se aclararon el uso de controles Touch, la diferencia entre Select y Activate, el estado del Rigidbody y las pruebas del Editor y del visor. La guía tiene ocho páginas tamaño carta e incluye las rutas de diagnóstico para Windows y macOS.

El ZIP VR-C00 contiene 477 archivos y seis scripts propios. Se comprobó su integridad, la sintaxis C#, los GUID y la coincidencia entre los dos scripts de la guía y los del proyecto. La importación en Unity, la compilación y las pruebas en Quest 3S siguen pendientes. Para regenerar solo esta introducción se puede pasar `--lab 0` al empaquetador y `--lab VR-C00` al renderizador. Los cuatro ZIP anteriores no se reemplazaron.

VR-C00 conserva el identificador de actividad `_4638903_1`, sus 100 puntos, un intento y la fecha anterior del 16 de septiembre de 2026 a las 23:59 (UTC-6). Se verificaron el título nuevo, las instrucciones guardadas y la vista previa del PDF de ocho páginas en Blackboard. El ZIP quedó oculto debajo de la actividad, con identificador `_4672822_1`.

Se revisaron los títulos y las instrucciones guardadas de VR-C00 a VR-C03, además de la descripción del recurso opcional VR-C04. En VR-C00 se eliminó un bloque duplicado con letras acentuadas incompletas. Se verificaron después del guardado palabras como aplicación, cámara, torquímetro, introducción, guía, páginas y configuración. Los demás textos revisados conservaban los acentos.
