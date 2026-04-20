# 01 · Resolución de problemas

<img src="assets/problem-solving.png" alt="Secuencia doodle: preocupado → pensando → eureka" width="100%">

Todo programa nace de un **problema**. Antes de tocar el teclado, quien programa con oficio recorre un proceso mental para **entender** el problema y **diseñar** una solución. Este módulo enseña ese proceso.

## Los tres estados de quien resuelve problemas

El doodle captura lo que pasa cada vez que enfrentas un problema real:

1. **Preocupado.** Ves el problema pero aún no sabes cómo abordarlo.
2. **Pensando.** Lo descompones, reúnes información, comparas opciones.
3. **Eureka.** Aparece una solución candidata. Listo para diseñarla y probarla.

Programar sigue exactamente ese arco. Nuestro trabajo es hacerlo **repetible** en lugar de un accidente afortunado.

---

## Qué cuenta como "problema"

No toda pregunta es un problema que resuelvas igual. Dos distinciones útiles:

### Bien definido vs mal definido

- **Bien definido** — entradas, meta y restricciones claras. *Calcular el área de un rectángulo dado ancho y alto.*
- **Mal definido** — meta difusa, datos incompletos, éxito subjetivo. *Hacer que la app se sienta más rápida.*

La mayoría de los problemas reales empiezan mal definidos. Tu primera tarea suele ser **convertir un problema mal definido en uno bien definido**.

### Tratable vs intratable

- **Tratable** — existe un algoritmo razonable que corre en tiempo razonable.
- **Intratable** — los algoritmos conocidos requieren tiempo o recursos desmedidos al crecer la entrada (el viajante de comercio con 1000 ciudades, por ejemplo).

Para problemas intratables solemos aceptar soluciones "suficientemente buenas" (heurísticas, aproximaciones) en vez de perfectas.

---

## Los cuatro pilares del Pensamiento Computacional

Antes del proceso de 7 pasos, conoce las cuatro jugadas mentales que quien piensa computacionalmente usa todo el tiempo. Las vas a aplicar en cada paso que sigue.

### <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/puzzle-piece.svg" width="20" height="20" alt=""> Descomposición

<img src="assets/CT-01.png" alt="Doodle: un problema enredado partiéndose en piezas más pequeñas y ordenadas" width="420">

Dividir un problema grande y aterrador en piezas pequeñas y manejables.

> Organizar un grupo de estudio de 10 personas → (a) encuestar horarios, (b) encontrar traslapes, (c) elegir sala, (d) decidir qué estudiar, (e) compartir material.

### <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/shapes.svg" width="20" height="20" alt=""> Reconocimiento de patrones

<img src="assets/CT-02.png" alt="Doodle: formas mezcladas a la izquierda siendo agrupadas por tipo a la derecha" width="420">

Detectar similitudes — con problemas pasados o dentro del problema actual.

> Contar vocales en una oración y contar consonantes usan la *misma* estructura de ciclo; solo cambia la condición.

### <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/wand-magic-sparkles.svg" width="20" height="20" alt=""> Abstracción

<img src="assets/CT-03.png" alt="Doodle: una taza de café detallada simplificándose en etapas a un ícono mínimo" width="420">

Quedarse solo con lo que importa; ignorar el resto.

> Una app de rutas de autobús no necesita modelar el color del autobús ni el nombre del chofer — solo paradas, horarios y capacidad.

### <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/list-ol.svg" width="20" height="20" alt=""> Pensamiento algorítmico

<img src="assets/CT-04.png" alt="Doodle: tarjeta de receta titulada ALGORITMO con pasos numerados e iconos pequeños" width="420">

Describir la solución como una secuencia clara y repetible de pasos.

> Una receta para "encontrar el número más grande en una lista" funciona igual con 5 elementos que con 5 millones.

**Cada problema que resuelves usa los cuatro pilares**, a menudo en ciclos. Descompones, detectas un patrón, abstraes la realidad desordenada, diseñas un algoritmo — y vuelves a descomponer cualquier paso que aún sea demasiado grande.

---

## El proceso de 7 pasos

Un proceso estructurado para pasar de "estoy atorado" a "aquí hay una solución que puedo defender".

### <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/magnifying-glass.svg" width="18" height="18" alt=""> 1. Identificar y definir el problema

- Enuncia el problema en **una oración**. Si no puedes, aún no lo entiendes.
- Divídelo en partes manejables (descomposición).
- Encuentra la **causa principal**, no solo los síntomas.
- Escribe: **dado** qué, **encontrar** qué, **sujeto a** qué restricciones.

> **Antipatrón:** saltar directo a "uso Python con base de datos" sin saber qué debe hacer el programa.

### <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/box-archive.svg" width="18" height="18" alt=""> 2. Reunir información

- Investiga lo que ya se sabe. ¿Alguien lo ha resuelto antes?
- Recolecta datos representativos (entradas de muestra y salidas esperadas).
- Habla con quienes han vivido la situación — usuarios, colegas, mentores.
- Revisa restricciones que pudiste pasar por alto: presupuesto, tiempo, hardware, legales.

### <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/chart-line.svg" width="18" height="18" alt=""> 3. Analizar el problema

- Examina todo lo reunido. ¿Qué forma tiene el problema?
- Busca **patrones**, **restricciones** y **causas raíz**.
- Identifica casos borde — las entradas raras que rompen soluciones ingenuas.
- Usa herramientas cuando ayuden: causa-efecto, FODA, 5-porqués.

### <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lightbulb.svg" width="18" height="18" alt=""> 4. Desarrollar posibles soluciones

- Genera **varias** alternativas. La primera idea rara vez es la mejor.
- Combina enfoques creativos y estructurados.
- Para cada candidata, esboza cómo maneja las entradas principales y los casos borde.
- No evalúes aún — solo genera.

### <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scale-balanced.svg" width="18" height="18" alt=""> 5. Evaluar las soluciones

- Compara pros y contras.
- Considera: factibilidad, costo, tiempo de construcción, mantenibilidad, impacto en usuarios.
- Considera riesgos — ¿qué se rompe si el supuesto X es falso?
- Elige la **más prometedora** (no necesariamente la más brillante).

### <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/hammer.svg" width="18" height="18" alt=""> 6. Implementar la solución

- Planea primero, escribe después. Muchos saltan este paso y pagan luego.
- Asigna responsabilidades si es trabajo en equipo.
- Define cronograma con hitos.
- En programación, **aquí diseñas el algoritmo** (módulos siguientes: diagramas de flujo y pseudocódigo).

### <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/arrows-rotate.svg" width="18" height="18" alt=""> 7. Monitorear y ajustar

- ¿Funciona en entradas reales, no solo en el demo?
- Detecta errores. Recoge retroalimentación.
- Ajusta cuando sea necesario. Acepta que la primera solución rara vez es la final.
- Documenta lo que aprendiste para la próxima.

---

## Ejemplo trabajado — organizar un grupo de estudio

Caminemos los 7 pasos de punta a punta en un escenario deliberadamente no técnico. **La misma estructura aplica a problemas de software.**

### Paso 1 · Identificar y definir

> *"Cinco compañeros y yo queremos estudiar juntos para el examen final, pero los horarios y temas favoritos difieren. ¿Cómo lo logramos?"*

Oración: **"Planear una sesión de estudio que entre en la agenda de todos, cubra todos los temas del examen y deje a la gente sintiéndose preparada."**

Descomposición:

- (a) Tiempos libres de cada quien.
- (b) Temas a cubrir.
- (c) Lugar de reunión.
- (d) Material (apuntes, problemas de práctica).
- (e) Forma de correr la sesión para que la gente aprenda, no solo se siente.

### Paso 2 · Reunir información

- Encuesta de horarios de los próximos 7 días.
- Lista de temas del temario oficial.
- Pregunta en qué tema cada quien se siente más débil (para emparejar fuerte + débil).
- Revisa salas disponibles en la biblioteca.

### Paso 3 · Analizar

- Patrón: 3 de 6 personas comparten miércoles y viernes por la tarde. Los otros 3 comparten martes y jueves.
- Restricción: el examen es el lunes — solo una semana.
- Causa raíz de "los horarios son imposibles": buscamos un único slot para todos en vez de dos sesiones más chicas.

### Paso 4 · Desarrollar soluciones

1. **Una sesión grande de 6 personas** en el único traslape (domingo 6 p. m.).
2. **Dos sesiones más chicas** (miércoles + jueves) cubriendo mitades del temario.
3. **Estudio asíncrono** — compartir apuntes y solo reunirse domingo para Q&A.
4. **Parejas rotativas** — cada persona enseña un tema a una pareja.

### Paso 5 · Evaluar

| Opción | Pros | Contras |
|--------|------|---------|
| 1 · Sesión grande | Todos juntos | 2 h no alcanzan para 6 temas |
| 2 · Dos sesiones | Más tiempo por tema | Riesgo de perder material entre ellas |
| 3 · Asíncrono + Q&A | Flexibilidad máxima | Los más débiles necesitan ayuda en vivo |
| 4 · Parejas rotativas | Aprendizaje activo, todos enseñan | Más coordinación |

Elegimos **opción 2** (sesiones separadas) con pedacitos de la 4 (una persona lidera cada tema en su sesión).

### Paso 6 · Implementar

- Mié 6–9 p. m., biblioteca sala 3 — temas A, B, C, líderes asignados.
- Jue 6–9 p. m., biblioteca sala 3 — temas D, E, F, líderes asignados.
- Documento compartido con apuntes, enlaces, exámenes anteriores.
- Dom 5 p. m. — 1 h de repaso conjunto + Q&A.

### Paso 7 · Monitorear y ajustar

- Mitad del miércoles: el tema B se alarga. Recortar el C y moverlo al Q&A del domingo.
- Viernes: 2 personas quedaron perdidas con el tema D. Moverlo al inicio del domingo.
- Después del examen: ¿qué funcionó? Escríbelo para el siguiente semestre.

---

## Escenarios de práctica

Corre los 7 pasos en papel para cada uno. Enfócate en los pasos 1–5; el paso 6 se desarrolla en los siguientes módulos.

- Tu laptop se volvió muy lenta de repente. Diagnostica por qué.
- 8 amigos quieren cenar en un restaurante, pero tienen 3 dietas distintas (vegetariana, sin gluten, alergia a nueces).
- A tu bici se le sale la cadena. Arréglalo.
- Empacar para un viaje de una semana con solo equipaje de mano y clima frío + cálido en el destino.
- Un formulario en línea acepta números de teléfono inválidos. Diseña cómo impedirlo.

---

## Errores comunes

- **Saltar a modo solución en el paso 1.** Si tu primer pensamiento es "uso base de datos", frena — aún no definiste el problema.
- **Saltarse el paso 2.** Investigar y hablar con usuarios toma tiempo pero ahorra muchísimo después.
- **Evaluar mientras haces brainstorm.** La crítica mata ideas. Genera primero, evalúa después.
- **Elegir la opción más llamativa.** Tecnología más nueva ≠ mejor solución. Soluciones aburridas que funcionan le ganan a soluciones emocionantes que no.
- **Sin paso 7.** Entregar no es terminar. Los problemas reales evolucionan; las soluciones requieren mantenimiento.

---

## Idea de cierre

La resolución de problemas es el **fundamento de todo lo demás** del curso. Algoritmos, diagramas de flujo, pseudocódigo y programación son solo herramientas para ejecutar la solución que diseñaste aquí. Si el diseño está mal, ningún código elegante lo salvará.

**Siguiente:** [Módulo 02 — Diagramas de flujo](02-flowcharts.md) — la primera forma formal de dibujar la solución que diseñaste.
