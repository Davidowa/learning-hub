# VR-C00 | Primer montaje XR y torquímetro

Unity 6.3 LTS · URP · Meta Quest 3S · Montaje guiado introductorio

## Qué vas a construir

Crearás una aplicación de realidad virtual con un banco de trabajo y un torquímetro representado por un bloque de 30 cm. Podrás tomarlo con los controles, girarlo y soltarlo. Un mensaje registrará qué interactor lo seleccionó. La práctica prepara el proyecto, la entrada XR y la instalación en Quest 3S antes del análisis de los laboratorios siguientes.

VR-C00 adapta el antiguo Labo 03. Después, VR-C01 estudia presencia, escala y seguimiento; VR-C02 amplía las interacciones y la retroalimentación; VR-C03 incorpora locomoción. VR-C04 es opcional y aborda cibermareo y comodidad. Cada proyecto de referencia se puede abrir por separado.

El banco permite comprobar escala y agarre con una escena pequeña. El torquímetro es una representación geométrica: esta práctica no simula torque ni ajuste de tornillos. Utiliza los controles Touch; las manos que aparecen en pantalla representan esos controles y no acreditan seguimiento de manos sin controladores.

## Antes de empezar

- Instala Unity 6.3 LTS con Android Build Support, Android SDK & NDK Tools y OpenJDK. Registra el parche utilizado; el proyecto de referencia usa 6000.3.27f1.
- Prepara Quest 3S con sus dos controles, un cable USB de datos y modo de desarrollador. La depuración USB se autoriza dentro del visor al conectarlo a la computadora. [1]
- Trabaja con el límite físico del visor y un área despejada. La sala virtual no informa dónde hay muebles reales. Alterna el visor con un compañero para revisar el registro desde la computadora.
- Puedes revisar el montaje con XR Interaction Simulator. Documenta las pruebas pendientes si no tienes visor; el simulador no acredita escala percibida, seguimiento físico ni instalación del APK.

## Dos formas de trabajar

Para aprender el montaje, sigue las partes 1 a 6 desde un proyecto nuevo. Para revisar el ejemplo, extrae el ZIP y abre en Unity Hub la carpeta que contiene Assets, Packages y ProjectSettings. Espera la resolución de paquetes y la preparación automática de Assets/Scenes/VR-C00.unity. Si se interrumpe, revisa Console y usa Tools > Learning Hub VR > Preparar proyecto. Reconstruir reemplaza la escena de ejemplo; conserva una copia de tus cambios.

El ejemplo incluye una copia manual del simulador marcada EditorOnly y los eventos ya conectados. Compara su Inspector con la guía. La entrega debe permitir explicar el montaje y sus resultados.

::: pagebreak

## Parte 1: Crear y configurar el proyecto

1. En Unity Hub crea un proyecto Universal 3D llamado BancoVR, en una carpeta local. Esa plantilla utiliza URP. Crea Assets/Scenes, Assets/Materials y Assets/Scripts. Guarda la escena como Assets/Scenes/VR-C00.unity.
2. Abre File > Build Profiles > Add Build Profile. Agrega Meta Quest, selecciónalo y usa Switch Platform. Instala el módulo Android del Editor si falta. El perfil Meta Quest está disponible en Unity 6.3. [2]
3. En Window > Package Manager instala XR Interaction Toolkit 3.3.2. Si lo buscas por nombre, utiliza com.unity.xr.interaction.toolkit y versión 3.3.2. Instala OpenXR Plugin si el perfil no lo agregó; el proyecto de referencia utiliza OpenXR 1.16.1 y URP 17.3.0.
4. En Player Settings > Other Settings establece Active Input Handling en Input System Package (New). Reinicia el Editor si lo solicita. En Package Manager > XR Interaction Toolkit > Samples importa Starter Assets y XR Interaction Simulator de 3.3.2.
5. En Edit > Project Settings > XR Plug-in Management selecciona la pestaña Android. Activa OpenXR e Initialize XR on Startup. La configuración de escritorio es independiente y no habilita XR para el APK.
6. En OpenXR de Android habilita Meta Quest Support. En Enabled Interaction Profiles agrega Oculus Touch Controller Profile. En Project Validation selecciona Android y resuelve los errores. Revisa también las reglas de Starter Assets. [3]
7. En Player Settings verifica IL2CPP, ARM64, Minimum API Level 29 y Vulkan. Usa Target API Level automático y revisa las exigencias de Project Validation. Si el perfil tiene ajustes propios, comprueba sus valores efectivos. Esta práctica instala una app de prueba por USB; no prepara una publicación en una tienda.
8. En Project Settings > Graphics y Quality verifica que el URP Asset corresponda al perfil activo. Usa materiales Universal Render Pipeline/Lit. Conserva el Universal Renderer de la plantilla. No agregues componentes de AR ni passthrough a esta escena.

## Parte 2: Preparar la cámara y los controles

9. Busca XR Origin (XR Rig) en Assets/Samples/XR Interaction Toolkit/3.3.2/Starter Assets/Prefabs. Arrastra ese prefab a Hierarchy. Elimina la Main Camera original de la plantilla y conserva la Directional Light. [4]
10. Debe existir un XR Interaction Manager. Si falta, agrégalo con GameObject > XR > XR Interaction Manager. Revisa Input Action Manager en el rig: Action Assets debe contener XRI Default Input Actions del mismo sample.
11. En la raíz XR Origin pon Position y Rotation en cero y Scale en (1, 1, 1). En XR Origin selecciona Requested Tracking Origin Mode: Floor y verifica que Camera apunte a la Main Camera de Camera Offset. Conserva Tracked Pose Driver y las acciones del prefab.
12. Desactiva el hijo Locomotion. Conserva Smooth Motion Enabled y Smooth Turn Enabled desactivados en los Controller Input Action Manager. El laboratorio utiliza movimiento de cabeza y controles; no requiere desplazamiento por joystick.

Antes de continuar debe haber una sola cámara XR, un Audio Listener y un XR Interaction Manager. Una cámara adicional o acciones sin asignar pueden producir una vista incorrecta o controles sin respuesta.

::: pagebreak

## Parte 3: Construir el banco

13. Crea Entorno y, dentro, un objeto vacío Banco. Ambos deben tener posición y rotación cero y escala uno. Usa GameObject > 3D Object > Cube para crear los objetos de la tabla. Las posiciones de Mesa, Motor y Torquimetro son locales a Banco; Piso es hijo de Entorno.

| Objeto | Position (X, Y, Z) | Scale (X, Y, Z) |
| --- | --- | --- |
| Piso | (0, -0.05, 1) | (4, 0.1, 4) |
| Mesa | (0, 0.9, 1.2) | (1.6, 0.05, 0.8) |
| Motor | (-0.55, 1.13, 1.2) | (0.5, 0.4, 0.4) |
| Torquimetro | (0.25, 0.94, 1.2) | (0.30, 0.03, 0.04) |

14. Conserva los Box Collider y deja Is Trigger desactivado. Piso, Mesa y Motor no necesitan Rigidbody. Motor será una referencia estática. La cara superior de Mesa queda en Y = 0.925; la cara inferior del torquímetro empieza a esa altura.
15. Crea materiales URP/Lit: PisoGris, MesaClara, MotorOscuro y TorquimetroNaranja. Asígnalos desde Project. El torquímetro debe distinguirse de la mesa. Un material magenta requiere revisar su shader y el URP Asset efectivo.
16. Agrega Rigidbody a Torquimetro. Usa Mass: 0.5, Use Gravity activado, Is Kinematic desactivado, Interpolate: Interpolate y Collision Detection: Continuous Dynamic. La masa es un valor del ejercicio, no una medición de una herramienta real.
17. Agrega XR Grab Interactable al mismo objeto. Asigna el XR Interaction Manager de la escena. Usa Interaction Layer Mask: Default, Select Mode: Single y Movement Type: Kinematic. En Colliders agrega su Box Collider. Desactiva Throw On Detach para soltarlo sin velocidad de lanzamiento heredada. [5]
18. Conserva las referencias y acciones de los interactores del prefab. Default debe estar incluido en su Interaction Layer Mask. Las capas de interacción XRI filtran selección; son distintas de las capas físicas de Unity. No cambies una para intentar corregir la otra.

Movement Type: Kinematic indica cómo XRI mueve el objeto mientras se sostiene. Al soltarlo, XRI restaura el estado del Rigidbody, que en reposo se configuró como dinámico y con gravedad. La prueba de caída comprueba esa transición; el movimiento de la cámara no la comprueba.

## Jerarquía de referencia

```text
VR-C00
  Directional Light
  XR Interaction Manager
  XR Origin (XR Rig) / Camera Offset y controles
    Locomotion [desactivado]
  Entorno
    Piso
    Banco / Mesa, Motor y Torquimetro
  DiagnosticoXR
  XR Interaction Simulator (EditorOnly)
```

El esquema resume el prefab. Conserva sus demás hijos y componentes. Banco pertenece a Entorno y no debe ser hijo de la cámara ni de un control.

::: pagebreak

## Parte 4: Agregar diagnóstico y evento de selección

19. Crea DeviceReport.cs en Assets/Scripts. Copia este código y agrega el componente a un GameObject vacío llamado DiagnosticoXR.

```csharp
using UnityEngine;
using UnityEngine.XR;

public sealed class DeviceReport : MonoBehaviour
{
    void Start()
    {
        Debug.Log($"VR-C00 | platform={Application.platform}");
        Debug.Log($"VR-C00 | graphics={SystemInfo.graphicsDeviceType}");
        Debug.Log($"VR-C00 | editor={Application.isEditor}");
        Debug.Log($"VR-C00 | xrEnabled={XRSettings.enabled}");
    }
}
```

En Quest se espera platform=Android, graphics=Vulkan, editor=False y xrEnabled=True con la configuración indicada. El valor de xrEnabled se registra al ejecutar Start; revísalo junto con la vista estéreo y la respuesta de la cabeza. En el Editor la plataforma y la API gráfica dependen de la computadora. No uses WindowsEditor o Direct3D11 como valores obligatorios en macOS.

20. Crea WrenchLog.cs y agrega su componente a Torquimetro. El nombre del archivo debe coincidir con el de la clase.

```csharp
using UnityEngine;
using UnityEngine.XR.Interaction.Toolkit;

public sealed class WrenchLog : MonoBehaviour
{
    public void Held(SelectEnterEventArgs args)
    {
        string interactor = args.interactorObject.transform.name;
        Debug.Log($"VR-C00 | Torquimetro tomado por {interactor}");
    }
}
```

21. En XR Grab Interactable abre Interactable Events > Select Entered. Pulsa +, arrastra Torquimetro a la ranura del objeto y selecciona WrenchLog > Held en la sección Dynamic SelectEnterEventArgs. Debe haber una sola conexión. Guarda la escena.
22. Cuando se selecciona el objeto, el evento entrega los datos del interactor. El método lee su nombre durante esa llamada y escribe el registro. Un control puede tener varios interactores; el mensaje identifica al que seleccionó el objeto, no una mano anatómica.

Select toma el objeto. Activate corresponde a una acción secundaria mientras se sostiene, si está configurada. Con Starter Assets, Select normalmente usa grip; consulta las acciones del prefab si cambias los bindings. Presionar el gatillo de Activate no garantiza que ocurra Select Entered.

::: pagebreak

## Parte 5: Revisar con el simulador

23. Arrastra el prefab XR Interaction Simulator del sample a Hierarchy. Pon su Tag en EditorOnly para excluirlo del APK. En Project Settings > XR Plug-in Management > XR Interaction Toolkit deja Use XR Interaction Simulator in scenes desactivado: esta guía utiliza una instancia manual. [6]
24. Si abriste el proyecto de referencia, la instancia manual ya existe. Conserva una sola. Pulsa Play y da foco a Game. Consulta la ayuda en pantalla para elegir cabeza o controles y para ejecutar Select; los bindings del simulador no son los botones físicos de Quest.
25. Mueve la cabeza simulada. El banco debe permanecer en Entorno. Acerca un control a Torquimetro o usa el interactor a distancia del prefab. Ejecuta Select, mueve el control y libera Select. Observa el mensaje de WrenchLog en Console.
26. Suelta la herramienta sobre la mesa y después fuera de ella. Debe apoyarse en la mesa o caer al piso. Detén Play y vuelve a iniciarlo para recuperar la posición inicial. Las modificaciones durante Play no sustituyen los valores guardados de la escena.

## Parte 6: Instalar y probar en Quest 3S

27. Conecta el visor mediante USB, despiértalo y acepta la depuración USB para esa computadora. En File > Build Profiles selecciona Meta Quest y comprueba que Quest aparezca en Run Device. Si necesitas diagnóstico por terminal, usa el adb del SDK asignado en Edit > Preferences > External Tools.
28. Agrega Assets/Scenes/VR-C00.unity a Scene List y déjala como única escena habilitada en el perfil. Activa Development Build para obtener registros. Revisa Project Validation de Android y usa Build And Run.
29. Abre la aplicación instalada en el visor. Debe mostrar el banco en estéreo y responder al movimiento de cabeza y controles. Una ventana plana dentro del entorno del visor no acredita que la aplicación se esté ejecutando en modo XR.
30. Toma Torquimetro con Select, gíralo y suéltalo sobre la mesa. Repite con el otro control. Después suéltalo fuera de la mesa. Mantente dentro del límite físico; no busques alcanzar una mesa virtual fuera de tu zona despejada.
31. Revisa los registros desde Window > Analysis > Android Logcat si tienes ese paquete instalado, o ejecuta adb logcat desde el SDK. Busca VR-C00 y copia los cuatro mensajes de DeviceReport y al menos un mensaje de WrenchLog por control.
32. Sin modificar la escala de XR Origin, describe si la altura de la mesa y los 30 cm del bloque corresponden a lo que esperabas. La cubierta termina a 92.5 cm del piso virtual. Alterna el visor con tu compañero para que cada quien revise su propio proyecto.

Build And Run instala una app autónoma por USB desde Windows o macOS. No requiere Meta Horizon Link. El registro permite conocer la plataforma ejecutada; la prueba física permite observar perspectiva, escala y respuesta del visor.

::: pagebreak

## Localizar adb sin fijar una ruta de otro equipo

En Windows abre PowerShell. Usa como punto de partida la ruta de Android SDK que muestre External Tools. La instalación por defecto suele estar dentro del Editor seleccionado en Unity Hub. Esta búsqueda sirve si Unity está en Program Files:

```powershell
Get-ChildItem "C:\Program Files\Unity" -Filter adb.exe -Recurse -ErrorAction SilentlyContinue
```

La búsqueda puede devolver varias versiones. Elige la del Editor utilizado y ejecuta el archivo con su ruta completa, por ejemplo:

```powershell
& "C:\ruta\al\SDK\platform-tools\adb.exe" devices
& "C:\ruta\al\SDK\platform-tools\adb.exe" logcat
```

En macOS, copia la ruta del SDK de External Tools y usa Terminal:

```bash
"/ruta/al/SDK/platform-tools/adb" devices
"/ruta/al/SDK/platform-tools/adb" logcat
```

Sustituye esas rutas por la de tu instalación. En devices, device indica que existe una conexión autorizada; unauthorized requiere aceptar el aviso dentro del visor. Si no aparece ningún dispositivo, revisa el cable, el modo de desarrollador y la conexión USB antes de recompilar.

## Si algo sale mal

| Síntoma | Revisión concreta |
| --- | --- |
| La app abre como pantalla plana. | Comprueba OpenXR y Meta Quest Support en Android, el perfil activo y el APK que ejecutaste. |
| La cabeza o los controles no responden. | Revisa el perfil Oculus Touch, Input Action Manager, Tracked Pose Driver y las acciones del sample. |
| El objeto no se puede tomar. | Comprueba XR Grab Interactable, Collider, Interaction Manager, capa Default y la acción Select. |
| Se toma, pero no aparece el mensaje. | Revisa WrenchLog y la conexión dinámica de Select Entered. No conectes ese método a Activated. |
| El objeto atraviesa la mesa al caer. | Conserva Box Collider sin Is Trigger en mesa y herramienta. Revisa Rigidbody, gravedad y detección de colisiones. |
| El objeto queda flotando al soltarlo. | En modo de edición, deja Is Kinematic desactivado y Use Gravity activado. Revisa que otro script no fije su Transform. |
| El simulador aparece dos veces. | Conserva la copia manual con Tag EditorOnly y desactiva su instancia automática. |
| La altura o la escala no corresponden. | Revisa el piso definido en Quest, el modo Floor y Scale=(1,1,1) de XR Origin y Banco. |

::: pagebreak

## Entrega y análisis

Conserva el proyecto completo con Assets, Packages y ProjectSettings. Entrega un video breve de las pruebas y un reporte Apellido_VR-C00.pdf de 2 a 3 páginas. Incluye las versiones de Unity y paquetes, la jerarquía, los valores de Rigidbody y XR Grab Interactable, la conexión de Select Entered y los registros obtenidos. Identifica si cada prueba se realizó en simulador o visor.

El video debe mostrar el banco, el cambio de perspectiva, la selección con cada control y la liberación sobre la mesa y fuera de ella. Si no tienes visor, muestra el simulador y señala como pendientes la instalación, el seguimiento físico y la escala percibida. No presentes resultados simulados como mediciones del dispositivo.

Responde estas preguntas con referencias a tu proyecto:

1. ¿Qué aportan URP, OpenXR y XRI al montaje? Indica un ajuste que comprobaste de cada uno.
2. ¿Qué diferencia hay entre el seguimiento de los controles y el seguimiento de manos sin controladores? ¿Cuál utilizaste?
3. ¿Qué cambia entre Select y Activate? Identifica la acción que produjo el mensaje de WrenchLog.
4. ¿Qué componentes explican que el torquímetro siga al control y después caiga? Distingue el movimiento durante el agarre del estado al soltar.
5. ¿Qué confirmó el registro y qué necesitó una observación dentro del visor? Señala los resultados que todavía no pudiste comprobar.

## Rúbrica de referencia

| Criterio | Puntos | Evidencia para obtener el total |
| --- | --- | --- |
| Prepara el proyecto XR. | 30 | Muestra URP, paquetes, OpenXR de Android, perfil, cámara y acciones asignadas. |
| Construye el banco y el agarre. | 30 | Presenta medidas, colliders, Rigidbody y XR Grab Interactable configurados. |
| Conecta y comprueba los eventos. | 25 | Muestra Select Entered, el mensaje del interactor y las pruebas de liberación. |
| Explica los resultados. | 15 | Responde las cinco preguntas y distingue simulación, visor y pruebas pendientes. |
| Total | 100 | La evaluación utiliza evidencia verificable del montaje propio. |

Cada criterio recibe el total si cumple la evidencia, la mitad si está parcial pero verificable y cero si falta o contradice el funcionamiento analizado. La prueba pendiente de visor debe quedar declarada; no reemplaces esa observación por una afirmación sin evidencia.

::: pagebreak

## Referencias y alcance

El montaje se contrastó con la documentación oficial y el código de XRI 3.3.2. Se revisaron la sintaxis y el contenido del proyecto. Durante la preparación no se ejecutó Unity ni se probó un Quest 3S. La importación, la compilación y las pruebas físicas forman parte de la comprobación del laboratorio.

[1] [Meta: preparación del visor](https://developers.meta.com/vr/documentation/unity/unity-env-device-setup/).

[2] [Unity 6.3: perfil Meta Quest](https://docs.unity.com/en-us/engine/6000.3/manual/xr/configuring-project-for/meta-quest-develop/build-profile).

[3] [OpenXR: Meta Quest Support](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.16/manual/features/metaquest.html).

[4] [XRI 3.3: Starter Assets](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.3/manual/samples-starter-assets.html).

[5] [XRI 3.3: XR Grab Interactable](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.3/manual/xr-grab-interactable.html).

[6] [XRI 3.3: XR Interaction Simulator](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.3/manual/xr-interaction-simulator-overview.html).
