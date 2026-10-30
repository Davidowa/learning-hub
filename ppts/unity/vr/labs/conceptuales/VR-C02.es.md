# VR-C02 | Interacción y retroalimentación

Unity 6.3 LTS · URP · Meta Quest 3S · Montaje guiado y análisis

## Qué vas a construir

Ampliarás la sala de VR-C01 con una herramienta que se pueda tomar y soltar, y un interruptor que encienda o apague una lámpara. Agregarás una señal de disponibilidad y un estado escrito para que la interacción no dependa solo del color.

Primero realizarás el montaje y sus comprobaciones; después explicarás los estados y las decisiones. La entrega es individual y vale 100 puntos. Tiempo estimado: dos sesiones de 80 minutos.

## Antes de empezar

- Completa el montaje de VR-C01, incluida la sala, OpenXR, los controles y el simulador. Conserva Unity 6.3 LTS, URP y Starter Assets de XRI 3.3.2.
- Utiliza una copia de la escena. Este laboratorio no necesita locomoción por joystick ni seguimiento de manos.
- Si no tienes Quest 3S, utiliza XR Interaction Simulator. Registra la diferencia entre esa comprobación y una prueba del APK en el visor.

## Parte 1: Preparar la herramienta

1. Abre LaboratoriosVR y guarda la escena de VR-C01 con File > Save As como Assets/Scenes/VR-C02.unity. Conserva la escena original.
2. Cambia el nombre de CuboMedida a Herramienta. Déjalo como hijo de Entorno, con Position (0, 0.85, 1.2) y Scale (0.2, 0.2, 0.2). La superficie de la mesa debe conservar su Box Collider.
3. En Herramienta conserva Box Collider, con Is Trigger desactivado. Agrega Rigidbody, activa Use Gravity y deja Is Kinematic desactivado. Usa Collision Detection = Continuous Dynamic e Interpolate = Interpolate como configuración inicial del ejercicio.
4. Agrega XR Grab Interactable. En Interaction Manager asigna el manager de la escena; en Interaction Layer Mask selecciona Default. En Colliders agrega el Box Collider de Herramienta si no aparece detectado.
5. Configura Select Mode = Single, Movement Type = Kinematic, Track Position y Track Rotation activados, y Throw On Detach desactivado. El objeto seguirá al interactor durante la selección y recuperará su comportamiento físico al soltarlo. [1]
6. Deja Attach Transform vacío para utilizar la referencia del propio objeto. No hagas Herramienta hija de un control ni de la cámara: XRI debe administrar la selección.

## Punto de comprobación

En Play, la herramienta debe caer sobre la mesa y detenerse. Si atraviesa la superficie, corrige primero los colliders y la posición inicial. Después prueba tomarla con el simulador o el control. Un objeto resaltado todavía no demuestra que pueda seguir a la mano.

::: pagebreak

## Parte 2: Agregar una señal de disponibilidad

7. Crea como hijo de Herramienta un objeto 3D `Text - TextMeshPro` llamado AvisoTomar. Escribe TOMAR, usa alineación centrada y colócalo sobre el cubo, mirando hacia el origen. Ajusta posición y tamaño en Scene hasta que sea legible. Desactiva AvisoTomar en la jerarquía.
8. En XR Grab Interactable de Herramienta expande Interactable Events. En First Hover Entered agrega una entrada con +. Arrastra AvisoTomar al campo del objeto y selecciona GameObject > SetActive(bool); marca el argumento como verdadero.
9. En Last Hover Exited agrega otra entrada para el mismo AvisoTomar, con SetActive(bool) y argumento falso. Usa estos eventos de primer y último hover para contemplar que más de un interactor pueda apuntar al objeto.
10. Prueba que el aviso aparezca al apuntar o acercar un interactor y desaparezca cuando ninguno lo considere candidato. La selección usa una acción distinta del hover.

## Parte 3: Crear el interruptor y la lámpara

11. Crea bajo Entorno un Cube llamado Interruptor, con Position (0.4, 0.81, 1.2) y Scale (0.12, 0.12, 0.12). Conserva Box Collider y no agregues Rigidbody. Crea un texto 3D sobre él que diga SELECCIONAR: ENCENDER/APAGAR.
12. Agrega XR Simple Interactable a Interruptor. Asigna el Interaction Manager, Interaction Layer Mask = Default y Select Mode = Single. Esta pieza se puede seleccionar, pero permanecerá fija.
13. Crea GameObject > Light > Point Light como hijo de Entorno y nómbralo LuzLaboratorio. Pon Position (0, 1.7, 1.2), Range = 3 y desactiva las sombras de esa luz. Conserva la Directional Light para que la sala siga visible cuando apagues la lámpara.
14. Crea dos textos 3D juntos, en Position aproximada (0.4, 1.1, 1.2): uno llamado EstadoEncendido con el texto ENCENDIDA y otro EstadoApagado con APAGADA. Oriéntalos hacia el origen y usa la misma posición y tamaño; el script mostrará solo uno.
15. Crea un GameObject vacío ControlLampara, con Transform restablecido. En Assets/Scripts crea LightSwitchLab.cs y copia el código completo de la página siguiente. Espera a que termine la compilación.

## Cómo conectar un evento en el Inspector

El botón + agrega una llamada. El campo del objeto debe recibir el GameObject que tiene el componente indicado. Después selecciona su método y, cuando sea un bool estático, marca o desmarca la casilla del argumento. No arrastres el archivo .cs al campo del evento.

::: pagebreak

## Parte 4: Programar y conectar el cambio de estado

```csharp
using UnityEngine;

public sealed class LightSwitchLab : MonoBehaviour
{
    [SerializeField] Light targetLight;
    [SerializeField] GameObject onLabel;
    [SerializeField] GameObject offLabel;
    bool isOn;

    void Start()
    {
        if (targetLight == null || onLabel == null || offLabel == null)
        {
            Debug.LogError("Asigna luz y las dos etiquetas.", this);
            enabled = false;
            return;
        }
        ApplyState();
    }

    public void ToggleLamp()
    {
        if (!enabled || targetLight == null) return;
        isOn = !isOn;
        ApplyState();
    }

    void ApplyState()
    {
        targetLight.enabled = isOn;
        onLabel.SetActive(isOn);
        offLabel.SetActive(!isOn);
        Debug.Log(isOn ? "Lampara encendida" : "Lampara apagada", this);
    }
}
```

16. Agrega LightSwitchLab a ControlLampara. En Target Light arrastra LuzLaboratorio; en On Label, EstadoEncendido; y en Off Label, EstadoApagado. Las referencias deben ser objetos de la escena.
17. En XR Simple Interactable de Interruptor abre Interactable Events > Select Entered. Agrega una entrada, arrastra ControlLampara y selecciona LightSwitchLab > ToggleLamp(). Debe existir una sola llamada para este evento.
18. No conectes también Activated al mismo método en esta versión. Así, una selección produce un cambio y no dos cambios consecutivos. Guarda la escena.

El script mantiene un bool, aplica el estado a la luz y muestra una etiqueta. Al volver a ejecutar la escena comienza apagada. No guarda el estado al cerrar la aplicación. Select Entered enciende o apaga el interruptor; Activate queda reservado para una acción diferente en el análisis.

::: pagebreak

## Parte 5: Probar las acciones

19. Presiona Play y da foco a Game. Con el simulador activa un control y utiliza su ayuda para ejecutar Grip y Trigger. En los XRI Default Input Actions de 3.3.2, Select utiliza GripButton y Activate utiliza TriggerButton para XRController. Comprueba los vínculos si modificaste el asset. [2]
20. Apunta a Herramienta: debe aparecer TOMAR. Ejecuta Select, mueve el control y confirma que el cubo lo sigue. Suelta Select para dejarlo caer sobre la mesa. Prueba la misma secuencia con el otro control.
21. Mientras un control mantiene seleccionada la herramienta, intenta seleccionarla con el otro. Con Select Mode = Single no deben quedar dos selectores simultáneos. Algunas transferencias pueden depender de los interactores; registra lo observado.
22. Apunta a Interruptor y ejecuta Select. Debe cambiar una sola vez el estado de la lámpara y su etiqueta. Mantener Select presionado no debe generar cambios cada cuadro. Suelta y vuelve a seleccionar para alternar otra vez.
23. Con el interruptor seleccionado, ejecuta Activate. Como no lo conectaste, no debe alternar la lámpara. Esta prueba permite distinguir dos eventos que a veces se confunden.
24. Detén Play. Para Quest 3S, selecciona el perfil Meta Quest, agrega VR-C02.unity y déjala como única escena habilitada. Revisa Project Validation y usa Build And Run, siguiendo la preparación USB de VR-C01.
25. Repite la toma, liberación y dos cambios del interruptor dentro del visor, si está disponible. Graba evidencia o marca la comprobación física como pendiente. No confundas una simulación con una prueba en el dispositivo.

## Jerarquía añadida

```text
Entorno
  SuperficieMesa [Box Collider]
  Herramienta [Rigidbody, XR Grab Interactable]
    AvisoTomar [inactivo al inicio]
  Interruptor [XR Simple Interactable]
  LuzLaboratorio [Point Light]
  EstadoEncendido
  EstadoApagado
ControlLampara [LightSwitchLab]
```

## Si algo sale mal

| Síntoma | Revisión concreta |
| --- | --- |
| El objeto se apunta, pero no se toma. | Revisa Select, Grip, Interaction Manager y la coincidencia de Interaction Layer Mask. |
| Se selecciona, pero no sigue al control. | Comprueba XR Grab Interactable, Track Position/Rotation y Rigidbody. XR Simple Interactable no aporta agarre. |
| El interruptor cambia dos veces. | Busca llamadas duplicadas o una conexión adicional a Activated. Deja solo Select Entered. |
| La lámpara no responde. | Revisa las tres referencias de LightSwitchLab y la llamada a ToggleLamp sobre ControlLampara. |
| El aviso queda visible. | Revisa Last Hover Exited y su argumento falso; no conectes solo el evento de entrada. |

::: pagebreak

## Análisis después del montaje

1. Dibuja los estados disponible, apuntada, tomada y liberada de Herramienta. Etiqueta cada transición con una acción o evento observado.
2. Dibuja por separado los estados encendida y apagada de la lámpara. Explica por qué seleccionar Interruptor no significa tomarlo.
3. Propón cómo cambiar el interruptor para que responda a Activate. Indica qué conexión quitarías y qué gesto tendría que efectuar el usuario mientras mantiene la selección. No conectes ambos eventos a la vez sin justificarlo.
4. Explica el papel de Collider, Rigidbody, interactor, interactuable y manager. Diferencia las capas de interacción de las capas físicas.

## Entrega y rúbrica

Entrega Apellido_VR-C02.pdf, de 3 a 5 páginas. Incluye Inspector de Herramienta, referencias del script, evento del interruptor, dos diagramas de estados y una tabla con cuatro pruebas: apuntar, tomar, soltar y cambiar la lámpara. Para cada prueba indica acción, resultado esperado y resultado observado. Añade las respuestas y registra las versiones.

Conserva el proyecto fuente con VR-C02.unity y LightSwitchLab.cs. Si usaste simulador, indica qué falta comprobar en Quest 3S. No se pide un APK en lugar del reporte.

| Criterio | Puntos | Evidencia para obtener el total |
| --- | --- | --- |
| Monta la herramienta. | 30 | Configura física, agarre, un selector y aviso de hover. |
| Monta la lámpara. | 30 | Asigna las referencias y un evento que alterna luz y etiqueta una vez por selección. |
| Comprueba las acciones. | 20 | Documenta las cuatro pruebas y distingue simulación de dispositivo. |
| Explica estados y componentes. | 20 | Presenta dos diagramas y responde las cuatro preguntas. |
| Total | 100 | La evidencia corresponde al montaje propio. |

Cada criterio recibe el total si cumple la evidencia, la mitad si está parcial pero verificable y cero si falta o contradice el funcionamiento analizado.

## Referencias y alcance de la revisión

[1] Unity XRI 3.3. Consulta las propiedades de agarre y los eventos de interacción.

[XR Grab Interactable](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.3/manual/xr-grab-interactable.html)

[Interactable Events](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.3/manual/interactable-events.html)

[2] Unity XRI 3.3. Consulta las acciones y los prefabs de Starter Assets.

[Starter Assets](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.3/manual/samples-starter-assets.html)

Se contrastaron nombres, propiedades y vínculos con el paquete oficial XRI 3.3.2. El script usa UnityEngine y UnityEvents del Inspector. No se ejecutó una compilación de Unity ni una prueba física durante la elaboración de la guía.
