# Práctica 1 · AR · Un cubo sobre una imagen

Esta práctica crea una aplicación de realidad aumentada (AR) que reconoce una imagen y muestra un cubo de 5 cm sobre ella. La cámara muestra el entorno real desde el arranque. El contenido se crea después de reconocer la imagen y se oculta cuando su estado de rastreo deja de ser Tracking.

La guía usa Unity 6.3 LTS, la plantilla Universal 3D y Android con ARCore. AR Foundation y Google ARCore XR Plugin se fijan en 6.3.5. El contenido sigue a la imagen durante la sesión; esta práctica no guarda objetos para otra ejecución.

## Alcance de la experiencia

El estado Tracking describe la calidad del rastreo. No certifica que la imagen esté visible en cada instante. ARCore puede conservar una pose estimada cuando la imagen sale del cuadro; por eso no se promete una desaparición inmediata al apartar la cámara. La regla del script es mostrar el contenido en Tracking y ocultarlo en Limited o None.

La imagen puede estar impresa o mostrarse en otra pantalla. En ambos casos debe ser plana y conservar el ancho físico registrado en la biblioteca. Los reflejos, el desenfoque y las imágenes con pocos detalles dificultan su reconocimiento.

## Antes de empezar

- Instala Unity 6.3 LTS con Android Build Support, Android SDK & NDK Tools y OpenJDK desde Unity Hub.
- Usa un celular Android compatible con ARCore, con Google Play Services for AR actualizado. Activa la depuración USB y conecta un cable que transfiera datos.
- Elige una imagen con detalles distribuidos y contraste. Prepara una regla y una impresión o una segunda pantalla donde mostrarla.
- Conserva una copia del proyecto antes de modificar una práctica anterior. Los nombres de menús de esta guía corresponden al Editor en inglés.

## Parte 1: Preparar el proyecto y Android

1. Crea un proyecto con Unity 6.3 LTS y la plantilla Universal 3D. Nómbralo Practica1AR y espera a que termine la importación.
2. Abre Window > Package Manager. En Unity Registry instala AR Foundation y Google ARCore XR Plugin, ambos en 6.3.5. Si la versión no aparece en la lista inicial, usa Install package by name con los identificadores `com.unity.xr.arfoundation` y `com.unity.xr.arcore`, y escribe la versión 6.3.5.
3. Abre File > Build Profiles, agrega o selecciona Android y presiona Switch Platform. Si falta el módulo, instálalo desde Unity Hub antes de continuar.
4. Abre Edit > Project Settings > Player > Android > Other Settings. Usa Input System Package (New) o Both en Active Input Handling. Acepta el reinicio del Editor si lo solicita.
5. En Project Settings > XR Plug-in Management > Android, activa ARCore y verifica Initialize XR on Startup. En los ajustes de ARCore, deja Requirement en Required y Depth en Optional.
6. En Player > Android > Other Settings, configura IL2CPP y ARM64. Desactiva Auto Graphics API y deja OpenGLES3 como única API para esta práctica. Usa Android 7.0 (API 24) como mínimo, o el nivel mayor que exija Project Validation para tu configuración.

OpenGLES3 es la ruta elegida para este ejercicio. ARCore 6.3 también permite Vulkan, que requiere configuración adicional en URP. No agregues esa variante mientras verificas la primera aplicación.

## Parte 2: Configurar la escena y el fondo de cámara

7. Guarda la escena como `Assets/Scenes/Practica1AR.unity`. En la jerarquía crea XR > AR Session y XR > XR Origin (Mobile AR). Elimina la Main Camera original de la plantilla y conserva la cámara que está dentro del XR Origin.
8. Revisa la cámara del XR Origin. Debe tener Camera, AR Camera Manager, AR Camera Background y el componente de seguimiento Tracked Pose Driver (Input System). El XR Origin debe tener esa cámara asignada y escala `1, 1, 1`. Conserva la luz direccional para iluminar el cubo.
9. En Project Settings > Quality, identifica el nivel predeterminado de Android y su Render Pipeline Asset. Si ese campo está vacío, revisa Default Render Pipeline en Project Settings > Graphics. Los nombres de los assets dependen de la plantilla; no tienen que llamarse Mobile_RPAsset o PC_RPAsset.
10. Abre cada URP Asset que pueda usar Android y revisa su Renderer List. En los Universal Renderer correspondientes, usa Add Renderer Feature para agregar AR Background Renderer Feature. Configura también los renderers del Editor si vas a probar con XR Simulation.
11. En la cámara AR, revisa que el Renderer seleccionado corresponda a uno de los renderers configurados. Si usarás XR Simulation, deja Depth Priming Mode en Disabled en ese renderer. Conserva la configuración de Render Graph de Unity 6.3.

AR Camera Background y el renderer activo trabajan juntos para dibujar la cámara. Si falta el feature en el renderer que usa Android, puede aparecer un fondo de color. Ese síntoma también requiere revisar permisos, la sesión AR y los mensajes de la consola; no identifica una sola causa por sí mismo.

## Parte 3: Registrar la imagen y crear el cubo

12. Importa la imagen en `Assets/Blancos`. Muestra la impresión o la imagen en la segunda pantalla con el tamaño que usarás durante la prueba. Evita reflejos y cambios de zoom.
13. Crea Assets > Create > XR > Reference Image Library y nómbrala BibliotecaBlancos. Presiona Add Image, asigna la textura y escribe `cubo` en Name, con minúsculas y sin espacios.
14. Mide el ancho del dibujo que se mostrará a la cámara, sin incluir márgenes ajenos a la textura. Activa Specify Size y escribe ese ancho en metros. Por ejemplo, 15 cm son 0.15 m. Si cambias el tamaño mostrado o la impresión, vuelve a medir.
15. Agrega AR Tracked Image Manager al XR Origin. Asigna BibliotecaBlancos en Serialized Library, solicita 1 en Max Number Of Moving Images y deja Tracked Image Prefab vacío. Ese campo personaliza los objetos del rastreador; el script creará el contenido por separado.
16. Crea un GameObject vacío llamado ContenidoCubo. Usa Reset para dejar posición y rotación en cero y escala en uno. Agrega un Cube como hijo, con posición local `0, 0.025, 0`, rotación local cero y escala `0.05, 0.05, 0.05`.
17. Crea un material, selecciona el shader Universal Render Pipeline/Lit y elige un color. Asígnalo al cubo. El eje Y local sale del plano de la imagen; el desplazamiento de 0.025 m apoya el cubo sobre ella.
18. Arrastra ContenidoCubo a `Assets/Prefabs` para crear el prefab y elimina la copia de la escena. En la jerarquía final no debe quedar ningún cubo de prueba.

## Parte 4: Crear el contenido desde el rastreo

19. Crea `Assets/Scripts/ImageContentController.cs` y sustituye todo su contenido con el código siguiente. El nombre del archivo debe coincidir con el de la clase. Espera a que Unity termine de compilar y revisa la consola.

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;

public sealed class ImageContentController : MonoBehaviour
{
    [Serializable]
    public sealed class ImageBinding
    {
        public string imageName;
        public GameObject prefab;
    }

    [SerializeField] ARTrackedImageManager images;
    [SerializeField] ImageBinding[] bindings;
    readonly Dictionary<TrackableId, GameObject> spawned = new();

    void OnEnable()
    {
        if (images == null || bindings == null || bindings.Length == 0)
        {
            Debug.LogError("Asigna Images y al menos una entrada en Bindings.", this);
            enabled = false;
            return;
        }
        images.trackablesChanged.AddListener(OnChanged);
        foreach (var image in images.trackables) Apply(image);
    }

    void OnDisable()
    {
        if (images != null)
            images.trackablesChanged.RemoveListener(OnChanged);
        foreach (var content in spawned.Values)
            if (content != null) Destroy(content);
        spawned.Clear();
    }

    void OnChanged(ARTrackablesChangedEventArgs<ARTrackedImage> changes)
    {
        foreach (var image in changes.added) Apply(image);
        foreach (var image in changes.updated) Apply(image);
        foreach (var pair in changes.removed)
        {
            if (!spawned.TryGetValue(pair.Key, out var content)) continue;
            if (content != null) Destroy(content);
            spawned.Remove(pair.Key);
        }
    }

    GameObject FindPrefab(string imageName)
    {
        foreach (var binding in bindings)
        {
            if (binding != null && binding.imageName == imageName)
                return binding.prefab;
        }
        return null;
    }

    void Apply(ARTrackedImage image)
    {
        if (image == null) return;
        bool tracked = image.trackingState == TrackingState.Tracking;
        if (!spawned.TryGetValue(image.trackableId, out var content)
            || content == null)
        {
            if (!tracked) return;
            var prefab = FindPrefab(image.referenceImage.name);
            if (prefab == null) return;
            content = Instantiate(prefab, image.transform, false);
            content.transform.localPosition = Vector3.zero;
            content.transform.localRotation = Quaternion.identity;
            content.transform.localScale = Vector3.one;
            spawned[image.trackableId] = content;
        }
        content.SetActive(tracked);
    }
}
```

20. Agrega ImageContentController al XR Origin. En Images arrastra el AR Tracked Image Manager de ese mismo objeto.
21. En Bindings, crea una entrada. Escribe `cubo` en Image Name y arrastra el asset ContenidoCubo desde Project a Prefab. Deja un solo controlador activo; si vienes de una versión anterior, quita TrackedImageVisibility o PrefabPerImage de la escena.
22. Confirma que Tracked Image Prefab siga vacío y guarda la escena. Mantén en la jerarquía AR Session, XR Origin y la luz, sin copias manuales del contenido.

## Cómo se organiza el código

Bindings relaciona el nombre de una entrada de la biblioteca con un prefab. La comparación distingue mayúsculas y espacios. Un nombre sin coincidencia no genera contenido; tampoco recibe una esfera por defecto.

El evento trackablesChanged informa imágenes agregadas, actualizadas y retiradas. Apply crea una sola instancia por TrackableId cuando el rastreo está en Tracking. La instancia queda como hija de la imagen y hereda su pose. Su raíz se restablece a posición cero, rotación identidad y escala uno; el tamaño permanece en el hijo Cube.

Cuando el estado cambia, SetActive controla únicamente el contenido creado. El objeto ARTrackedImage permanece activo para que el proveedor pueda seguir actualizándolo. Al retirar una imagen se elimina su contenido. Al desactivar el controlador se retira la suscripción y se limpian sus instancias; al reactivarlo se revisan las imágenes que el manager ya conoce.

## Parte 5: Compilar y probar en el celular

23. Abre Project Settings > XR Plug-in Management > Project Validation y selecciona Android. Corrige los errores y revisa las advertencias. Usa Fix cuando corresponda; no actives Ignore build errors para omitir problemas pendientes.
24. En Build Profiles, confirma Android y agrega Practica1AR.unity con Add Open Scenes en Scene List. Deja esta como única escena habilitada. Si usas un perfil con lista propia, puedes mostrarla con Add Settings > Scene List; sin esa lista, se usa la lista global. Conecta el celular y presiona Build And Run.
25. Abre la aplicación y concede el permiso de cámara. Comprueba que se vea el entorno real y que todavía no aparezca el cubo.
26. Apunta a la imagen, mantenla enfocada y ocupa con ella una parte amplia del cuadro. Debe aparecer un cubo de 5 cm apoyado en su centro. Cambia el ángulo despacio y revisa que siga la orientación de la imagen.
27. Aparta la cámara o cubre la imagen para degradar el rastreo. Cuando el proveedor reporte Limited o None, el contenido debe ocultarse. Regresa a la imagen y comprueba que reaparezca sin duplicarse. Si el proveedor conserva Tracking fuera del cuadro, registra ese comportamiento en el video.
28. Cierra la aplicación y vuelve a abrirla. Debe comenzar sin contenido y reconocer de nuevo la imagen. La prueba en Play Mode, sin configurar XR Simulation, no sustituye la revisión en el celular.

## Si algo sale mal

- Si aparece un fondo de color o negro, revisa el permiso de cámara, AR Session, AR Camera Background y el feature del renderer activo. Consulta también los errores del dispositivo.
- Si el cubo aparece antes de reconocer la imagen, busca una copia en la jerarquía y elimínala. El prefab debe estar solo en Project hasta que se ejecute el controlador.
- Si el material aparece magenta, revisa que use Universal Render Pipeline/Lit. Un material Built-in necesita conversión o un material nuevo compatible con URP.
- Si no aparece contenido, revisa Images, Bindings, el prefab y el nombre `cubo`. Verifica que la biblioteca esté asignada y que el tamaño físico corresponda al mostrado.
- Si el cubo tiene una posición o escala incorrecta, revisa el ancho registrado, la escala del XR Origin y los transforms del prefab. La escala del hijo define los 5 cm.
- Si aparecen duplicados, conserva un solo ImageContentController y deja Tracked Image Prefab vacío. Revisa que no siga activo un script de la versión anterior.

## Entregable y validación

Graba un video que muestre el arranque, la detección, un cambio de ángulo y la recuperación del rastreo. Incluye el Inspector con la biblioteca, la medida física y la entrada de Bindings, además de una consola sin errores. Conserva el proyecto fuente para reproducir la prueba.

Los pasos y las firmas del script se contrastaron con la documentación y el código oficial de AR Foundation 6.3.5. La revisión del código incluye análisis sintáctico; Unity Editor no está instalado en este Mac. La compilación y el comportamiento en Android permanecen pendientes de validación en el equipo del estudiante o del profesor.

## Referencias técnicas

- Unity, configuración de escena: https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.3/manual/project-setup/scene-setup.html
- Unity, configuración de URP: https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.3/manual/project-setup/universal-render-pipeline.html
- Unity, biblioteca y manager de imágenes: https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.3/manual/features/image-tracking/artrackedimagemanager.html
- Unity, estado de rastreo: https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.3/manual/features/image-tracking/artrackedimage.html
- Google, imágenes aumentadas: https://developers.google.com/ar/develop/augmented-images
