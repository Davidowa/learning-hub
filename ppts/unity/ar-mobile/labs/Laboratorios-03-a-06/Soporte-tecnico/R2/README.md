# Autoría de las guías R2 y la infografía

Estos scripts se conservan para el docente. Los proyectos del alumno no necesitan ejecutarlos para completar la actividad.

`render_guias.py` toma como fuente el Guia.md de cada base, genera los cuatro PDF, sincroniza las guías de base y solución y actualiza los ZIP de Entregas. Comprueba que los demás archivos de los ZIP no cambien. La fuente de los cambios futuros es el Markdown del proyecto; los PDF son sus exportaciones.

Los scripts utilizan Python con reportlab y pdfplumber y las fuentes Arial, Georgia y Consolas instaladas en Windows. Desde esta carpeta se pueden ejecutar los siguientes comandos:

```powershell
python render_guias.py
python infografia_pasos.py
```

El segundo comando genera el PDF de la infografía y guarda su texto de trabajo en la carpeta local work, excluida de Git. Para actualizar las vistas previas se utiliza Poppler desde la raíz Laboratorios-03-a-06:

```powershell
pdftoppm -scale-to 1500 -png Infografia/OnGUI-y-Canvas-Learning-Hub.pdf Infografia/OnGUI-y-Canvas-Learning-Hub
```

Después de modificar texto o diseño se revisan las páginas renderizadas. Una exportación sin errores no demuestra que la distribución del texto sea correcta. Los hashes de paquetes se actualizan al volver a generar las entregas.

`LabContentMenuAudit.cs` es una prueba de preparación para una copia temporal del proyecto. Su resultado se conserva en LabContent-audit.txt. No se añade a Assets del alumno ni se utiliza para construir su escena. El registro diferencia el reconocimiento del comando de menú y la creación directa del asset en modo batch.

`Blackboard-R2.json` conserva los ocho registros de actividad y los ocho de solución verificados durante la publicación. Es una evidencia de esa revisión, no una consulta del estado actual de Blackboard.
