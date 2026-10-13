# Desarrollo de aplicaciones móviles · React Native

El curso comparte 17 sesiones, objetivos conceptuales y evaluación con la edición SwiftUI. React Native aplica esos conceptos a Android e iOS. La edición SwiftUI construye para iOS y estudia Android mediante equivalencias de concepto.

Las presentaciones de cada idioma están en `es/` y `en/`. El encuadre usa `w01.0`; las sesiones usan `w01` a `w17`. Los temarios y ejercicios tienen versiones en español e inglés. Los fragmentos de código completos de las tarjetas están en `labs/samples/`; deben integrarse en el contexto indicado.

`plan.json` contiene la síntesis compartida. Las propuestas originales se conservan en `propuestas/`. El anexo fechado registra herramientas y compatibilidad. Las comprobaciones de sintaxis y dominio no sustituyen la construcción de una app completa ni sus pruebas en dispositivos.

Para compilar desde `ppts/`, usa el entorno Python 3.14 del repositorio:

```bash
../.venv/bin/python -m kit.preflight react-native
../.venv/bin/python -m kit.build react-native
../.venv/bin/python -m kit.lint react-native
../.venv/bin/python -m kit.sizes react-native
../.venv/bin/python -m kit.pdf react-native -o ../pdf --jobs 3
```
