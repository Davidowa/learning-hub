# Validación del proyecto de rastreo de imágenes

El controlador pasó 24 comprobaciones con sustitutos locales de las clases de Unity. Los cuatro scripts se analizaron para Editor y Android con sintaxis C# 9. Las comprobaciones cubren la coincidencia por nombre, el rechazo de nombres desconocidos, la creación al recuperar Tracking, la ocultación en Limited o None y la conservación de otras figuras al eliminar una imagen.

También se revisan la ausencia de duplicados, la limpieza al desactivar el controlador, la recuperación al reactivarlo y los mensajes ante campos sin asignar. Estas comprobaciones de lógica no ejecutan el motor de Unity ni el proveedor ARCore.

Las firmas de los eventos y de la biblioteca se contrastaron con AR Foundation 6.3.5. La configuración URP se contrastó con el código oficial de URP 17.3.0, asociado a Unity 6.3. El paquete registra Unity 6000.3.27f1.

Los marcadores conservan identificadores estables y un ancho de referencia de 0.16 m. La herramienta arcoreimg de ARCore 6.3.5 para macOS devolvió `bad CPU type in executable` porque es x86_64. No se obtuvo una puntuación de calidad de las imágenes.

Unity Editor no está instalado en este Mac. Permanecen pendientes la importación de los assets, la generación de la configuración URP y XR, la compilación, la vista previa, el reconocimiento en el celular y la compilación Android. No se generó un APK.
