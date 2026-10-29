# Un puntero guarda una dirección

El operador & obtiene la dirección; * permite acceder al objeto apuntado. En el ejemplo, edad guarda 20 y ptr guarda la dirección de edad. Las direcciones de la lámina son ilustrativas.

| Expresión | Qué pide | En este ejemplo |
| --- | --- | --- |
| edad | El valor de edad | 20 |
| &edad | La dirección de edad | 0x1000 |
| ptr | La dirección guardada | 0x1000 |
| *ptr | El valor del objeto apuntado | 20 |

Después de inicializar ptr, ptr == &edad y *ptr == edad. Al declarar, * indica que ptr es un puntero a int. En una expresión, *ptr designa a edad: permite leerla o modificarla. Al ejecutar *ptr = 25, cambia edad; la dirección guardada en ptr se conserva.

Como una casa: edad es el contenido; &edad es la dirección; ptr es la nota con esa dirección; *ptr permite acceder al contenido.

Un puntero debe apuntar a un objeto válido para leer o escribir mediante *. No desreferencies nullptr ni un puntero sin inicializar.

# char* apunta a un carácter de la cadena

El arreglo guarda caracteres; el puntero permite acceder a ellos. En la inicialización char* ptr = matricula, matricula se convierte en un puntero a su primer elemento: ptr == &matricula[0]. El arreglo y el puntero son objetos distintos.

El carácter nulo marca el final de la cadena. El arreglo tiene 12 elementos; 6 guardan dígitos y los otros 6 se inicializan en cero. cout trata char* como una cadena y lee hasta el carácter nulo. *ptr es solo el primer carácter. La conversión a const void* permite mostrar la dirección.

El getter devuelve un puntero al primer carácter; no se copia el arreglo. const char* impide modificar los caracteres mediante el puntero devuelto. El const después de () indica un método que no modifica el estado del objeto.

El puntero devuelto puede usarse mientras e exista y su almacenamiento siga siendo válido. Al destruir e, p queda colgante. Antes de imprimir una cadena, debe existir un carácter nulo accesible dentro del almacenamiento válido.
