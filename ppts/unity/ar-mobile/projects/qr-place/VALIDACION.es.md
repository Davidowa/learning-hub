# Validación de la práctica 6

Se ejecutaron 48 comprobaciones con .NET 10 sobre la lógica independiente de Unity. Los 9 archivos C# también pasaron el análisis de sintaxis C# 9 con símbolos UNITY_EDITOR y UNITY_ANDROID. El análisis de sintaxis no equivale a compilar las API de Unity.

ZXing decodificó ambos QR en cuatro giros y dos vistas con perspectiva y desenfoque. También leyó un QR desconocido y devolvió un resultado vacío ante una imagen sin código. Se verificaron los textos admitidos, el rechazo de otros textos y de un búfer inválido, así como las operaciones de colocación, selección, eliminación y conservación de identificadores del inventario.

El QR desconocido se decodifica como texto, pero la relación de contenido lo rechaza. Estas pruebas no prueban la adquisición de cámara, la pausa y reactivación del componente dentro de Unity, los permisos Android, la creación de anclajes ni la conservación del DLL durante una compilación IL2CPP.

No se encontró un Unity Editor instalado en el equipo de preparación. Permanecen pendientes la importación y compilación con Unity 6000.3.27f1, la interfaz renderizada, Project Validation, Build And Run y las pruebas de cámara y rastreo en Android. Las versiones y firmas utilizadas se contrastaron con el código oficial de los paquetes, pero esa revisión no sustituye una compilación.

Los casos de prueba y su programa se incluyen en Validation. Las pruebas físicas y los criterios de observación están descritos paso a paso en Guia.es.md y Guia.es.pdf.
