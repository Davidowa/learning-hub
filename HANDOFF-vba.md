# Sesión C · TIA503, Análisis y Procesamiento de la Información (VBA)

Corre en paralelo con las sesiones A y B, que trabajan cuadernos de Colab en
`notebooks/`. Ustedes no comparten archivos con ellas: tú vives en `ppts/`, ellas
en `notebooks/`. Lo único común es que las tres cierran contra el mismo git.

## Encargo

Terminar el curso. Van diez semanas de diecisiete, en los dos idiomas.

**Faltan siete semanas por dos idiomas, catorce decks.** Sigue con la semana 11,
eventos, y de ahí en orden hasta la 17.

## Estado al arrancar

```
ppts/vba/analisis-y-procesamiento-de-la-informacion/
  HANDOFF.md              lee este primero, esta al dia
  syllabus-tia503.xlsx
  es/  w01 … w10  (.yaml + .pptx)
  en/  same
```

20 lecciones, preflight, build, lint y sizes en cero. Todo commiteado en
`6818abb`.

## Lo que cambió mientras no estabas, y te toca

**Las notas de orador ya no existen.** Se quitaron de los cuatro cursos, 309
bloques en 160 archivos. Tú ya habías quitado las tuyas, 22 bloques en 20
archivos, y esa decisión ahora es la del repositorio entero. **Los decks nuevos
se escriben sin `notes:`.**

Lo que se fue contigo, y que conviene tener presente al escribir de la 11 en
adelante: los minutos por bloque desaparecieron del repositorio. La procedencia
de cada `.bas` y las tablas de resultados verificados siguen en tu HANDOFF, así
que eso no se perdió.

**El verde de Excel cambió.** Ya no es `217346`. La paleta usa ahora los cuatro
verdes publicados, repartidos por la superficie donde cada uno pasa contraste:

| Verde | Dónde | Ratio |
|---|---|---|
| `107C41` | estructura en papel | 5.0, y 5.3 con blanco encima |
| `185C37` | `BLUE_DEEP` | 7.5 |
| `33C481` | palabras clave en el lienzo verde | 6.9 |
| `21A366` | sin uso | 3.0 en papel, no alcanza |

Tu HANDOFF ya lo trae con esas cifras. Los diez decks que ya escribiste se
reconstruyeron con la paleta nueva y quedaron en cero.

**Tres cambios en el kit**, todos ya en git:

1. `preflight` reporta línea y columna del error de YAML, en vez de
   `while parsing a block mapping`, que no servía para nada.
2. Chequeo nuevo: un valor que abre con comilla y no cierra. Rompe el parser y
   el mensaje viejo no ayudaba a encontrarlo.
3. El chequeo de `diagram` era demasiado estricto y marcaba láminas que se ven
   bien. `DIAGRAM_SLACK` recupera el redondeo; un cuarto renglón sigue cayendo.

## Reglas de la casa que aplican a lo que falta

Están completas en `ppts/HANDOFF.md` y en el HANDOFF de tu curso. Las que más se
rompen al escribir semanas nuevas:

- **El acento significa una cosa: esto es el riesgo.** `accent: true` va solo en
  una anotación de código cuyo rótulo ya lo diga. Nunca en una tarjeta de
  agenda, una fila de tabla ni una lista de herramientas.
- **Sin em dashes.** Comas, puntos, dos puntos, paréntesis. El separador de la
  casa es el punto medio.
- **Español mexicano neutro.** Sin vosotros, sin ordenador.
- **El subtítulo de portada tiene presupuesto: unos 130 caracteres.** Pasando de
  ahí se va a tres líneas y queda a 0.06" de la regla. Ningún chequeo se queja.
- **Muestra un grupo completo y en orden**, no solo los que confunden. Una tabla
  parcial enseña que el resto no existe.
- **Nada de rutas de instalación local si el curso no las exige.** Revisa qué
  entorno asume tu syllabus antes de pedir una captura de terminal.

## Verificar

```bash
cd ppts
python -m kit.preflight vba
python -m kit.build      vba
python -m kit.lint       vba
python -m kit.sizes      vba
python -m kit.preview    vba/analisis-y-procesamiento-de-la-informacion/es/w11.es.pptx w11 --cols 8
```

Los cuatro en cero. Y el paso cinco no es opcional: mira la hoja de contactos
antes de dar una semana por terminada. Los otros cuatro chequeos ven geometría;
solo mirar atrapa una lámina correcta que no dice nada. Borra el PNG después,
que se acumulan en la raíz de `ppts/`.

## Qué no tocar

`python/` y `cpp/` están terminados y revisados a la vista, los 122 decks. Si
crees que algo está mal ahí, dilo en tu reporte en lugar de editarlo.

`notebooks/` es de las sesiones A y B.

## Lo que dejaste pendiente contigo mismo

`AccessVBOM` sigue en 1, y el valor no existía antes de que lo pusieras. Bórralo
al terminar el curso, como dijiste.

## Al terminar

Reporta el estado y actualiza el HANDOFF de tu curso. Si algo del kit te
estorbó, dilo: `ppts/kit/` es territorio compartido y conviene que quede escrito
qué se cambió y por qué.
