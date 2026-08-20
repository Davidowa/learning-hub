# Práctica 1 · Un cubo sobre una imagen impresa

La primera práctica guiada de rastreo de imágenes. Parte de un proyecto vacío de Unity 6 y termina en una app que abre mostrando el cuarto por la cámara, sin nada encima, y que dibuja un cubo sobre una hoja impresa en cuanto la cámara la reconoce. Cuando la hoja sale del cuadro, el cubo se esconde.

La guía está armada para evitar las dos fallas que más aparecen en esta práctica. La primera es compilar y recibir una pantalla de un solo color, amarillo, gris o el que traiga el Background de la cámara, con el cubo flotando sobre un fondo plano en vez del cuarto. Eso no es un error de rastreo: es que nadie está dibujando la imagen de la cámara, y se arregla en un asset de URP antes de compilar. La segunda es que el cubo se vea desde el arranque, sin que la app haya reconocido nada. Eso pasa cuando el cubo vive en la escena en lugar de vivir en un prefab que el manager instancia al detectar. Aquí el cubo nunca toca la jerarquía de la escena final.

## Lo que necesitas antes de empezar

- Unity 6 instalado con el módulo **Android Build Support**, incluidos SDK, NDK y OpenJDK.
- Un teléfono Android con ARCore, depuración USB prendida y un cable que lleve datos.
- Una imagen con buen contraste y detalle, impresa en papel mate. Una portada de revista o un cartel con texto y figuras funcionan bien. Un logotipo con tres trazos sobre fondo blanco no.
- Una regla. Va en serio: el paso 12 la necesita.

## Parte 1 · El proyecto y la escena

1. Crea un proyecto nuevo de Unity 6 con la plantilla **Universal 3D**, para que URP ya venga configurado. Un proyecto existente con esa plantilla también sirve.
2. Abre **Window > Package Manager**, entra a Unity Registry e instala **AR Foundation** y **Google ARCore XR Plugin**, los dos en la misma versión. El segundo jala XR Plug-in Management por su cuenta.
3. Abre **Edit > Project Settings > XR Plug-in Management**, entra a la pestaña de Android y marca **ARCore** en Plug-in Providers.
4. Arma la escena con sus dos GameObjects obligatorios: **GameObject > XR > AR Session** y **GameObject > XR > XR Origin (Mobile AR)**. Sin cualquiera de los dos, la app abre y AR calladamente no corre.
5. Borra la Main Camera que trajo la plantilla. La única cámara de la escena debe ser la que el XR Origin carga bajo su Camera Offset. Con dos cámaras en la escena renderiza la equivocada y la consola se llena de avisos de audio listeners.
6. Agrega el renderer feature que dibuja la imagen de la cámara. Abre **Project Settings > Graphics**, entra al asset de URP al que apunta, busca su Renderer List y abre el **Universal Renderer**. Presiona **Add Renderer Feature** y escoge **AR Background Renderer Feature**.
7. Repite la revisión en la pestaña **Quality**. Cada nivel de calidad puede apuntar a un asset de URP distinto, y la plantilla Universal 3D trae varios. Si el nivel activo en Android apunta a un asset cuyo renderer no tiene el feature, el teléfono compila con la lista que sí revisaste y renderiza con la que no. El síntoma es la pantalla de un color, y la consola no dice una palabra.

Ese renderer feature es la diferencia entre ver el cuarto y ver una pared de color con un cubo flotando. El componente AR Camera Background no dibuja la imagen por sí mismo: le pasa el trabajo a esa lista, y si la lista está vacía, lo que llena la pantalla es el Background de la cámara.

## Parte 2 · El blanco y su biblioteca

8. Importa la imagen del blanco al proyecto. Arrástrala a una carpeta del Project, por ejemplo `Assets/Blancos`. Unity la importa como textura y así la necesita la biblioteca.
9. Imprime la imagen en papel mate. El papel brillante devuelve el reflejo del cuarto y el rastreador no logra empatar la imagen.
10. Crea la biblioteca: **Assets > Create > XR > Reference Image Library**. Nómbrala `BibliotecaBlancos`.
11. Selecciona la biblioteca, presiona **Add Image**, arrastra la textura a la entrada y ponle de nombre `blanco`.
12. Mide con la regla el ancho de la hoja que salió de la impresora. El número que importa es el del papel, no el que sugiere el archivo. Una hoja carta completa mide 0.216 m de ancho y una A4 mide 0.210 m; si imprimiste a otra escala, mide la tuya.
13. Marca **Specify Size** en la entrada y captura ese ancho en metros. Al escribir el ancho, el alto se ajusta solo con la proporción de la imagen.

Si capturas el doble del ancho real, el contenido se dibuja como al doble de distancia y al doble de tamaño. El rastreador no puede medir tu papel: le cree a la biblioteca y deriva la distancia del ancho aparente. Este número mal capturado es la razón por la que un cubo flota sobre la mesa o se hunde en ella con el rastreo funcionando perfectamente.

## Parte 3 · El manager y el prefab

14. Selecciona el **XR Origin** y agrégale el componente **AR Tracked Image Manager** con Add Component.
15. Arrastra `BibliotecaBlancos` al campo **Serialized Library** del manager, y deja **Max Number Of Moving Images** en 1. Rastrear imágenes en movimiento cuesta CPU, y esta práctica solo usa una.
16. Crea la raíz del prefab: **GameObject > Create Empty**, nómbrala `ContenidoBlanco` y déjale el transform en ceros con el botón Reset del componente. Cualquier posición guardada en la raíz se vuelve un desplazamiento respecto a la hoja.
17. Créale un hijo con **GameObject > 3D Object > Cube**. Al cubo ponle escala `0.05, 0.05, 0.05` y posición `0, 0.025, 0`, para que un cubo de cinco centímetros descanse sobre el papel en lugar de atravesarlo. El manager coloca la raíz del prefab en el centro de la imagen, con el eje Y saliendo de la hoja.
18. Dale color al cubo. Crea un material con **Assets > Create > Material**, que en este proyecto sale con el shader URP/Lit, escoge un color y arrástralo al cubo. Si en vez de crear uno reciclas un material de otro proyecto y el cubo se pinta magenta, ese material es del pipeline built-in; conviértelo desde **Window > Rendering > Render Pipeline Converter**.
19. Arrastra `ContenidoBlanco` de la jerarquía a la carpeta del Project para volverlo prefab, y **bórralo de la escena**. Este paso es el que decide si el cubo aparece desde el arranque o solo al detectar. En la jerarquía de la escena no queda ningún cubo; el único cubo del proyecto vive en el asset del prefab.
20. Arrastra el prefab al campo **Tracked Image Prefab** del manager. Cuando la sesión reconozca la imagen, el manager instancia el prefab, le agrega el componente ARTrackedImage y mantiene su pose siguiendo a la hoja.

## Parte 4 · Esconderlo cuando la hoja se va

Hay un detalle que el manager no resuelve solo. Cuando la hoja sale del cuadro, el GameObject instanciado no se destruye: se queda donde la vio por última vez, con su estado de rastreo degradado. Sin este paso, el cubo queda flotando en el aire apuntando a una mesa que ya no está en pantalla. La documentación lo dice sin rodeos: no hay API para saber si una imagen es visible, pero el estado de rastreo lo delata.

21. Crea el script `TrackedImageVisibility.cs` y pégale esto:

```csharp
using UnityEngine;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;

public class TrackedImageVisibility : MonoBehaviour
{
    [SerializeField] ARTrackedImageManager images;

    void OnEnable() => images.trackablesChanged.AddListener(OnChanged);
    void OnDisable() => images.trackablesChanged.RemoveListener(OnChanged);

    void OnChanged(ARTrackablesChangedEventArgs<ARTrackedImage> e)
    {
        foreach (var img in e.added) Apply(img);
        foreach (var img in e.updated) Apply(img);
    }

    static void Apply(ARTrackedImage img)
    {
        bool visible = img.trackingState == TrackingState.Tracking;
        foreach (var r in img.GetComponentsInChildren<Renderer>())
            r.enabled = visible;
    }
}
```

Línea por línea:

- `using UnityEngine;` trae la base de todo componente: `MonoBehaviour`, `SerializeField` y el tipo `Renderer`.
- `using UnityEngine.XR.ARFoundation;` trae el manager y los tipos del evento: `ARTrackedImageManager`, `ARTrackedImage` y `ARTrackablesChangedEventArgs`.
- `using UnityEngine.XR.ARSubsystems;` trae `TrackingState`. Vive en un namespace aparte porque describe lo que reporta el proveedor, no a los managers.
- `public class TrackedImageVisibility : MonoBehaviour` declara el script como componente, que es lo que permite colgarlo del XR Origin en el paso 22.
- `[SerializeField] ARTrackedImageManager images;` es un campo privado que el Inspector sí muestra. Ahí cae el manager cuando lo arrastras; el script nunca lo anda buscando por código.
- `void OnEnable() => images.trackablesChanged.AddListener(OnChanged);` se suscribe al evento del manager cuando el componente prende. `trackablesChanged` es un UnityEvent, y por eso se escucha con `AddListener`.
- `void OnDisable() => images.trackablesChanged.RemoveListener(OnChanged);` se da de baja cuando el componente se apaga. Sin esta línea, un componente que se apaga y se vuelve a prender queda suscrito dos veces y el handler corre doble.
- `void OnChanged(ARTrackablesChangedEventArgs<ARTrackedImage> e)` es el handler. El argumento `e` carga tres listas en una sola llamada: added, updated y removed.
- `foreach (var img in e.added) Apply(img);` recorre las imágenes que la sesión acaba de reconocer. Por aquí entra la hoja la primera vez que la cámara la ve.
- `foreach (var img in e.updated) Apply(img);` recorre las que cambiaron de pose o de estado. Esta lista llega casi cada frame mientras la hoja esté en el cuadro, y también cuando sale, que es el momento que a esta práctica le importa.
- `static void Apply(ARTrackedImage img)` decide la visibilidad de una imagen. Es `static` porque no toca ningún campo del componente, solo trabaja con lo que recibe.
- `bool visible = img.trackingState == TrackingState.Tracking;` es la decisión completa del script. `Tracking` significa que el proveedor está viendo la hoja en este momento; `Limited` significa que la recuerda pero ya no la ve bien, que es justo lo que reporta cuando la hoja sale del cuadro. Solo el primer caso enciende el cubo.
- `foreach (var r in img.GetComponentsInChildren<Renderer>())` junta todos los renderers colgados del prefab instanciado, que aquí es el MeshRenderer del cubo. Si un día el prefab carga tres figuras, las tres entran sin cambiar el script.
- `r.enabled = visible;` prende o apaga solo el dibujo. El GameObject sigue vivo y su transform sigue al blanco, así que el cubo reaparece en su lugar en cuanto la cámara regresa a la hoja.

22. Agrega el script al XR Origin y arrastra el AR Tracked Image Manager a su campo `images`. Un campo vacío falla en silencio en el teléfono, donde no puedes ver el nulo, así que revísalo dos veces.

## Parte 5 · Compilar y probar

23. Abre **Project Settings > XR Plug-in Management > Project Validation** en la pestaña de Android y presiona los botones **Fix** que aparezcan. Los seis ajustes deben quedar así:

| Ajuste | Valor |
|---|---|
| Minimum API Level | Android 7.0, nivel 24 |
| Scripting Backend | IL2CPP |
| Target Architectures | ARM64 |
| Auto Graphics API | Apagado |
| Graphics APIs | OpenGLES3, sin Vulkan |
| ARCore Requirement | Required |

Required deja la app fuera de los teléfonos sin ARCore, y a cambio te deja dar por hecho que AR existe. Para esta práctica es lo que conviene.

24. Abre **File > Build Profiles**, escoge Android, presiona **Switch Platform** si la plataforma activa era otra, y luego **Build And Run** con el teléfono conectado y despierto.
25. Recorre esta lista en orden:
    - La app abre mostrando el cuarto. Nada de pantalla de un color, nada de cubo.
    - Apuntas a la hoja impresa y el cubo aparece parado sobre ella, del tamaño de una goma de borrar.
    - Alejas la cámara de la hoja y el cubo desaparece. Regresas y reaparece en su lugar.
    - Mueves la hoja despacio y el cubo la sigue.

## Si algo sale mal

| Qué ves | Qué significa | Dónde se arregla |
|---|---|---|
| Un solo color de fondo (amarillo, gris, el que sea), con o sin cubo | Nadie dibuja la imagen de la cámara | AR Background Renderer Feature, en el renderer del asset de URP activo, pasos 6 y 7 |
| El cubo visible desde el arranque | Quedó una copia del prefab en la escena | Bórrala de la jerarquía; el cubo solo vive en el asset, paso 19 |
| Cubo magenta | Material del pipeline built-in | Render Pipeline Converter, paso 18 |
| Pantalla negra | Permiso de cámara negado | Ajustes de la app en el teléfono |
| El cubo se queda flotando al quitar la hoja | El script no está o su campo quedó vacío | Pasos 21 y 22 |
| Nunca detecta la hoja | Blanco con poco detalle, papel brillante, o el tamaño capturado no es el impreso | Pasos 9, 12 y 13 |
| El cubo flota sobre la mesa o se hunde | El ancho capturado no es el que mide la regla | Pasos 12 y 13 |

## Entregable

Un video corto de la pantalla del teléfono que muestre las cuatro pruebas del paso 25, en ese orden. El arranque limpio cuenta tanto como la detección: un video que empieza con el cubo ya visible reprueba el primer punto.
