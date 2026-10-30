# VR-C04 | Cibermareo y diseño de comodidad

Unity 6.3 LTS · URP · Meta Quest 3S · Laboratorio guiado opcional

## Qué vas a construir y analizar

Agregarás un menú de preferencias a la sala de VR-C03. La escena comenzará con teletransporte y snap turn; el menú permitirá revisar las opciones y restaurar esos valores. Después analizarás un caso de cibermareo mediante un storyboard.

Esta actividad es opcional, no tiene columna de calificación y no sustituye los tres laboratorios obligatorios. El montaje y la revisión se pueden completar en el Editor. No se requiere provocar malestar, comparar síntomas ni recopilar datos de otras personas. Tiempo estimado: 90 minutos.

## Antes de empezar

- Completa VR-C03, con sus destinos y Canvas World Space. Conserva Unity 6.3 LTS, URP y Starter Assets de XRI 3.3.2.
- Crea una copia de la escena. La revisión de las preferencias no exige probar movimiento continuo en un visor.
- El término cibermareo, o VR sickness, describe malestar asociado con una experiencia de realidad virtual. Aquí se estudian decisiones de diseño; no se realiza una evaluación médica.

## Parte 1: Preparar el menú

1. Guarda la escena de VR-C03 como Assets/Scenes/VR-C04-Opcional.unity. Conserva un solo XR Origin, un Interaction Manager y un EventSystem con XR UI Input Module.
2. Duplica InstruccionesXR y llama a la copia PreferenciasXR. Pon Position (0, 1.3, 1.5), Rotation cero y Scale (0.002, 0.002, 0.002). Conserva Width = 800 y aumenta Height a 600.
3. En la copia elimina los hijos MostrarAyuda y Ayuda. Conserva Canvas, Canvas Scaler y Tracked Device Graphic Raycaster. Asigna como Event Camera la Main Camera del XR Origin si el campo quedó vacío.
4. Crea dos UI > Toggle bajo el Canvas. Nómbralos MovimientoContinuo y GiroContinuo. Usa anclajes centrales, posiciones (0, 170) y (0, 80), y tamaño (650, 70). Cambia sus etiquetas a MOVIMIENTO CONTINUO y GIRO CONTINUO. En ambos deja Is On desactivado.
5. Crea dos `Button - TextMeshPro`: Restaurar, en (0, -20), con tamaño (650, 70) y texto VOLVER A TELETRANSPORTE Y SNAP; y Salir, en (0, -110), con texto SALIR DE LA APP. Usa fuente 30 y comprueba que quepan las etiquetas.
6. Agrega un `Text - TextMeshPro` llamado EstadoPreferencias, en (0, -220), con tamaño (700, 100), fuente 28 y alineación centrada. Será la confirmación escrita del modo actual.

El menú permanece en el espacio virtual. Evita hacerlo hijo de la cámara o cubrir toda la vista. Su ubicación y tamaño se deben comprobar en relación con la tarea y las personas que lo usarán. [1]

::: pagebreak

## Parte 2: Crear el controlador de preferencias

7. Crea Assets/Scripts/ComfortOptionsLab.cs y copia este código completo. El namespace de Starter Assets requiere que ese sample de XRI 3.3.2 esté importado.

```csharp
using TMPro;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.XR.Interaction.Toolkit.Samples.StarterAssets;
public sealed class ComfortOptionsLab : MonoBehaviour
{
    [SerializeField] ControllerInputActionManager leftController;
    [SerializeField] ControllerInputActionManager rightController;
    [SerializeField] Toggle moveToggle;
    [SerializeField] Toggle turnToggle;
    [SerializeField] TMP_Text statusText;
    bool continuousMove;
    bool continuousTurn;
    void Start()
    {
        if (leftController == null || rightController == null ||
            moveToggle == null || turnToggle == null || statusText == null)
        {
            Debug.LogError("Completa las cinco referencias del menu.", this);
            enabled = false;
            return;
        }
        RestoreDefaults();
    }
    public void SetContinuousMove(bool value)
    {
        if (!enabled) return;
        continuousMove = value;
        ApplyModes();
    }
    public void SetContinuousTurn(bool value)
    {
        if (!enabled) return;
        continuousTurn = value;
        ApplyModes();
    }
    public void RestoreDefaults()
    {
        continuousMove = false;
        continuousTurn = false;
        moveToggle.SetIsOnWithoutNotify(false);
        turnToggle.SetIsOnWithoutNotify(false);
        ApplyModes();
    }
    void ApplyModes()
    {
        leftController.smoothMotionEnabled = continuousMove;
        rightController.smoothMotionEnabled = continuousMove;
        leftController.smoothTurnEnabled = continuousTurn;
        rightController.smoothTurnEnabled = continuousTurn;
        statusText.text = (continuousMove ? "Movimiento continuo" : "Teletransporte")
            + " / " + (continuousTurn ? "Giro continuo" : "Snap turn");
    }
    public void QuitApplication()
    {
        Debug.Log("Solicitud de salida de la aplicacion.", this);
        Application.Quit();
    }
}
```

::: pagebreak

## Parte 3: Conectar el Inspector y la UI

8. Crea un GameObject vacío ControlComodidad y agrega ComfortOptionsLab. En Left Controller y Right Controller arrastra los objetos del XR Origin que contienen Controller Input Action Manager. No arrastres los modelos visuales de los controles.
9. Asigna MovimientoContinuo a Move Toggle, GiroContinuo a Turn Toggle y EstadoPreferencias a Status Text. Las cinco referencias deben quedar completas antes de Play.
10. En MovimientoContinuo > Toggle > On Value Changed(bool), agrega ControlComodidad y selecciona ComfortOptionsLab > SetContinuousMove desde la sección Dynamic bool. No uses un bool estático, porque el método debe recibir el valor de la casilla.
11. En GiroContinuo conecta On Value Changed(bool) con SetContinuousTurn, también en Dynamic bool.
12. En Restaurar > Button > On Click(), conecta ControlComodidad con RestoreDefaults(). En Salir conecta QuitApplication(). Conserva una sola llamada por botón.
13. En Locomotion/Turn verifica Snap Turn Amount = 45. En Locomotion/Move deja Dynamic Move Provider del prefab; no agregues otro Continuous Move Provider. Para la revisión del Editor puedes establecer Move Speed = 1. El script cambia las acciones permitidas por los managers, no mueve la cámara por su cuenta. [2]
14. Guarda la escena y revisa la consola. Si falta el tipo ControllerInputActionManager, importa Starter Assets de la misma versión y comprueba su namespace antes de reemplazar código.

## Parte 4: Revisar sin provocar malestar

15. En Play, con XR Interaction Simulator, comprueba que ambas casillas comiencen apagadas y que el texto indique Teletransporte / Snap turn.
16. Acciona una casilla con el rayo de UI y verifica que cambien el texto y la propiedad correspondiente en ambos Controller Input Action Manager. Puedes comprobar la conexión en el Inspector sin efectuar un desplazamiento continuo.
17. Presiona Restaurar. Las casillas deben apagarse, los managers deben regresar a sus valores iniciales y el texto debe confirmarlo. SetIsOnWithoutNotify actualiza la UI sin disparar de nuevo sus callbacks.
18. Presiona Salir. En el Editor aparecerá el mensaje de consola, pero Application.Quit no detiene Play. Detén la ejecución con el botón del Editor. En una aplicación compilada la llamada solicita salir.
19. Si decides compilar, deja solo VR-C04-Opcional.unity habilitada en el perfil Meta Quest y usa Build And Run siguiendo VR-C01. Verifica el estado inicial y la opción de salida; no necesitas activar movimiento o giro continuos dentro del visor.

Meta recomienda preferencias configurables y valores iniciales orientados a la comodidad. Las opciones no garantizan que todas las personas toleren una experiencia del mismo modo. [3] Si aparece malestar en una observación física, termina la experiencia y retira el visor; no continúes para completar una comparación.

::: pagebreak

## Caso para analizar después del montaje

Una visita virtual comienza sobre una plataforma que avanza automáticamente. Al tomar una herramienta, la cámara se sacude para simular su peso. Las instrucciones están detrás del usuario y solo existe giro continuo. La visita no tiene un menú accesible para recuperar preferencias o salir.

1. Identifica las cinco decisiones que revisarías. Relaciona cada una con una acción que el usuario puede o no puede controlar.
2. Propón una señal que comunique el peso de la herramienta sin mover artificialmente la cámara. Incluye una señal que no dependa solo del audio.
3. Dibuja un storyboard de seis viñetas: inicio, preferencias, desplazamiento, herramienta, consulta de instrucciones y salida. Indica quién controla cada cambio de posición y orientación.
4. Explica qué elementos de tu menú ya están implementados y qué decisiones del caso siguen siendo propuestas. No presentes el storyboard como una prueba con usuarios.
5. Describe los límites de una revisión en el Editor. Explica por qué tu tolerancia personal no permite concluir que todas las personas tolerarán el mismo contenido.

## Si algo sale mal

| Síntoma | Revisión concreta |
| --- | --- |
| Falta ControllerInputActionManager. | Revisa Starter Assets 3.3.2 y la línea using del script. |
| La casilla cambia, pero el modo no. | Revisa Dynamic bool, referencias de los dos managers y errores de consola. |
| Restaurar no actualiza la UI. | Comprueba Move Toggle, Turn Toggle y la llamada única a RestoreDefaults. |
| El rayo no opera la interfaz. | Revisa Canvas World Space, Event Camera, raycaster, XR UI Input Module y UI Press según VR-C03. |
| Salir no detiene el Editor. | Ese resultado es esperado. Application.Quit se comprueba en el APK; detén Play manualmente. |

::: pagebreak

## Entrega opcional y revisión

Si realizas la actividad, prepara Apellido_VR-C04-Opcional.pdf, de 3 a 5 páginas. Incluye el menú, sus referencias y eventos, una comprobación de Restaurar, el storyboard y las respuestas. Conserva el proyecto con su script. El docente podrá indicar el medio para compartirlo; este recurso no crea una entrega obligatoria en Blackboard.

La revisión cualitativa considera si el menú tiene referencias completas, comienza con teletransporte y snap turn, restaura ambos controles y comunica el estado. También considera que el storyboard responda al caso y reconozca las pruebas pendientes. No añade puntos ni requiere utilizar el visor.

## Referencias y alcance de la revisión

[1] Meta. Consulta la colocación de contenido y la comodidad visual y física.

[Comfort](https://developers.meta.com/vr/design/comfort/)

[2] Unity XRI 3.3. Consulta Controller Input Action Manager y la configuración del prefab. Sus propiedades públicas se contrastaron con el código de Starter Assets 3.3.2.

[Starter Assets](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.3/manual/samples-starter-assets.html)

[3] Meta. Consulta las preferencias de locomoción y sus valores iniciales.

[Locomotion user preferences](https://developers.meta.com/vr/design/locomotion-user-preferences/)

No se ejecutó una compilación en Unity ni una prueba física durante la elaboración de la guía. El montaje del menú y su comprobación forman parte de esta actividad opcional.
