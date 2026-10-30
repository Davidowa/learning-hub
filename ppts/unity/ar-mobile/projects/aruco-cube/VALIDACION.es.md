# Validación de la práctica 5

Se ejecutaron 34 comprobaciones con .NET 10 sobre la lógica independiente de Unity. Los 5 archivos C# también pasaron el análisis de sintaxis C# 9 con símbolos UNITY_EDITOR y UNITY_ANDROID. El análisis de sintaxis no equivale a compilar las API de Unity.

El detector se evaluó con 13 imágenes sintéticas de 640 × 480 píxeles. Reconoció el ID 23 en cuatro giros, perspectiva, inclinación, desenfoque, ruido y menor iluminación; rechazó otro ID, una imagen reflejada, una oclusión y una imagen vacía. Las esquinas positivas mantuvieron el orden canónico con error promedio inferior a 7 píxeles respecto de las coordenadas de referencia. Las pruebas geométricas verificaron profundidad métrica, escala física, orientación, pose oblicua, rechazo de geometría degenerada e inversión UV con rotación y recorte.

Estos casos no miden precisión o tasa de fallos en escenas reales ni incluyen una evaluación amplia de falsos positivos. El detector reconoce un único ID con coincidencia exacta y no reemplaza la implementación completa de OpenCV. Deben verificarse sobre el celular la conversión de imagen CPU a pantalla, la distorsión, el desfase temporal, la estabilidad y el costo de procesamiento.

No se encontró un Unity Editor instalado en el equipo de preparación. Permanecen pendientes la importación y compilación con Unity 6000.3.27f1, la interfaz renderizada, Project Validation, Build And Run y las pruebas de cámara y rastreo en Android. Las versiones y firmas utilizadas se contrastaron con el código oficial de los paquetes, pero esa revisión no sustituye una compilación.

Los casos de prueba y su programa se incluyen en Validation. Las pruebas físicas y los criterios de observación están descritos paso a paso en Guia.es.md y Guia.es.pdf.
