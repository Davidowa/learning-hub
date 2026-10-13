# Estado de la auditoría, semana por semana

## Continuación del 13 de octubre de 2026

Las 99 semanas que requerían continuación recibieron una revisión independiente: 33 de C++/C#/SQL, 32 de Office/VBA, incluida Office w09, y 34 de Python/Unity. Con las 68 ya revisadas, el registro original tiene **167 pares es/en revisados**. Se corrigieron los defectos confirmados y se conservaron las refutaciones y los límites de ejecución en los informes fechados.

Los informes actuales son `continuacion-2026-10-13-code-db.json`, `continuacion-2026-10-13-office.json` y `continuacion-2026-10-13-python-unity.json`. La segunda revisión de los 54 pares nuevos está en `continuacion-2026-10-13-newcourses-review.json`. Los 34 pares para Mac, 68 presentaciones, se derivan de Office/VBA y tienen una revisión de rutas, figuras y atajos.

La revisión no convierte las mediciones históricas sin datos originales en resultados reproducidos. También conserva las políticas docentes existentes. Office/VBA y Unity tienen límites de ejecución documentados; una revisión estática no equivale a probar todas las macros, escenas o dispositivos.

El manifiesto `continuacion-2026-10-13-entrega.json` registra la comprobación final de fuentes, PowerPoint y PDF. El bloque siguiente conserva el estado anterior para rastrear el relevo; sus conteos pendientes son históricos.

## Registro anterior a esta continuación

Cada semana es el par es/en. La auditoría tiene dos pasadas por semana:

1. **Auditoría**: un agente corre todo el código de las diapositivas (Python, g++, .NET 10,
   MariaDB), revisa referencias de línea, respuestas de quiz, trazas, afirmaciones técnicas,
   títulos que no describen su diapositiva, paridad es/en y registro, y corrige lo que confirma.
2. **Revisión**: otro agente intenta refutar cada corrección, revierte lo que no era defecto y
   hace una pasada propia.

| Curso | Revisada (las dos pasadas) | Solo auditada (falta la revisión) | Sin auditar |
|---|---|---|---|
| cpp | w00 w01 w02 w03 w04 w09 w10 w11 w12 w13 w14 w15 w16 | w05 w06 w07 w08 w17 | · |
| csharp | w01.0 w01.1 w09 w10 w11 | w02 w03 w04 w05 w06 w07 w08 w12 w13 w14 w15 w16 w17 | · |
| mysql | w01 w10 | w02 w03 w04 w05 w06 w07 w08 w09 w11 w12 w13 w14 w15 w16 w17 | · |
| office | · | w01 w02 w03 w04 w05 w06 w07 w08 w10 w11 w12 w13 w14 w15 w16 w17 | w09 |
| py-datos | w01.0 w01.1 w02 w03 w04 w05 w06 w07 w11 w12 w13 w14 w15.1 w15.2 w15.3 w16.1 | w08 w09 w10 w16.2 w17 | · |
| py-algoritmos | w01.0 w01.1 w02 w03 w04 w05 w06 w07 w08 w11 w12 w13 w14 w15.1 | w09 w10 w15.2 w15.3 w16.1 w16.2 w17 | · |
| py-poo | w01.0 w01.1 w01.2 w01.3 w01.4 w07 w08 w09 w10 w11 w12 | w01.5 w02 w03 w04 w05 w06 w13 w14 w15 w16 w17 | · |
| unity · ar-mobile | w01 w02 | w03 w04 w05 | · |
| unity · essentials | w04 w05 | w01 w02 w03 w06 | · |
| unity · vr | w01 | w02 w03 w04 w05 | · |
| vba | w10 w11 | w01 w02 w03 w04 w05 w06 w07 w08 w09 w12 w13 w14 w15 w16 w17 | · |

Total: 68 revisadas, 98 solo auditadas, 1 sin auditar, de 167.

## Revisiones que se detuvieron a medio camino

Estas revisiones estaban corriendo cuando se detuvo todo. Sus ediciones parciales se conservaron
porque los cuatro chequeos del kit quedan en cero, pero la revisión no terminó: vuelve a correrla.

cpp w05, cpp w06, cpp w17, csharp w02, csharp w03, csharp w12, csharp w13, mysql w02, mysql w04, mysql w11, mysql w13, office w01, office w10, office w11, py-algoritmos w09, py-algoritmos w15.2, py-algoritmos w15.3, py-datos w08, py-datos w09, py-datos w16.2, py-datos w17, py-poo w01.5, py-poo w03, py-poo w13, py-poo w14, unity ar-mobile-w03, unity ar-mobile-w04, unity essentials-w06, unity vr-w02, vba w01, vba w02, vba w12, vba w13

Excepciones, que se regresaron al último commit porque la edición a medias no pasaba los chequeos:

- **csharp w02 (es y en)**: la revisión encontró un defecto real y no alcanzó a acomodarlo. En la
  diapositiva del plan de impresora, el programa imprime "iniciando impresion" también después de
  "ABORTAR", y el MIENTRAS/while no tiene tope de vueltas. La corrección a medias está en
  `wip/csharp-w02-revision.diff`; dejó dos tarjetas de código de 16 y 18 líneas, que no caben. Hay
  que partir el ejemplo en dos diapositivas, en los dos idiomas.
- **office w09 (es y en)**: la auditoría no terminó en ninguno de sus dos intentos. Su avance está en
  `wip/office-w09-auditoria.diff` sin verificar (por ejemplo, cambia `?` por el carácter de
  reemplazo `�` en el ejemplo de codificación, que Courier New puede no dibujar). Hay que
  auditar w09 desde cero.
