# Práctica 2 · Dos imágenes, un cubo y una esfera

La segunda práctica de rastreo de imágenes. Parte del proyecto terminado de la práctica 1 y le enseña a distinguir: una hoja impresa produce un cubo y otra hoja distinta produce una esfera, cada figura sobre su propio papel, cada una visible solo mientras la cámara ve su hoja.

El cambio de fondo está en quién instancia el contenido, no en la segunda hoja. El campo Tracked Image Prefab del manager es uno solo, así que sirve cuando toda imagen produce lo mismo y se queda corto en cuanto dos imágenes producen cosas distintas. En esta práctica ese campo se queda vacío y un script decide qué prefab corresponde a cada imagen. Puede hacerlo porque toda imagen rastreada sabe con qué entrada de la biblioteca empató, y el nombre de esa entrada viaja en `referenceImage.name`.

## Lo que necesitas antes de empezar

- El proyecto de la práctica 1 compilando y pasando sus cuatro pruebas. Si el cubo de la práctica 1 no aparece o la pantalla sale de un color, arregla eso primero; esta guía no repite esos pasos.
- Una segunda imagen impresa, con tanto contraste y detalle como la primera y que no se le parezca. Dos carteles de la misma serie o dos páginas del mismo folleto se parecen demasiado entre sí, y el rastreador puede confundirlas o tardar en decidirse.
- La regla otra vez. La segunda hoja también se mide.

## Parte 1 · La segunda entrada de la biblioteca

1. Importa la segunda imagen al proyecto, a la misma carpeta `Assets/Blancos`.
2. Abre `BibliotecaBlancos` y renombra la entrada existente a `cubo`. El nombre deja de ser decorativo en esta práctica: el script lo compara letra por letra.
3. Agrega la segunda entrada con **Add Image**, arrastra la segunda textura y nómbrala `esfera`. Minúsculas, sin espacios, igual que la primera.
4. Mide con la regla el ancho de la segunda hoja impresa, marca **Specify Size** en la entrada nueva y captura ese ancho en metros. Cada entrada carga su propia medida; que la primera esté bien medida no salva a la segunda.

## Parte 2 · El segundo prefab

5. Duplica la estructura del prefab de la práctica 1 pero con una esfera. Crea un GameObject vacío `ContenidoEsfera` con el transform en ceros, créale un hijo con **GameObject > 3D Object > Sphere**, escala `0.05, 0.05, 0.05`, posición `0, 0.025, 0`, para que la esfera descanse sobre el papel. La raíz en ceros importa más aquí que en la práctica 1: el script de esta guía instancia el prefab como hijo del transform de la imagen, y cualquier posición guardada en la raíz se vuelve un desplazamiento respecto a la hoja.
6. Crea un segundo material URP/Lit con otro color y asígnalo a la esfera. Que las dos figuras se distingan de un vistazo en el video: si el cubo es rojo, la esfera no.
7. Vuelve `ContenidoEsfera` prefab arrastrándolo al Project y bórralo de la escena, exactamente como en la práctica 1. En la jerarquía no queda ni cubo ni esfera.
8. Renombra el prefab de la práctica 1 a `ContenidoCubo` si todavía se llama `ContenidoBlanco`, para que en el Inspector se lea qué es cada cosa.

## Parte 3 · El script que reparte

9. Selecciona el XR Origin y **vacía el campo Tracked Image Prefab** del AR Tracked Image Manager. Si ese campo conserva el cubo, el manager instancia un cubo por cada imagen detectada, incluida la de la esfera, y vas a ver dos cubos y ninguna esfera. Este es el error más común de la práctica.
10. Sube **Max Number Of Moving Images** a 2, para que las dos hojas puedan rastrearse a la vez sobre la mesa.
11. Quita el componente `TrackedImageVisibility` del XR Origin. Su trabajo se muda al script nuevo, que necesita saber qué instanció para poder esconderlo.
12. Crea el script `PrefabPerImage.cs`:

```csharp
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;

public class PrefabPerImage : MonoBehaviour
{
    [SerializeField] ARTrackedImageManager images;
    [SerializeField] GameObject cubePrefab;
    [SerializeField] GameObject spherePrefab;

    readonly Dictionary<TrackableId, GameObject> spawned = new();

    void OnEnable() => images.trackablesChanged.AddListener(OnChanged);
    void OnDisable() => images.trackablesChanged.RemoveListener(OnChanged);

    void OnChanged(ARTrackablesChangedEventArgs<ARTrackedImage> e)
    {
        foreach (var img in e.added)
        {
            GameObject prefab =
                img.referenceImage.name == "cubo" ? cubePrefab : spherePrefab;
            spawned[img.trackableId] = Instantiate(prefab, img.transform);
            Apply(img);
        }

        foreach (var img in e.updated) Apply(img);

        foreach (var pair in e.removed)
            if (spawned.Remove(pair.Key, out var go)) Destroy(go);
    }

    void Apply(ARTrackedImage img)
    {
        if (spawned.TryGetValue(img.trackableId, out var go))
            go.SetActive(img.trackingState == TrackingState.Tracking);
    }
}
```

Línea por línea, saltando lo que ya explicó la práctica 1:

- `using System.Collections.Generic;` trae `Dictionary`, que el script de la práctica 1 no necesitaba.
- Los otros tres `using` son los de la práctica 1, con un tipo más en juego: `TrackableId` también vive en ARSubsystems.
- La declaración de la clase y el campo `images` del manager repiten los de la práctica 1 sin cambio.
- `[SerializeField] GameObject cubePrefab;` y `spherePrefab` son los dos campos donde caen los prefabs en el paso 13. El script no sabe qué figura carga cada uno; solo sabe cuál corresponde a qué nombre.
- `readonly Dictionary<TrackableId, GameObject> spawned = new();` es el registro de lo instanciado: por cada imagen reconocida, la figura que se le creó. El `readonly` impide reasignar el diccionario; su contenido sí cambia todo el tiempo.
- `OnEnable` y `OnDisable` se suscriben y se dan de baja del mismo `trackablesChanged` de la práctica 1, con las mismas razones.
- `foreach (var img in e.added)` corre una vez por imagen recién reconocida. Todo lo que sigue dentro del bloque decide y crea.
- `GameObject prefab = img.referenceImage.name == "cubo" ? cubePrefab : spherePrefab;` es el reparto completo. Compara el nombre de la entrada de la biblioteca con la que empató la imagen, literal, letra por letra, y todo lo que no se llame `cubo` recibe esfera. Por eso los nombres de los pasos 2 y 3 no son decorativos.
- `spawned[img.trackableId] = Instantiate(prefab, img.transform);` hace dos cosas. `Instantiate` clona el prefab como hijo del transform de la imagen, así que hereda su pose sin más código. Y la instancia queda guardada bajo el `trackableId`, el identificador que no cambia mientras la sesión siga reconociendo la hoja, que es lo que permite encontrarla después.
- `Apply(img);` fija la visibilidad inicial de la figura recién creada, por si la imagen ya llegó con estado degradado.
- `foreach (var img in e.updated) Apply(img);` revisa la visibilidad en cada cambio de pose o de estado, igual que en la práctica 1.
- `foreach (var pair in e.removed)` recorre las imágenes que la sesión dejó de reconocer. Llegan como pares de identificador e imagen, no como una lista simple de imágenes.
- `if (spawned.Remove(pair.Key, out var go)) Destroy(go);` saca la entrada del diccionario y, si existía, destruye la figura huérfana. Con imágenes casi nunca pasa, pero cuando pasa, nada se queda flotando.
- `void Apply(ARTrackedImage img)` ya no es `static` como en la práctica 1, porque necesita leer el diccionario del componente.
- `if (spawned.TryGetValue(img.trackableId, out var go))` busca la figura registrada para esa imagen. Si no hay registro, no hace nada, sin tronar.
- `go.SetActive(img.trackingState == TrackingState.Tracking);` prende o apaga el GameObject completo con el mismo criterio de la práctica 1: visible solo mientras el proveedor está viendo la hoja. Aquí es `SetActive` en vez de apagar renderers porque este script es dueño de la instancia y puede apagarla entera.

13. Agrega `PrefabPerImage` al XR Origin y llena sus tres campos: el manager, `ContenidoCubo` en `cubePrefab` y `ContenidoEsfera` en `spherePrefab`. Tres campos son tres oportunidades de dejar un nulo que solo truena en el teléfono.

## Parte 4 · Compilar y probar

14. Compila con **Build And Run**; los ajustes de Android no cambiaron desde la práctica 1. Si Project Validation marca algo nuevo, presiona **Fix** antes.
15. Pon las dos hojas sobre la mesa, separadas, y recorre esta lista:
    - La app abre mostrando el cuarto, sin figura alguna.
    - Apuntas a la hoja `cubo` y aparece el cubo sobre ella. Solo el cubo.
    - Apuntas a la hoja `esfera` y aparece la esfera sobre ella. Solo la esfera.
    - Encuadras las dos hojas a la vez y cada figura está parada sobre la suya.
    - Sacas una hoja del cuadro y su figura se esconde; la otra sigue donde estaba.

## Si algo sale mal

Las fallas de pantalla de la práctica 1 aplican igual aquí y se arreglan en el mismo lugar. Estas son las nuevas:

| Qué ves | Qué significa | Dónde se arregla |
|---|---|---|
| Dos cubos y ninguna esfera | Tracked Image Prefab sigue asignado en el manager | Vacíalo, paso 9 |
| Las dos hojas producen esfera | El nombre en la biblioteca no es exactamente `cubo` | La comparación es literal; revisa mayúsculas y espacios, pasos 2 y 3 |
| Figuras intercambiadas | Los prefabs quedaron cruzados en el Inspector | Paso 13 |
| Solo se rastrea una hoja a la vez | Max Number Of Moving Images sigue en 1 | Paso 10 |
| Una figura del tamaño equivocado | La segunda hoja no se midió, o se capturó la medida de la primera | Paso 4 |
| Nada aparece en ninguna hoja | El script no está en el XR Origin o el campo del manager quedó vacío | Paso 13 |
| El rastreador confunde las hojas | Los dos blancos se parecen demasiado | Escoge una segunda imagen distinta e imprime de nuevo |

## Entregable

Un video corto de la pantalla del teléfono con las cinco pruebas del paso 15, en ese orden. El cuadro que más pesa en la revisión es el de las dos hojas a la vez, con cada figura sobre la suya, porque es el único que demuestra que el reparto por nombre funciona.
