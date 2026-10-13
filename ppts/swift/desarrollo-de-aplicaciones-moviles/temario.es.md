# Desarrollo de aplicaciones móviles

Este curso organiza conceptos, implementación y evidencia en 17 sesiones. Cada práctica usa únicamente conceptos de la sesión y de las anteriores. React Native construye para Android e iOS. SwiftUI construye para iOS y estudia Android mediante equivalencias de concepto.

## Evaluación

| Componente | Peso | Entrega |
|---|---:|---|
| Parcial 1 | 20 % | w08 |
| Parcial 2 | 20 % | w13 |
| Proyecto | 20 % | w16 |
| Examen final | 20 % | w17 |
| Tareas y laboratorios | 20 % | w01-w16 |

## Sesiones

### 01. El dispositivo móvil como plataforma

- Tamaño, entrada, energía y conectividad delimitan el uso del dispositivo.
- Sensores e interrupciones afectan la experiencia y el diseño.
- Distingue UI nativa, renderizado propio y contenido web.
- Identifica lenguaje, SDK, compilador, simulador, firma y distribución.
- Define historias de usuario con criterios de aceptación.

Práctica: Mostrar la app en un simulador y en un dispositivo. Entrega un commit identificable y evidencia del resultado.

### 02. El lenguaje: tipos, valores y funciones

- Declara valores, tipos y funciones con contratos explícitos.
- Modela la ausencia con opcionales y uniones de tipos.
- Compara copiar valores con compartir referencias.
- Usa un conjunto cerrado para los estados del reporte.
- Aplica map, filter y reduce a colecciones.
- Prueba funciones puras con entradas y salidas conocidas.

Práctica: Modelar reportes y probar funciones puras. Entrega un commit identificable y evidencia del resultado.

### 03. Android e iOS por dentro

- Compara las capas del sistema, runtime y servicios.
- La app declara identidad, permisos y capacidades.
- Distingue una pantalla de un punto de entrada del sistema.
- Registra entradas y salidas del primer plano.
- Comprueba qué estado sobrevive a la terminación del proceso.

Práctica: Configurar identidad y registrar cambios de ciclo de vida. Entrega un commit identificable y evidencia del resultado.

### 04. Interfaz declarativa: componentes y layout

- Compón vistas pequeñas con responsabilidades visibles.
- Pasa datos de entrada mediante propiedades.
- El layout negocia espacio según contenido y restricciones.
- Usa controles del sistema para acciones y entrada.
- Compara una jerarquía de componentes con un flujo de pantallas.

Práctica: Componer una lista y una vista de detalle. Entrega un commit identificable y evidencia del resultado.

### 05. Estado e interacción

- Define qué vista es dueña del estado editable.
- Pasa estado y acciones sin duplicar la fuente de verdad.
- Modela campos válidos, vacíos y con error.
- La validación de dominio debe funcionar fuera de la vista.
- Comprueba el estado después de cada evento de usuario.

Práctica: Validar y guardar entradas del formulario. Entrega un commit identificable y evidencia del resultado.

### 06. Listas y navegación

- Asigna una identidad estable a cada registro.
- Carga listas sin construir todas las filas simultáneamente.
- Representa los destinos de navegación y sus argumentos.
- Confirma una acción destructiva y conserva contexto.
- Comprueba búsqueda, edición y regreso a la lista.

Práctica: Navegar entre lista y detalle con identidad estable. Entrega un commit identificable y evidencia del resultado.

### 07. Arquitectura de la app

- Separa presentación, dominio y acceso a datos.
- Expresa dependencias mediante interfaces o protocolos.
- Usa un repositorio en memoria para probar reglas.
- Distingue estado de pantalla y estado de negocio.
- Documenta una decisión arquitectónica y su costo.

Práctica: Separar el repositorio y probarlo con datos en memoria. Entrega un commit identificable y evidencia del resultado.

### 08. Red y asincronía

- HTTP, códigos de estado y JSON forman un contrato.
- Las operaciones asíncronas permiten atender interacción.
- Valida el contenido externo antes de usarlo.
- Representa carga, éxito, vacío y error con reintento.
- Cancela solicitudes al abandonar su contexto.

Práctica: Representar carga, éxito, vacío y error de una solicitud. Entrega un commit identificable y evidencia del resultado.

### 09. Persistencia local y trabajo sin conexión

- Elige almacenamiento según tamaño, estructura y sensibilidad.
- Una migración debe preservar los registros existentes.
- Modela altas y cambios pendientes de sincronización.
- Resuelve conflictos con una política explícita.
- Guarda credenciales en el almacenamiento seguro de la plataforma.

Práctica: Conservar datos después de reiniciar y migrar el esquema. Entrega un commit identificable y evidencia del resultado.

### 10. Cámara, fotos y archivos

- Distingue elegir una foto de capturar una nueva.
- Solicita permisos cuando la función los necesita.
- La negación debe dejar una ruta útil para el usuario.
- Separa referencias a archivos de los datos del dominio.
- Limpia archivos que dejan de pertenecer a un reporte.

Práctica: Adjuntar una foto y manejar permisos denegados. Entrega un commit identificable y evidencia del resultado.

### 11. Sensores y ubicación

- Expresa muestras con unidades y marcos de referencia.
- El intervalo de muestreo afecta ruido y energía.
- Comprueba una lectura contra una referencia conocida.
- Solicita ubicación con alcance proporcional a la función.
- Detén la suscripción cuando la pantalla deja de usarla.

Práctica: Registrar muestras con unidades y cancelar suscripciones. Entrega un commit identificable y evidencia del resultado.

### 12. Integración con el sistema

- Delega compartir y abrir enlaces al sistema.
- Valida argumentos de enlaces antes de navegar.
- Una notificación requiere contexto y control del usuario.
- El trabajo en segundo plano depende de un presupuesto del sistema.
- Guarda progreso para reintentos e interrupciones.
- Compara contratos equivalentes en Android e iOS.

Práctica: Abrir un reporte mediante un enlace validado. Entrega un commit identificable y evidencia del resultado.

### 13. Accesibilidad, idiomas y pantallas

- Cada control necesita nombre, rol y estado comprensibles.
- Comprueba el flujo completo con un lector de pantalla.
- Permite aumentar texto sin perder acciones.
- Separa mensajes traducibles de la lógica.
- Prueba layout en tamaños y orientaciones diferentes.

Práctica: Completar el flujo con lector de pantalla y dos idiomas. Entrega un commit identificable y evidencia del resultado.

### 14. Calidad: pruebas, depuración e integración continua

- Prueba reglas de negocio con funciones y repositorios falsos.
- Prueba componentes mediante acciones y resultados visibles.
- Verifica un flujo crítico de principio a fin.
- Una regresión necesita una prueba que fallaba antes de corregirla.
- La integración continua debe poder partir de un clon limpio.
- Mide rendimiento y accesibilidad además de compilar.

Práctica: Corregir una falla y agregar una prueba de regresión. Entrega un commit identificable y evidencia del resultado.

### 15. Seguridad, privacidad y publicación

- Mantén secretos fuera del código distribuido.
- Recolecta solo datos necesarios para una finalidad definida.
- Relaciona cada permiso con una función visible.
- Distingue firma, distribución de prueba y publicación.
- Documenta dependencias, versión y procedimientos de recuperación.
- Prepara evidencias de privacidad y mantenimiento.

Práctica: Preparar una compilación firmada para distribución de prueba. Entrega un commit identificable y evidencia del resultado.

### 16. Evaluar la siguiente herramienta

- Define el problema antes de elegir una dependencia.
- Compara funcionalidad, integración, mantenimiento y salida.
- Escribe criterios y una regla de suspensión del piloto.
- Prueba una función nativa pequeña sin trasladar todo el dominio.
- Conserva la opción de sustituir la herramienta.

Práctica: Evaluar una herramienta con un piloto reversible. Entrega un commit identificable y evidencia del resultado.

### 17. Examen final

- Ubica el alcance acumulativo y los criterios de calificación.
- Resuelve una falla mediante evidencia reproducible.
- Implementa una mejora usando contratos existentes.
- Defiende una decisión y sus límites.

Práctica: Resolver y defender un ticket de mantenimiento. Entrega un commit identificable y evidencia del resultado.

## Reglas de entrega

Declara herramientas de asistencia y conserva evidencia reproducible. Cada integrante debe explicar el trabajo. El enunciado de cada examen define los materiales permitidos.
