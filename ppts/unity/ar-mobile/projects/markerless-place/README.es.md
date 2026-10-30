# Colocar figuras en AR para Unity 6.3 LTS

Elige Cubo o Esfera y toca una superficie detectada para colocar una figura de 20 cm. Camina a su alrededor, aparta la cámara y vuelve a la zona mientras la sesión conserve el rastreo. Toca una figura para seleccionarla y usa Eliminar selección para quitarla.

## Abrir el proyecto

1. Agrega esta carpeta desde Unity Hub y ábrela con Unity 6.3 LTS. La versión registrada es 6000.3.27f1.
2. Espera la descarga de paquetes y la compilación de scripts. La primera importación necesita internet.
3. Ejecuta Tools > AR Place > Preparar proyecto si el asistente no preparó los materiales automáticamente.
4. Abre Assets/Scenes/Placement.unity y presiona Play para probar la simulación del piso y la pared.

En la simulación, haz clic en una superficie para colocar la figura. W, A, S y D permiten caminar; Q y E cambian la altura. Mantén el botón derecho del mouse para girar la cámara y usa Shift si necesitas desplazarte más rápido.

## Android y anclajes

Instala Android Build Support, SDK, NDK y OpenJDK desde Unity Hub. Selecciona Android en Build Profiles, revisa Project Validation y confirma que ARCore esté activado antes de Build And Run.

El proyecto usa URP 17.3.0, AR Foundation 6.3.5 y ARCore 6.3.5. No requiere un marcador: detecta planos horizontales y verticales y crea un anclaje para cada figura colocada.

Los objetos permanecen durante la sesión y no se eliminan por distancia. La estabilidad depende del rastreo; cerrar la app o reiniciar la sesión elimina la distribución. El proyecto no guarda posiciones para otro día ni activa servicios de anclajes en la nube.

La guía completa está incluida como Guia.es.md y Guia.es.pdf dentro del ZIP. Su fuente en el repositorio está en ../../labs/lab04.es.md y describe las pruebas de colocación, selección, eliminación y recorrido.

## Validación

La carpeta Validation ejecuta 27 comprobaciones del inventario con .NET 10 y analiza la sintaxis de los cinco scripts de Unity. Puedes ejecutarlas desde esta carpeta con la siguiente instrucción:

```sh
dotnet run --project Validation/Validation.csproj
```

La importación, la compilación de Unity, la interfaz y los anclajes deben probarse en el Editor y en un celular. El paquete contiene el proyecto fuente y la guía; no incluye un APK compilado.

El asistente prepara AR_URP y AR_Renderer en Assets/Settings y agrega AR Background Renderer Feature. Ejecuta Preparar proyecto si abres una copia anterior para convertir sus materiales a URP. Revisa Graphics, Quality y la consola antes de compilar.
