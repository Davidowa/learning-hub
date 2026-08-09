# Sesión B · Cuadernos de Análisis de Datos (TIA502)

Corre en paralelo con la sesión A, que trabaja los cuadernos de COM102. Las dos
tocan `notebooks/kit/`. Lee la sección de convivencia antes de editar el kit.

## Encargo

Los 40 cuadernos ya están construidos, 20 por idioma, y en cero. **No hay que
escribir semanas nuevas.** El encargo es una revisión de fondo sobre lo que ya
existe.

## Lo primero, y es lo que importa

**Sacar de los cuadernos toda mención a que el alumno no es programador, o a
que la programación es cosa ajena que hay que justificarle.**

Esto ya se corrigió en los decks: la portada de la semana 1 decía "por qué un
alumno de negocios aprende a programar" y ahora dice "para qué sirve
programar". Los cuadernos no se han revisado con ese criterio.

Qué se busca, y por qué:

- **Etiquetar al lector.** "Alumno de negocios", "no eres programador", "aunque
  no te dediques a esto". Aunque sea cierto que el grupo viene de
  Empresariales, la frase le dice a alguien que esto no es para él justo
  cuando está empezando.
- **Pedir perdón por el contenido.** "No te preocupes, no es tan técnico", "esto
  suena complicado pero". Si hace falta disculparse por una explicación,
  el problema es la explicación.
- **Comparaciones que rebajan.** Está bien tender el puente desde Excel, ese es
  el argumento del curso y funciona. Lo que no sirve es usarlo para decir que
  lo de acá es lo difícil y lo de allá lo suyo.

El puente Excel a Python **se queda**. La semana `w01.1` existe para eso y es
buena. La diferencia entre tender un puente y pedir disculpas es de tono, y ahí
hace falta criterio, no un `grep`.

Empieza por buscar, pero no te quedes ahí:

```bash
grep -rin "no eres\|no son programador\|negocios\|business student\|no te preocupes\|aunque no" notebooks/kit/lessons/da_*.py
```

Después lee las celdas de texto de `w01.1`, `w01.0` y las de cierre de cada
cuaderno, que es donde este tono suele esconderse.

## Estado al arrancar

40 cuadernos desde 27 módulos de lección: los primeros emiten los dos idiomas
desde un solo archivo, los últimos se partieron en `_es` y `_en` al crecer.

```
notebooks/kit/lessons/da_*.py
notebooks/analisis-de-datos/{es,en}/   w01.1, w02..w14, w15.1-3, w16.1-2, w17
```

Los dos árboles tienen exactamente los mismos veinte archivos. Todo trackeado y
commiteado.

## Lo segundo, si queda tiempo

Los decks de TIA502 cambiaron esta semana y los cuadernos no se han alineado:

- **Colab es ahora el entorno principal**, no VS Code. El laboratorio de la
  semana 1 abre un cuaderno en lugar de instalar Python, y la rúbrica acepta
  "el cuaderno o el archivo". Revisa que los cuadernos no sigan pidiendo una
  instalación local.
- La tarea ya no pide activar DataCamp. El bono sigue existiendo en TIA502,
  eso no cambió, pero no es requisito de la primera entrega.

## Sin notas de orador

Los decks ya no llevan `notes:`. Se quitaron 309 bloques de los cuatro cursos.
Si un cuaderno se apoyaba en contexto que vivía ahí, ya no está.

## Convivencia con la sesión A

Las dos sesiones editan `notebooks/kit/`. Regla: **quien toque `nbkit.py`,
`build.py` o `verify.py` lo dice en su reporte antes de seguir.** Si necesitas
un cambio en el kit, hazlo mínimo y corre la verificación de los dos cursos
antes de darlo por bueno.

Los `lessons/*.py` no se pisan: los tuyos empiezan con `da_`, los de la sesión
A con `poo_`.

## Verificar

```bash
cd notebooks
python -m kit.build
python -m kit.verify
```

Cero errores en los dos idiomas. Y como esta sesión edita prosa y no código,
lee las celdas de texto después de construir: la verificación ejecuta celdas,
no juzga tono.

## Cuidado con esto

`notebooks/kit/lessons/da_w01_1.py` aparece como modificado en `git status` y
**no lo está**. El blob en disco y el del índice son el mismo hash; `git diff`
sale vacío. Es caché de fechas rancio. No lo reviertas.

## Al terminar

Reporta cuántas menciones encontraste y de qué tipo. Si alguna te pareció
defendible y la dejaste, dilo y por qué: el criterio importa más que el
conteo.
