# 01 · Resolución de problemas y diseño de algoritmos

<img src="assets/problem-solving.png" alt="Secuencia doodle: preocupado → pensando → eureka" width="100%">

Todo programa nace de un **problema**. Este módulo enseña la mentalidad necesaria *antes* de escribir código.

## Los tres estados de quien resuelve problemas

El doodle de arriba captura lo que pasa cada vez que enfrentas un problema real:

1. **Preocupado.** Ves el problema pero aún no sabes cómo abordarlo.
2. **Pensando.** Lo descompones, reúnes información, comparas opciones.
3. **Eureka.** Aparece una solución candidata. Listo para diseñarla y probarla.

Programar sigue exactamente ese arco. Vamos a hacerlo **repetible** en lugar de azaroso.

---

## 1. Resolución de problemas

> **Definición:** proceso de identificar y resolver retos de forma lógica y efectiva.

Antes de construir software, hay que entender el problema. Escribir código antes de entenderlo es la razón más común por la que los programas fallan.

### Los 7 pasos

<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/magnifying-glass.svg" width="18" height="18" alt=""> **1. Identificar y definir el problema**

- Entiéndelo con claridad. ¿Puedes decirlo en una oración?
- Divídelo en partes manejables.
- Encuentra la causa principal, no solo los síntomas.

<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/box-archive.svg" width="18" height="18" alt=""> **2. Reunir información**

- Investiga lo que ya se sabe.
- Recolecta datos.
- Habla con quienes han vivido la situación.

<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/chart-line.svg" width="18" height="18" alt=""> **3. Analizar el problema**

- Examina la información reunida.
- Busca patrones, restricciones y causas.
- Usa herramientas — diagramas causa-efecto, FODA — cuando ayuden.

<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lightbulb.svg" width="18" height="18" alt=""> **4. Desarrollar posibles soluciones**

- Brainstorm de varias alternativas.
- Combina enfoques creativos y estructurados.
- No te enamores de la primera idea.

<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scale-balanced.svg" width="18" height="18" alt=""> **5. Evaluar las soluciones**

- Compara pros y contras.
- Considera factibilidad, costo, impacto.
- Elige la opción más prometedora.

<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/hammer.svg" width="18" height="18" alt=""> **6. Implementar la solución**

- Plan de acción.
- Asignar responsabilidades.
- Definir cronograma.
- En programación, esto se convierte en escribir la aplicación.

<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/arrows-rotate.svg" width="18" height="18" alt=""> **7. Monitorear y ajustar**

- ¿Funciona realmente?
- Detecta errores. Recoge retroalimentación.
- Ajusta cuando sea necesario.

### Escenarios cotidianos para practicar

Aplica los 7 pasos a situaciones que aún no tienen que ver con computadoras:

- Organizar un viaje grupal con presupuestos y preferencias distintas.
- Diagnosticar por qué una computadora se volvió lenta.
- Decidir el menú de una fiesta con restricciones alimentarias.
- Arreglar una bicicleta a la que se le sale la cadena.
- Empacar eficientemente para un viaje de una semana con solo equipaje de mano.

Si puedes recorrer los 7 pasos en papel para cada escenario, ya estás pensando como programador.

---

## 2. Algoritmos

> **Definición:** descripción paso a paso de cómo resolver un problema.

Una vez entendido el problema, describes la secuencia de acciones que lo resuelve. Esa secuencia es el algoritmo.

### La analogía de la receta

<img src="assets/doodle-thinking-blushed-algo.png" alt="Doodle de una persona pensando en 'algo' en un pizarrón" width="320">

Un algoritmo es como una **receta**. Una receta lista ingredientes y el orden exacto de pasos. Un algoritmo lista entradas y el orden exacto de acciones. Omite un paso, cambia el orden, y el resultado cambia.

### Algoritmos cotidianos

- Preparar un sándwich.
- Lavar una tanda de ropa.
- Hacer té.
- Convertir Fahrenheit a Celsius.
- Buscar un libro específico en una repisa.

### Algoritmos en programación

En cómputo los algoritmos definen los pasos que luego se traducen a código. Una app de navegación usa un algoritmo para:

1. Identificar origen y destino.
2. Calcular rutas posibles.
3. Seleccionar la más corta (o la más rápida).

La misma idea de tres pasos, ya sea para un humano o una computadora.

---

## 3. Diagramas de flujo

> **Definición:** forma visual de representar un algoritmo usando formas estándar.

Los diagramas de flujo son la primera representación **formal** de un algoritmo. Son dibujos con una gramática estricta — quien sabe leerlos entiende el algoritmo sin importar el idioma.

### Formas principales

| Forma | Significado |
|-------|-------------|
| Óvalo | Inicio / Fin del proceso |
| Rectángulo | Proceso / Tarea (acción a realizar) |
| Paralelogramo | Entrada / Salida (dato que entra o sale) |
| Rombo | Decisión (sí/no que bifurca el flujo) |
| Círculo | Conector (salta a otra parte del diagrama) |
| Flecha | Dirección y orden |

### Por qué importan

Ayudan a:

- Visualizar un proceso con claridad.
- Entender el orden de los pasos.
- Detectar decisiones y bifurcaciones.
- Simplificar lo que parece complejo.

### Diagramas de práctica

Dibuja uno para cada escenario:

- Ir a una tienda a comprar una pluma (decide: ¿está abierta?, ¿tienen plumas?, ¿tienes dinero?).
- Calcular el promedio de dos números.
- Imprimir los números del 1 al 5.

### Herramientas

- [diagrams.net](https://app.diagrams.net/) — gratuita, funciona en el navegador.
- [Lucidchart](https://www.lucidchart.com/) — tiene nivel gratuito.
- Lápiz y papel — sigue siendo la forma más rápida de iterar.

---

## 4. Pseudocódigo

> **Definición:** forma estructurada e independiente del lenguaje para describir un algoritmo.

El pseudocódigo es la segunda representación principal. Parece código pero no es ejecutable en ningún lenguaje real — su único trabajo es describir la lógica con claridad para que los humanos la revisen antes de comprometerse a una sintaxis.

### Por qué importa

Ayuda a:

- Enfocarte en la **lógica** antes que en la **sintaxis**.
- Describir algoritmos en formato limpio y legible.
- Discutir soluciones con otros sin importar el lenguaje.
- Detectar errores antes de escribir el código real.

### Acciones típicas

- `INICIO / FIN`
- `LEER <variable>`
- `ESCRIBIR <expresión>`
- `<variable> = <expresión>` (asignación)
- Aritmética: `+`, `-`, `*`, `/`
- Condiciones: `SI <condición> ENTONCES ... SINO ... FIN SI`
- Ciclos: `MIENTRAS <condición> HACER ... FIN MIENTRAS`

### Ejemplo — suma de dos números

```text
INICIO
  LEER a
  LEER b
  suma = a + b
  ESCRIBIR suma
FIN
```

### Pseudocódigo de práctica

- Suma de dos números (arriba).
- Imprimir números del 1 al 5.
- Conversión de Fahrenheit a Celsius.
- Iniciar sesión en una red social (leer usuario, leer contraseña, verificar coincidencia, permitir o denegar).

---

## Cierre del Módulo 01

Combinando **resolución de problemas**, **algoritmos**, **diagramas de flujo** y **pseudocódigo**, empiezas a pensar como programador **antes** de escribir una sola línea de código real. Siguiente módulo: qué es programar realmente, qué lenguajes usamos y qué está haciendo la computadora por debajo.
