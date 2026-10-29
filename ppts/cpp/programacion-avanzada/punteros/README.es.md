# Punteros en C++

La infografía reúne en dos láminas carta los temas de las ocho páginas de la guía original. La primera explica la dirección y el valor, los operadores & y *, la declaración de un puntero, la modificación del objeto apuntado, la analogía de la casa y un programa completo. La segunda conecta ese modelo con char*, los arreglos de caracteres, el terminador nulo y getMatricula().

El diseño sigue la serie de Learning Hub para C++: azul 00599C, azul marino 0B1B3A, fondo F7F8FA y el pato del proyecto. The Storyteller orientó la jerarquía y las explicaciones visuales. Las láminas se generaron con ImageGen integrado; los prompts están en fuentes. El PDF contiene las imágenes en dos páginas de 612 por 792 puntos. Los PNG se conservan por separado.

Se precisó que el getter devuelve un puntero al primer carácter del arreglo, sin copiarlo. La explicación distingue los dos calificadores const, la salida de char* y la salida de una dirección mediante const void*. Las direcciones de los diagramas son ilustrativas. El arreglo de 12 elementos conserva los seis dígitos y seis caracteres nulos de su inicialización.

Los ejemplos se compilaron con C++20, Wall, Wextra, pedantic y Werror. La validación comprobó los operadores, la modificación mediante el puntero, los 12 caracteres, la salida y el getter. Se revisaron ambas páginas renderizadas antes de subirlas a Blackboard. El original descargado se conserva en original.

## Referencias técnicas

- Operadores unarios: https://eel.is/c++draft/expr.unary.op
- Conversión de arreglo a puntero: https://eel.is/c++draft/conv.array
- Salida de caracteres y cadenas: https://eel.is/c++draft/ostream.inserters.character
- Duración de los objetos: https://eel.is/c++draft/basic.life
