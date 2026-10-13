# Fundamentos del comercio electrónico

El curso contiene un encuadre y 17 sesiones en español e inglés. El caso ficticio Molienda conecta catálogo, economía del pedido, experiencia de compra, pagos, operaciones, adquisición y retención. Los datos de práctica están en `labs/data/`; las maquetas con defectos intencionales están en `labs/fixtures/`.

`teaching-plan.json` contiene la edición que alimentó estas presentaciones. `plan.json` conserva la propuesta original. Los temarios y ejercicios tienen versiones en ambos idiomas. El documento de fuentes fechado distingue reglas vigentes de supuestos aritméticos: las comisiones y tasas del caso no son tarifas comerciales ni clasificaciones fiscales verificadas.

Para compilar desde `ppts/`, usa el entorno Python 3.14 del repositorio:

```bash
../.venv/bin/python -m kit.preflight ecommerce
../.venv/bin/python -m kit.build ecommerce
../.venv/bin/python -m kit.lint ecommerce
../.venv/bin/python -m kit.sizes ecommerce
../.venv/bin/python -m kit.pdf ecommerce -o ../pdf --jobs 3
```
