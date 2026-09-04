# Práctica 2 · Cruzar el taller, y un paro que se queda abajo

La segunda práctica de VR. Parte del proyecto terminado de la práctica 1 y le agrega dos cosas: teletransporte con dos anclas y giro en pasos, para cruzar el taller sin marearte, y un paro de emergencia sobre el motor que se traba a la primera presión, ignora las siguientes y solo suelta cuando caminas hasta un tablero del otro lado del cuarto.

El cambio de fondo está en quién decide, no en el botón. Hasta ahora todo el comportamiento vino de componentes que Unity ya traía, cableados en el inspector. Un paro de emergencia no se puede expresar así, porque tiene una regla propia y un estado que sobrevive a que el dedo se vaya. Un botón que se destraba al soltarlo es un timbre, y a un motor nadie le pone un timbre. Esa regla es una clase, y por eso esta práctica escribe un interactable propio que hereda del que trae el toolkit.

La locomoción va primero por una razón práctica: si no puedes llegar hasta el paro, no puedes probarlo.

## Lo que necesitas antes de empezar

- El proyecto `Banco` de la práctica 1 compilando y pasando sus seis pruebas. Si la app abre plana o el torquímetro no se levanta, arregla eso primero; esta guía no repite esos pasos.
- El visor del salón, con la computadora ya autorizada.
- Espacio para dar dos o tres pasos y girar sobre tu propio eje, y tu compañero cuidando que no te lleves una silla.

## Parte 1 · Cruzar el taller sin marearse

Mover la vista con la palanca es la causa más común de malestar en VR. Los ojos reportan un desplazamiento que el oído interno nunca sintió, y el cuerpo resuelve ese desacuerdo con náusea. El teletransporte y el giro en pasos lo evitan en vez de pedirle a la gente que se acostumbre: entre un punto y el siguiente no hay movimiento intermedio que los ojos puedan reportar.

1. Selecciona el **XR Origin** dentro del XR Interaction Setup y agrégale tres componentes: **Locomotion Mediator**, **Teleportation Provider** y **Snap Turn Provider**. El mediador reparte el turno entre proveedores, para que dos formas de moverte no peleen por el mismo cuadro.
2. En el Snap Turn Provider deja el giro en **45 grados**, con un retardo corto, alrededor de `0.5`. Prueba después con 30 y con 90 y quédate con el que menos moleste; es una de las cosas que solo se deciden adentro.
3. Selecciona el `Piso` y agrégale el componente **Teleportation Area**. Usa el collider que el Plane ya tiene, así que no hace falta nada más. Ponlo solo en el piso: un área de teletransporte sobre la mesa de trabajo deja que alguien se pare encima del banco, y eso se ve gracioso una vez y estorba siempre.
4. Crea un objeto vacío llamado `AnclaMotor` en `-0.55, 0, 0.35`, justo frente al extremo del motor, y gíralo en Y para que mire hacia el banco. Agrégale el componente **Teleportation Anchor**. Un ancla no es lo mismo que un área: en vez de dejar que la persona caiga donde apuntó, la pone en un punto y con una orientación que tú escogiste. Para una estación donde hay algo que operar, eso es lo que quieres.
5. Crea el tablero de reposición al otro lado del taller. Un objeto vacío `TableroReposicion` en `3, 0, 0`, con un **Cube** hijo escalado `0.4, 0.3, 0.05` a la altura de la cintura, alrededor de `y = 1.1`. Que quede lejos es la idea, no un descuido.
6. Ponle su propia ancla, `AnclaTablero`, en `2.4, 0, 0`, mirando hacia el tablero, con su componente **Teleportation Anchor**.
7. Compila y pruébalo antes de escribir una sola línea de código. Apunta al piso con la mano y va a aparecer el arco; suelta y aparecerás allá. Gira con el stick y la vista tiene que saltar de golpe, nunca barrer. Si el arco no aparece, revisa que el rig del sample traiga su interactor de teletransporte y que las acciones estén habilitadas.

## Parte 2 · El motor y su paro

8. Crea `MotorDrive.cs` y ponlo en el objeto `Motor`, que ya existe desde la práctica 1:

```csharp
using UnityEngine;

public class MotorDrive : MonoBehaviour
{
    public bool Running { get; private set; } = true;

    public void Stop()
    {
        Running = false;
        Debug.Log("motor detenido");
    }

    public void Arm()
    {
        Running = true;
        Debug.Log("motor armado");
    }
}
```

Por ahora el motor solo lleva la cuenta de si está corriendo. En la sesión 4 esa bandera se vuelve una de las tres condiciones del enclavamiento completo, junto con la puerta de guarda cerrada y el eje por debajo de cincuenta rpm.

9. Crea el botón de paro: un **Cylinder** hijo de `Banco`, llamado `ParoDeEmergencia`, escala `0.05, 0.02, 0.05`, posición `0.6, 0.945, 1.2`. Queda al extremo derecho de la cubierta, chato y ancho, como un paro de verdad. El tamaño importa porque un dedo tiene que poder atinarle sin mirar.
10. Dale un material rojo. Es la única cosa roja de la escena, y así debe quedarse.
11. Al **Cube** del tablero dale un material de otro color. Ese es el que repone.

## Parte 3 · La clase propia

Un UnityEvent arrastrado en el inspector describe qué hace *este* botón. Una clase describe qué *es* un paro de emergencia, y cada copia que hagas llega sabiéndolo.

12. Crea `EmergencyStop.cs`:

```csharp
using UnityEngine;
using UnityEngine.XR.Interaction.Toolkit;
using UnityEngine.XR.Interaction.Toolkit.Interactables;

[CanSelectMultiple(false)]
public class EmergencyStop : XRBaseInteractable
{
    [SerializeField] MotorDrive motor;

    public bool Latched { get; private set; }

    protected override void OnSelectEntered(SelectEnterEventArgs args)
    {
        base.OnSelectEntered(args);

        if (Latched)
            return;

        Latched = true;
        motor.Stop();
        Debug.Log($"paro trabado por {args.interactorObject.transform.name}");
    }

    public void ClearFromPanel()
    {
        if (!Latched)
            return;

        Latched = false;
        motor.Arm();
        Debug.Log("paro repuesto desde el tablero");
    }
}
```

Línea por línea:

- `using UnityEngine.XR.Interaction.Toolkit;` trae `SelectEnterEventArgs` y el atributo `CanSelectMultiple`. Los dos viven en el namespace raíz del toolkit.
- `using UnityEngine.XR.Interaction.Toolkit.Interactables;` trae `XRBaseInteractable`. Los componentes de interactable se mudaron a este namespace hijo en la versión 3 del toolkit. Esa mudanza es la causa de casi todo error de compilación que vas a encontrar copiando ejemplos viejos de internet.
- `[CanSelectMultiple(false)]` declara que una sola mano a la vez puede seleccionar esto. Dos manos sobre un paro de emergencia no debería ser algo que el sistema siquiera pueda expresar, y el atributo lo vuelve imposible en lugar de improbable.
- `public class EmergencyStop : XRBaseInteractable` hereda de la clase base de todos los interactables. Al heredar, el objeto se registra solo con el XR Interaction Manager cuando se habilita, y se da de baja cuando se apaga. Nada de eso hay que escribirlo.
- `[SerializeField] MotorDrive motor;` es un campo privado que el inspector sí muestra. Ahí cae el objeto `Motor` cuando lo arrastras. El script nunca lo busca por nombre, y esa es la diferencia entre una referencia que el compilador vigila y una que truena en el visor.
- `public bool Latched { get; private set; }` es el estado que sobrevive a que el dedo se vaya. Cualquiera lo puede leer, solo esta clase lo puede escribir.
- `protected override void OnSelectEntered(SelectEnterEventArgs args)` es el método que el toolkit llama cuando alguien empieza a seleccionar este objeto. Es `protected` y `override` porque la base ya lo define; tú lo estás extendiendo, no inventando.
- `base.OnSelectEntered(args);` es la línea más importante del archivo y la que más se olvida. Levanta el evento `selectEntered` para todo el que esté escuchando desde el inspector. Quítala y tu código sigue corriendo, pero el sonido, el resaltado y cada listener que otra persona le colgó se callan sin un solo mensaje en la consola.
- `if (Latched) return;` es el enclavamiento. Una segunda presión sobre un paro ya trabado no hace nada, porque la máquina ya está abajo.
- `motor.Stop();` es lo único que el paro le pide al mundo. Todo lo demás es su propio estado.
- `args.interactorObject.transform.name` dice cuál mano lo hizo. Léelo dentro de la llamada y no guardes el objeto: la documentación del toolkit dice con todas sus letras que estos argumentos valen solo mientras el evento se está invocando. Un cuadro después estarías leyendo algo que ya se reutilizó.
- **No hay ningún `OnSelectExited`, y es a propósito.** Soltar el botón es exactamente lo que no debe liberar un paro de emergencia.
- `ClearFromPanel()` es público porque lo llama otro objeto, el tablero del otro lado del taller. Reponer es una caminata. Eso es diseño de seguridad, no una limitación técnica.

13. Selecciona `ParoDeEmergencia`, agrégale el componente **EmergencyStop** y arrastra el objeto `Motor` a su campo `motor`. Un campo vacío falla en silencio en el visor, donde no puedes ver el nulo, así que revísalo dos veces.
14. Agrégale también un **XR Poke Filter**, con **Poke Direction** en `Y`. Ese componente define los requisitos físicos de una presión, y con el eje puesto el paro solo responde a un dedo que baja sobre él, no a una mano que lo roza de lado. En el visor los contactos accidentales son la regla, no la excepción.
15. Al **Cube** del tablero ponle un **XR Simple Interactable**, el interactable genérico para cuando no necesitas comportamiento propio. En su evento **Select Entered**, desde el inspector, arrastra el objeto `ParoDeEmergencia` y escoge el método `ClearFromPanel`. La regla del paro vive en una clase y el cableado de un botón cualquiera vive en el inspector. Cada cosa donde le toca, y ese reparto es la sesión entera.

## Parte 4 · Compilar y probar

16. Compila con **Build And Run**. Los ajustes de Android no cambiaron desde la práctica 1. Deja **Development Build** marcado para poder leer la consola.
17. Ponte el visor y pídele a tu compañero que lea `adb logcat`. Recorre esta lista:
    - Apuntas al piso, te teletransportas, llegas. Giras con el stick y la vista salta en pasos.
    - Te paras en `AnclaMotor` y quedas viendo el banco, sin tener que buscarlo.
    - Presionas el paro con el dedo. El log dice `paro trabado` con el nombre de la mano, y `motor detenido`.
    - Levantas el dedo. El log no dice nada nuevo, y `Latched` sigue en verdadero.
    - Presionas el paro otra vez. Tampoco pasa nada, porque la guarda regresó temprano.
    - Te teletransportas a `AnclaTablero`, tocas el botón de reposición, y el log dice `paro repuesto` y `motor armado`.
    - Regresas al banco y el paro vuelve a trabar. El ciclo cierra.
18. Rómpelo a propósito una vez. Comenta la línea `base.OnSelectEntered(args);`, recompila y presiona el paro. El motor se sigue deteniendo y el log de tu propia clase sigue apareciendo, así que todo parece funcionar. Lo que se cayó en silencio es cualquier cosa colgada del evento desde el inspector. Anota qué observaste y descomenta la línea.
19. Cámbiense el visor para que tu compañero pruebe su propio build. Pregúntale si 45 grados de giro le acomodaron o si hubiera preferido 30, porque ese número casi nunca coincide entre dos personas.

## Si algo sale mal

Las fallas de build y de entrada de la práctica 1 aplican igual aquí y se arreglan en el mismo lugar. Estas son las nuevas:

| Qué ves | Qué significa | Dónde se arregla |
|---|---|---|
| No aparece el arco de teletransporte | Falta el Teleportation Provider, o el piso no tiene área | Pasos 1 y 3 |
| El arco aparece y no te mueve | Falta el Locomotion Mediator en el XR Origin | Paso 1 |
| El giro barre en vez de saltar | Está activo un proveedor de giro continuo | Deja solo el Snap Turn Provider, paso 1 |
| Puedes teletransportarte encima del banco | El área quedó en más geometría de la que creías | Paso 3 |
| El ancla te deja mirando a otro lado | Le falta rotación en Y | Pasos 4 y 6 |
| El paro no responde al dedo | Falta el collider, el componente, o el poke viene del eje equivocado | Pasos 9, 13 y 14 |
| El paro se dispara al rozarlo de lado | Sin XR Poke Filter, o con Poke Direction mal puesta | Paso 14 |
| `NullReferenceException` al presionar | El campo `motor` quedó vacío en el inspector | Paso 13 |
| El paro se destraba solo al levantar el dedo | Le agregaste un `OnSelectExited` que no debía existir | Parte 3, la nota del enclavamiento |
| El botón de reposición no repone | El evento del inspector quedó sin método, o apunta al objeto equivocado | Paso 15 |
| No compila, `XRBaseInteractable` no se encuentra | Falta el `using` del namespace `Interactables` | Parte 3, primer bloque |

## Entregable

Un video corto de la pantalla del visor con las siete pruebas del paso 17, en ese orden, y el texto de la consola pegado aparte. Más un párrafo sobre el paso 18: qué se rompió al quitar la llamada a la base, cómo te diste cuenta, y por qué esa falla es más cara que una que truena.

El cuadro que más pesa en la revisión es el cuarto: levantar el dedo y que el paro siga trabado. Es el único que demuestra que hay estado y no una reacción.
