# Práctica 1 · Un torquímetro que se levanta, en el visor

La primera práctica guiada de VR. Parte de un proyecto vacío de Unity 6 y termina en una app instalada en el visor que abre mostrando el banco de trabajo en estéreo, con las dos manos rastreadas y un torquímetro sobre la mesa que puedes alcanzar, levantar, girar y soltar. La consola dice cuál de las dos manos lo tomó. Nada de esto se juzga desde el monitor: la escena no está terminada hasta que te pusiste el visor y mediste con las manos si la mesa quedó a la altura correcta.

La guía está armada para evitar las dos fallas que más aparecen en esta práctica. La primera es compilar y que la app abra como una ventana plana flotando en el menú del visor, sin estéreo y sin manos. Eso no es un error de la escena: es que el build salió sin proveedor de XR, porque OpenXR quedó marcado en la pestaña de escritorio y no en la de Android, y entonces Android corre la app como cualquier app 2D. La segunda es que todo se vea bien, las manos se muevan y el gatillo no haga absolutamente nada. Eso casi siempre es un perfil de interacción que falta, o el Input Action Manager que nunca habilitó las acciones.

El visor es el del salón y se trabaja en parejas, pero cada quien arma su propio proyecto y entrega el suyo. La pareja sirve para las pruebas del final: quien tiene el visor puesto no puede ver la consola, y quien está afuera no puede ver lo que de verdad está pasando.

## Lo que necesitas antes de empezar

- Unity 6 instalado con el módulo **Android Build Support**, incluidos SDK, NDK y OpenJDK.
- El visor del salón y su cable USB-C. Que lleve datos, no solo corriente: un cable de carga es la causa más común de que `adb` no vea nada.
- El visor ya en modo desarrollador. Los del salón ya vienen así. Si te toca uno de cero, los pasos están en el apéndice.
- Dos metros por dos metros de piso libre, y alguien cerca mientras traes el visor puesto.

## Parte 1 · El proyecto y los paquetes

1. Crea un proyecto nuevo de Unity 6 con la plantilla **Universal 3D**. Nómbralo `Banco`, sin espacios en la ruta y fuera de OneDrive.
2. Abre **Window > Package Manager**, entra a Unity Registry e instala el **XR Interaction Toolkit**. Ese paquete jala XR Plug-in Management por su cuenta.
3. Instala también el **OpenXR Plugin** desde el mismo registro. OpenXR es el estándar que habla con el runtime del visor, y el Toolkit es lo que convierte ese rastreo en manos que agarran cosas. Los dos hacen falta.
4. Sin salir del Package Manager, selecciona el XR Interaction Toolkit, abre su pestaña **Samples** e importa **Starter Assets**. De ahí sale el rig ya armado, con las dos manos y sus interactores. Armarlo componente por componente es un ejercicio distinto y más largo.

## Parte 2 · Decirle al build que es de XR

5. Abre **Edit > Project Settings > XR Plug-in Management** y entra a la **pestaña de Android**, la del muñeco verde. Marca **OpenXR**. Esta es la casilla de la primera falla. Marcarla en la pestaña de Windows no cambia nada de lo que se instala en el visor, y las dos pestañas se ven casi idénticas.
6. Entra a **XR Plug-in Management > OpenXR**, todavía en Android. En **Interaction Profiles** presiona el más y agrega **Oculus Touch Controller Profile**. Sin un perfil de interacción los controles se rastrean y ningún botón reporta nada. Esa es la segunda falla.
7. En esa misma página, bajo **OpenXR Feature Groups**, habilita el grupo **Meta Quest**. Es lo que agrega al build lo específico de Horizon OS.
8. Revisa la lista de validación de esa ventana. Los errores traen un botón **Fix** que escribe el ajuste por ti. Más rápido y más confiable que ir a cazarlos uno por uno.

## Parte 3 · El banco

Los números de abajo están medidos para que el banco quede a la altura de un banco. Si los cambias, vuelve a medirlos con el visor puesto.

9. Guarda la escena de la plantilla como `Assets/Scenes/Banco.unity`.
10. Arrastra el prefab **XR Interaction Setup** desde `Assets/Samples/XR Interaction Toolkit/.../Starter Assets/Prefabs` a la jerarquía. Trae el XR Origin con su cámara, las dos manos con sus interactores y el manager que los empareja.
11. **Borra la Main Camera que trajo la plantilla.** La única cámara de la escena debe ser la que cuelga del XR Origin bajo su Camera Offset. Con dos cámaras renderiza la equivocada y la consola se queja de dos audio listeners.
12. Revisa que la escena tenga exactamente un **XR Interaction Manager** y un **Input Action Manager**. El prefab normalmente los trae. Si falta alguno, el manager se agrega con **GameObject > XR > Interaction Manager**, y el otro como componente en un objeto vacío. Sin el Input Action Manager las acciones nunca se habilitan y ningún botón responde, sin una sola línea en la consola.
13. Pon el piso: un **Plane** en el origen, escala `2, 1, 2`, que da veinte por veinte metros. Nómbralo `Piso`.
14. Crea un objeto vacío llamado `Banco` en el origen, con **GameObject > Create Empty**. Todo lo que sigue cuelga de ahí. Un padre vacío en ceros mantiene legibles los números de sus hijos, y en la práctica 2 te va a servir para mover el banco entero sin recalcular nada.
15. La mesa de trabajo: un **Cube** hijo de `Banco`, escala `1.6, 0.05, 0.8`, posición `0, 0.9, 1.2`. La cubierta queda a noventa centímetros del piso, que es la altura de un banco de taller real. Con el visor puesto se nota de inmediato si le erraste.
16. El motor: un **Cube** hijo de `Banco` llamado `Motor`, escala `0.5, 0.4, 0.4`, posición `-0.55, 1.13, 1.2`. Va en el extremo izquierdo de la mesa. Hoy no hace nada; en la práctica 2 es lo que el paro de emergencia apaga.
17. El torquímetro: un **Cube** hijo de `Banco` llamado `Torquimetro`, escala `0.30, 0.03, 0.04`, posición `0.25, 0.94, 1.2`. Treinta centímetros de largo, acostado sobre la cubierta. Es lo único de esta escena que se va a poder levantar.
18. Dales materiales. **Assets > Create > Material** para cada uno, que en este proyecto salen con el shader URP/Lit. Que el torquímetro se distinga del resto de un vistazo. Si reciclas un material de otro proyecto y algo se pinta magenta, ese material es del pipeline integrado, y se arregla en **Window > Rendering > Render Pipeline Converter**.
19. Selecciona el torquímetro y **Add Component > XR Grab Interactable**. Unity le agrega un Rigidbody al mismo tiempo, porque el componente lo exige. Ese Rigidbody es lo que hace que el torquímetro se caiga si lo sueltas fuera de la mesa, y también la razón por la que la mesa necesita su Box Collider, que ya trae por ser un Cube.

## Parte 4 · Dos scripts cortos

20. Crea `DeviceReport.cs` y ponlo en un objeto vacío de la escena:

```csharp
using UnityEngine;

public class DeviceReport : MonoBehaviour
{
    void Start()
    {
        Debug.Log($"os    {Application.platform}");
        Debug.Log($"gfx   {SystemInfo.graphicsDeviceType}");
        Debug.Log($"edit  {Application.isEditor}");
    }
}
```

Que un build termine no dice nada sobre lo que recibió el visor. Estas tres líneas sí. En Play mode vas a leer `WindowsEditor`, `Direct3D11` y `True`; en el visor tienen que leer `Android`, `Vulkan` y `False`. Los dos últimos juntos son la prueba de que lo que estás mirando corrió en el dispositivo y no en la computadora.

21. Crea `WrenchLog.cs` y ponlo en el torquímetro:

```csharp
using UnityEngine;
using UnityEngine.XR.Interaction.Toolkit;

public class WrenchLog : MonoBehaviour
{
    public void Held(SelectEnterEventArgs a)
    {
        Debug.Log($"torquímetro en {a.interactorObject.transform.name}");
    }
}
```

22. Con el torquímetro seleccionado, busca el evento **Select Entered** del XR Grab Interactable en el inspector, presiona el más, arrastra el propio torquímetro a la ranura del objeto y escoge `WrenchLog > Held`. El inspector solo lista métodos públicos que reciben un argumento del tipo del evento, y por eso `Held` está declarado así y no de otra forma. Si el método no aparece en la lista, revisa la firma.

## Parte 5 · Que el visor acepte el build

23. Conecta el visor a la computadora con el cable USB-C.
24. Ponte el visor. Si esa computadora nunca ha compilado a ese visor, va a aparecer un aviso preguntando si permites la depuración USB. Acéptalo y marca **Always allow from this computer**. El aviso es por computadora, así que cada máquina del salón lo pide una vez aunque el visor ya esté en modo desarrollador.
25. En una terminal corre `adb devices`. Tiene que aparecer el visor con la palabra `device` al lado. Si dice `unauthorized`, el aviso del paso 24 sigue esperando adentro del visor y nadie lo ha contestado. Si no aparece nada, revisa el cable antes que cualquier otra cosa.

## Parte 6 · Compilar y probar

26. Abre **File > Build Profiles** y crea un perfil de **Meta Quest**. Ese perfil existe de Unity 6.1 en adelante y llega con los seis valores ya puestos. Si estás en Unity 6.0 no lo vas a encontrar: escoge la plataforma **Android**, presiona **Switch Platform** y captura tú mismo esta tabla en Player Settings.

| Ajuste | Valor |
|---|---|
| Graphics API | Vulkan |
| Scripting Backend | IL2CPP |
| Target Architectures | ARM64 |
| Minimum API Level | Android 10, nivel 29 |
| Target API Level | Android 12L, nivel 32 |
| Stereo Rendering Mode | Single Pass Instanced |

El último renglón merece un párrafo. Un cuadro de VR son dos imágenes, una por ojo. En multi pass el motor recorre la escena dos veces y el CPU paga cada draw call dos veces. En single pass instanced la recorre una vez, con draws instanciados que llenan los dos ojos. Casi todo el ahorro cae del lado del CPU. Por eso viene puesto de fábrica, y no como una optimización que tú tengas que descubrir.

27. Agrega `Banco.unity` a la lista de escenas del perfil. Lo que no está en la lista no existe para el player.
28. Marca **Development Build**. Es lo que te deja leer la consola con `adb logcat`, y en la práctica de perfilado va a hacer falta de todas formas.
29. Presiona **Build And Run** con el visor conectado y despierto. Un visor dormido a media instalación deja el build a medias sin decir por qué, así que tápale el sensor mientras compila.
30. Ponte el visor y pídele a tu compañero que lea `adb logcat` desde la computadora. Recorre esta lista en orden:
    - La app abre en estéreo, con el banco alrededor, no como una ventana plana.
    - El log dice `Android`, `Vulkan` y `False`.
    - Mueves la cabeza y la vista responde de inmediato, sin arrastre.
    - Ves las dos manos y se mueven contigo.
    - Alcanzas el torquímetro, aprietas el gatillo, y se pega a tu mano. El log dice cuál mano fue.
    - Lo sueltas sobre la mesa y se queda. Lo sueltas fuera de la mesa y se cae al piso.
31. Antes de quitarte el visor, contesta las dos preguntas de la sesión 1 y que tu compañero las anote tal cual: ¿la cubierta quedó a la altura que esperabas con las manos? ¿El torquímetro se siente de treinta centímetros? Las dos se contestan solamente ahí adentro.
32. Cámbiense el visor y que tu compañero repita el paso 30 sobre su propio build, con el tuyo leyendo la consola. Sus respuestas al paso 31 casi nunca van a coincidir con las tuyas, y esa diferencia es un dato sobre la escena, no un desacuerdo.

## Si algo sale mal

| Qué ves | Qué significa | Dónde se arregla |
|---|---|---|
| La app abre como ventana plana, sin estéreo | El build salió sin proveedor de XR | OpenXR en la pestaña de **Android**, paso 5 |
| El log dice `WindowsEditor` | Estás leyendo Play mode, no el visor | Paso 29, y conecta el logcat al dispositivo |
| Estéreo bien, pero la cabeza no mueve la vista | Renderiza la cámara equivocada | Borra la Main Camera de la plantilla, paso 11 |
| Las manos se ven y ningún botón responde | Falta el perfil de interacción, o el Input Action Manager | Pasos 6 y 12 |
| La mano atraviesa el torquímetro | Le falta el XR Grab Interactable, o su collider | Paso 19 |
| El torquímetro se levanta y el log no dice nada | El evento del inspector quedó sin método | Paso 22 |
| `Held` no aparece en la lista del evento | El método no es público, o su argumento no es del tipo del evento | Paso 21 |
| Algo se pinta magenta | Material del pipeline integrado | Render Pipeline Converter, paso 18 |
| `adb devices` dice `unauthorized` | El aviso sigue esperando dentro del visor | Paso 24 |
| `adb devices` no lista nada | Cable de carga, o el visor no está en modo desarrollador | Paso 25, y el apéndice |
| `INSTALL_FAILED_UPDATE_INCOMPATIBLE` | Ya hay un build con ese package name y otra firma | Desinstala esa app desde el visor y recompila |

## Entregable

Un video corto de la pantalla del visor con las seis pruebas del paso 30, en ese orden, las tres líneas del log pegadas como texto, y tus dos respuestas del paso 31. El cuadro que más pesa en la revisión es el último de la lista: soltar el torquímetro fuera de la mesa y verlo caer es lo que demuestra que hay un Rigidbody de verdad y no un objeto pegado a la mano.

## Apéndice · Poner un visor en modo desarrollador

Los visores del salón ya están así. Esto es para quien vaya a preparar uno de cero, o para quien tenga el suyo.

Primero, la cuenta de Meta tiene que pertenecer a un equipo de desarrollador, y eso se crea en el dashboard de Meta, no en el visor. Es el paso que tarda, y sin él el interruptor de modo desarrollador ni siquiera aparece.

Ya con eso, en la app **Meta Horizon** del teléfono: toca el ícono del visor en la barra de herramientas, luego el visor emparejado, luego **Headset Settings**, luego **Developer Mode**, y préndelo. De ahí en adelante cada computadora nueva pide su propia autorización de depuración USB, que es el paso 24 de esta guía.
