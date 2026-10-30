# Validación del proyecto

La revisión corresponde a Unity 6.3 LTS, con AR Foundation y Google ARCore XR Plugin fijados en 6.3.5. El Editor registrado es 6000.3.27f1.

## Comprobaciones ejecutadas

La clase CaptureRegistry pasó 15 comprobaciones con .NET 10. Se revisaron la captura inicial, los impactos repetidos y la independencia entre imágenes. También se revisaron la recuperación del estado, el reinicio y el rechazo de identificadores inválidos.

Roslyn analizó los siete scripts de Unity con la sintaxis de C# 9. El análisis se ejecutó con los símbolos de Editor y Android por separado. Esta comprobación identifica errores de sintaxis; la compilación con las bibliotecas de Unity sigue pendiente.

Las versiones se consultaron en el registro oficial de paquetes de Unity, y las firmas utilizadas se contrastaron con el código oficial de AR Foundation 6.3.5, ARCore 6.3.5 y XR Plug-in Management 4.5.3.

El proyecto incluye una escena con referencia al script CaptureBootstrap y un marcador de prueba de 1024 por 1024 píxeles. La guía pasó el lint de the-writer sin hallazgos HIGH ni MEDIUM.

Se renderizaron y revisaron las cinco páginas de la guía y la hoja del marcador. El marcador ocupa un cuadrado de 16 cm en su PDF antes de cualquier ajuste de la impresora.

## Pruebas pendientes en Unity

Unity Editor no está instalado aquí. Permanecen pendientes la importación, la compilación en Unity, Play Mode, el renderizado de la escena y la compilación Android.

La cámara, el tamaño físico, el impacto y la persistencia deben probarse en un celular con ARCore. La guía contiene los pasos para revisar esos comportamientos antes de entregar una aplicación compilada.

Se intentó evaluar el marcador con arcoreimg del paquete oficial 6.3.5. Ese ejecutable macOS es x86_64 y este Mac es arm64 sin traducción disponible. El sistema respondió `bad CPU type in executable`, por lo que la calidad del marcador permanece sin medir.

El entregable contiene el proyecto fuente, la guía y el marcador. No se generó un APK. Las pruebas de rastreo en un celular siguen pendientes.

La configuración se convirtió a URP 17.3.0. Se revisaron el renderer feature del fondo de cámara y los shaders de materiales; la importación y el renderizado dentro de Unity siguen pendientes de prueba.
