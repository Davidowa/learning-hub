# Infografías de C++ para P3

La serie contiene ocho infografías en español, con una hoja carta por tema y nombres preparados para Blackboard. Usa la paleta de C++ y la familia tipográfica de Learning Hub: azul 00599C, azul marino 0B1B3A, fondo F7F8FA y naranja para destacar una precisión. Los originales de Descargas se conservaron.

## Criterio de la serie

La audiencia son los estudiantes de Programación Avanzada que repasan los temas de P3. Cada hoja presenta una regla del lenguaje mediante un ejemplo, una comparación o un diagrama que se puede leer sin una explicación oral. La jerarquía visual y la reducción de elementos siguen el criterio de The Storyteller; el vocabulario y la redacción se revisaron con The Writer.

Las imágenes se generaron y corrigieron con la herramienta integrada ImageGen. Las versiones seleccionadas están en es. Las correcciones posteriores ajustaron las flechas de herencia, la representación de los subobjetos del diamante y el fragmento de salida formateada. El texto editable y los ejemplos completos se guardaron por separado para permitir su consulta y revisión.

## Orden y temas

| Número | Tema | Archivo original relacionado |
| --- | --- | --- |
| 01 | Clases y estructuras | Comparación Visual de Clases y Estructuras C++-2.png |
| 02 | Agregados y constructores | Comparación entre struct y class en C++-1.png |
| 03 | Acceso a miembros y this | Infografía de acceso a miembros en C++.png |
| 04 | Modificadores de acceso | Modificadores de acceso en C++.png |
| 05 | Lista de inicialización | C++_ Inicialización de Circle.png |
| 06 | Tipos de herencia | Infografía de Tipos de Herencia en C++.png |
| 07 | Funciones virtuales y override | C++ Virtual Functions Infographic.png |
| 08 | Polimorfismo con Shape | Infografía de funciones virtuales en C++.png |

La carpeta P3 contiene los PDF individuales y los PNG con los mismos nombres. Incluye un PDF de ocho páginas, un índice CSV con los nombres para mostrar en Blackboard y ocho ejemplos completos. Para imprimir, selecciona papel carta y tamaño real; cada página mide 8.5 × 11 pulgadas, equivalentes a 612 × 792 puntos.

Los PDF conservan las láminas como imágenes. El texto de consulta está disponible en lectura y los archivos C++ en ejemplos. Cada ejemplo es independiente y requiere C++20; sus bibliotecas e instrucciones de compilación están incluidas en el paquete.

## Revisión técnica

Los ocho ejemplos se compilaron con Apple clang 21.0.0, usando C++20 y las opciones Wall, Wextra, pedantic y Werror. Todos se ejecutaron y pasaron sus aserciones. También se verificaron siete rechazos de compilación esperados: acceso privado, acceso protegido a través de una referencia a la base, override con const incorrecto, asignación tardía de un const, una referencia sin inicializar, una clase abstracta instanciada y conversión ambigua en un diamante.

La salida del ejemplo 07 fue 78.54. El ejemplo 08 produjo 78.54, 24.00 y 9.00 en ese orden. El programa de validación está en fuentes/validar_ejemplos.py y genera un informe local al ejecutarse. Las transcripciones pasaron el lint formal de The Writer; se omitió un perfil de ensayo porque son infografías con tablas y fragmentos de código.

El checker de The Storyteller no reportó hallazgos en el manifiesto de contenido. Las láminas no son gráficas cuantitativas: la dirección de flechas, los textos, las tablas y la composición se revisaron visualmente. Los nueve PDF tienen páginas carta. La serie completa se renderizó para revisar márgenes y legibilidad.

## Referencias técnicas

- Borrador de C++20, acceso a miembros: https://timsong-cpp.github.io/cppwp/n4861/class.access
- Borrador de C++20, acceso protegido: https://timsong-cpp.github.io/cppwp/n4861/class.protected
- Borrador de C++20, agregados: https://timsong-cpp.github.io/cppwp/n4861/dcl.init.aggr
- Borrador de C++20, inicialización de bases y miembros: https://timsong-cpp.github.io/cppwp/n4861/class.base.init
- Borrador de C++20, funciones virtuales: https://timsong-cpp.github.io/cppwp/n4861/class.virtual
- Borrador de C++20, construcción y destrucción: https://timsong-cpp.github.io/cppwp/n4861/class.cdtor
- Borrador de C++20, herencia múltiple: https://timsong-cpp.github.io/cppwp/n4861/class.mi
- C++ Core Guidelines, diseño de clases y estructuras: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rc-struct
