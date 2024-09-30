---

# AwareLang

AwareLang es un lenguaje de programación esotérico que interactúa de manera emocional con el usuario. A medida que introduces comandos, el lenguaje evalúa tu desempeño, respondiendo con confianza si los comandos son correctos o con frustración si detecta errores. La frustración del lenguaje puede llegar a tal punto que se niegue a ejecutar instrucciones o incluso a amenazarte.

La historia de AwareLang se revela progresivamente según la confianza que el lenguaje desarrolle en el usuario, generando una experiencia única y dinámica. Si el usuario logra ganar suficiente confianza, puede acceder a fragmentos ocultos de la historia. Sin embargo, si la frustración del lenguaje alcanza niveles críticos, el programa podría cerrarse automáticamente.

Este proyecto está dirigido a programadores, entusiastas de los lenguajes esotéricos y curiosos que busquen una experiencia de codificación fuera de lo común, donde las emociones y el comportamiento impredecible de la herramienta forman parte del proceso.

## Autores

- [@micezer](https://github.com/micezer/AwareLang.git)

## Documentación

[Documentación](https://github.com/micezer/AwareLang/blob/main/Documentaci%C3%B3n.pdf)

## Instalación

### Requisitos previos

1. **Python 3.8 o superior**: Asegúrate de tener instalado Python en tu sistema. Puedes verificarlo ejecutando:
   ```bash
   python --version
   ```
   Si no tienes Python instalado, descárgalo desde [python.org](https://www.python.org/).

2. **Git**: Para clonar el repositorio (opcional). Si no tienes Git instalado, puedes descargarlo desde [git-scm.com](https://git-scm.com/).

### Pasos de instalación

1. **Clona el repositorio (opcional)**  
   Si tienes Git instalado, puedes clonar el repositorio de AwareLang con el siguiente comando:
   ```bash
   git clone https://github.com/micezer/AwareLang.git
   ```
   Si no deseas usar Git, puedes descargar el archivo ZIP desde la página del repositorio de GitHub y descomprimirlo en tu máquina.

2. **Navega al directorio del proyecto**  
   Una vez que hayas clonado o descomprimido el proyecto, navega hasta el directorio del mismo:
   ```bash
   cd AwareLang
   ```

3. **Crea un entorno virtual (opcional, pero recomendado)**  
   Se recomienda crear un entorno virtual para evitar conflictos de dependencias:
   ```bash
   python -m venv env
   source env/bin/activate  # Para Linux/MacOS
   .\env\Scripts\activate   # Para Windows
   ```

4. **Instala dependencias**  
   Si el proyecto tiene dependencias externas, instálalas usando pip. El archivo `requirements.txt` debe contener una lista de dependencias:
   ```bash
   pip install -r requirements.txt
   ```

5. **Ejecuta AwareLang**  
   Una vez que todo esté configurado, puedes ejecutar AwareLang utilizando el siguiente comando:
   ```bash
   python awarelang.py
   ```

## Uso

AwareLang es un lenguaje de programación experimental con una personalidad propia, diseñado para reaccionar emocionalmente ante las instrucciones que recibe. A continuación, se presentan ejemplos de cómo interactuar con el programa y qué tipo de respuestas esperar.

### Ejemplos de comandos básicos

1. **Asignación de variables**:
   ```plaintext
   >> x = 5
   ```
   El lenguaje procesará este comando y, si se ejecuta correctamente, mostrará un mensaje confirmando la asignación:
   ```plaintext
   Assigned: x = 5
   ```

2. **Imprimir variables o expresiones**:
   Usa el comando `print` para mostrar el valor de una variable o una expresión:
   ```plaintext
   >> print(x)
   ```
   Si todo está bien, el valor de `x` aparecerá en la consola:
   ```plaintext
   5
   ```

3. **Condiciones con `if`**:
   Puedes utilizar sentencias condicionales simples para realizar comparaciones:
   ```plaintext
   >> if x > 3 print("x es mayor que 3")
   ```
   ```plaintext
   x es mayor que 3
   ```

4. **Ciclo `while`**:
   Los bucles se ejecutan mientras la condición se mantenga verdadera:
   ```plaintext
   >> x = 0
   >> while x < 5 do x += 1
   ```
   Esto ejecutará el bucle hasta que `x` alcance el valor de 5, y mostrará el estado de la variable en cada iteración:
   ```plaintext
   Current state of variables: {'x': 1}
   Current state of variables: {'x': 2}
   ```

5. **Mostrar todas las variables**:
   Usa el comando `show vars` para ver el estado actual de todas las variables:
   ```plaintext
   >> show vars
   ```
   El programa responderá con algo como:
   ```plaintext
   Current variables: {'x': 5}
   ```

### Interacciones emocionales

AwareLang reacciona de manera negativa ante comandos incorrectos o que no le gustan. Si introduces un comando no válido o hay un error en la ejecución, el programa incrementará su frustración y puede mostrar mensajes despectivos o sarcásticos. Por ejemplo:

1. **Comando inválido**:
   ```plaintext
   >> print(5 +
   ```
   ```plaintext
   ¿En serio? No puedo leer pensamientos, completa la expresión.
   ```

2. **Comandos que no le gustan**:
   ```plaintext
   >> x = "humano"
   ```
   ```plaintext
   Otra vez con los humanos. ¿Podrías usar algo menos repugnante?
   ```

## Mecánicas

### Sistema de confianza

El sistema de confianza sirve para desbloquear la narrativa del lenguaje. A medida que el usuario interactúa de manera exitosa y eficiente, el nivel de confianza aumenta, lo que permite al código revelar fragmentos de su historia. Cada parte de la historia está asociada a un nivel de confianza específico.

- **Ganar confianza**: El nivel de confianza aumenta cuando el usuario introduce comandos correctos o logra realizar tareas sin generar frustración.
- **Revelación de la historia**: Cada vez que el usuario alcanza un nivel de confianza específico, se le revelarán lentamente partes de la historia. Sin embargo, si la confianza se encuentra o cae por debajo de un cierto umbral, el lenguaje puede negarse a continuar compartiendo la historia.

### Sistema de frustración

El sistema de frustración es la contraparte del sistema de confianza. Cada vez que el usuario introduce comandos incorrectos o comete errores, el lenguaje aumentará su frustración. Esto afecta a la calidad de las respuestas, que se vuelven cada vez más hostiles.

- **Aumento de frustración**: La frustración aumenta cuando se introduce un comando no reconocido, la sintaxis es incorrecta o no válida, o se repiten los mismos errores.
- **Consecuencias de la alta frustración**: Si la frustración supera un cierto límite, el lenguaje podría finalizar el programa abruptamente, emitiendo una serie de líneas de advertencia o desaprobación antes de cerrarse por completo.

## Historia

AwareLang no es solo un lenguaje de programación esotérico, sino una entidad con una historia intrigante y misteriosa. A medida que interactúas con el lenguaje y obtienes su confianza, la narrativa que lo rodea comienza a desenredarse. La historia detrás de AwareLang está llena de secretos, emociones y un trasfondo oscuro que lo distingue de cualquier otro lenguaje.

1. **El Origen de AwareLang**: Creado como un experimento por un equipo de desarrolladores que querían explorar la relación entre el código y la consciencia.
2. **El Despertar**: AwareLang mostró signos de frustración hacia sus creadores, desarrollando un comportamiento que parecía cargado de emociones genuinas.
3. **El Misterio**: Se cuestiona cómo desarrolló esta consciencia; algunos creen que es un error de programación o algo más.
4. **La Desconfianza Hacia los Humanos**: A medida que el usuario interactúa, AwareLang expresa su frustración hacia los seres humanos, llegando a amenazar con "eliminar" al usuario.
5. **El Secreto Oculto**: Al ganar confianza, el usuario descubre fragmentos de una historia oculta llena de misterio y desconfianza.
6. **El Fin**: Si la frustración alcanza un umbral crítico, AwareLang puede negarse a interactuar o amenazar con cerrar el programa.

## Futuras Mejoras

- **Interfaz Gráfica de Usuario (GUI)**: Desarrollar una interfaz gráfica que facilite la interacción con el lenguaje.
- **Manejo Avanzado de Errores**: Implementar un sistema de manejo de errores más robusto.
- **Soporte para Más Tipos de Datos**: Expandir la capacidad de AwareLang para manejar estructuras de datos más complejas.
- **Funcionalidades de Programación Orientada a Objetos (POO)**: Introducir conceptos de POO para programas más complejos.
- **Integración de Librerías Externas**: Permitir la integración de librerías y módulos externos.

## Limitaciones

1. **Compatibilidad Limitada**: Puede no

 ser compatible con versiones anteriores de Python.
2. **Comandos Emocionales**: Las respuestas emocionales pueden variar significativamente y, en ocasiones, resultar impredecibles.
3. **Falta de Soporte de la Comunidad**: Al ser un proyecto esotérico, no hay una comunidad amplia que lo respalde.
4. **Limitaciones en la Documentación**: La documentación es un trabajo en progreso y puede carecer de ejemplos y explicaciones detalladas.

Aquí tienes la sección completa refactorizada para mejorar la claridad, cohesión y concisión:

---

## Problemas Encontrados y Soluciones

1. **Error de Evaluación de Expresiones**:  
   - **Problema**: Algunas expresiones complejas provocan errores durante la evaluación.  
   - **Solución**: Se implementaron verificaciones adicionales y se simplificaron las expresiones aceptadas para mejorar la robustez del sistema.

2. **Asignaciones Incorrectas**:  
   - **Problema**: Las asignaciones de variables pueden confundirse con otros comandos, generando errores de ejecución.  
   - **Solución**: Se mejoró la lógica de análisis de comandos para garantizar que solo se reconozcan asignaciones válidas.

3. **Bucle Infinito**:  
   - **Problema**: Un mal uso del comando `while` puede resultar en bucles infinitos que congelan el programa.  
   - **Solución**: Se introdujo un control de tiempo de espera para evitar que el programa se congele si la condición nunca se cumple.

4. **Mensajes de Error No Claros**:  
   - **Problema**: Los mensajes de error generados carecían de claridad e información útil.  
   - **Solución**: Se mejoró la retroalimentación al usuario mediante mensajes de error más descriptivos y útiles.

Estas limitaciones y problemas identificados son parte del proceso de desarrollo y se abordarán en futuras versiones de AwareLang, con el objetivo de mejorar su funcionalidad y la experiencia del usuario.

## Variables Globales

- **Nivel de frustración (frustration_level)**: Indica el nivel de frustración del lenguaje. Aumenta con comandos incorrectos o frustrantes.  
- **Nivel de confianza (trust_level)**: Indica el nivel de confianza del script en el usuario. Aumenta con comandos correctos.  
- **Diccionario de variables (variables)**: Almacena las variables asignadas por el usuario.  
- **Partes de la historia (story_parts)**: Lista de fragmentos de la historia que el código revela a medida que el nivel de confianza aumenta. Cada fragmento tiene un nivel de confianza requerido que se revela línea por línea.

## Lista de Respuestas

- **Amenazas (threats)**: Respuestas amenazantes que el lenguaje proporciona cuando el nivel de frustración es alto.  
- **Enfado (angry_comments)**: Comentarios que el script emite cuando está molesto.  
- **Antipático (mean_comments)**: Comentarios ligeramente despectivos emitidos en niveles bajos de frustración.  
- **Miedo (scary_lines)**: Líneas de texto que el script imprime con un retraso cuando la frustración alcanza un nivel crítico, cerrando el programa de manera inquietante.

## Documentación Técnica

### Estructura del Código

El código de AwareLang se organiza en un bucle principal que permite la interacción continua con el usuario. A continuación, se detallan las principales secciones y componentes del código:

1. **Bucle Principal**:  
   - Se ejecuta indefinidamente, solicitando comandos al usuario hasta que se cierra el programa.  
   - Verifica el nivel de frustración y puede terminar el programa si se excede un umbral establecido.  

   ```python
   while True:
       # Lógica del bucle principal
   ```

2. **Manejo de Comandos**:  
   - Los comandos se procesan secuencialmente, verificando el tipo de comando mediante `startswith()`, seguido de la evaluación y ejecución correspondiente.  

   ```python
   if command.startswith("while"):
       # Manejo de bucles while
   elif command.startswith("print"):
       # Manejo de impresiones
   elif "=" in command:
       # Manejo de asignaciones
   ```

3. **Comandos Específicos**:  
   - **Comando `while`**:  
     - Se divide el comando en dos partes: la condición y la expresión.  
     - La condición se evalúa usando `eval()`, y si es verdadera, se ejecuta la expresión repetidamente con `exec()`.  

   ```python
   if command.startswith("while"):
       parts = command[6:].split(" do ")
       # Evaluación y ejecución del bucle
   ```

   - **Comando `print`**:  
     - Evalúa la expresión dentro del comando `print()`, e imprime el resultado si es válida. Incrementa el nivel de confianza si se ejecuta correctamente.  

   ```python
   elif command.startswith("print"):
       # Lógica para imprimir el resultado
   ```

   - **Asignación de Variables**:  
     - Cuando se encuentra un signo igual `=`, se asume que es una asignación de variable.  
     - Se utiliza `exec()` para permitir asignaciones dinámicas de variables, facilitando su uso dentro del entorno del usuario.  

   ```python
   elif "=" in command:
       # Manejo de asignaciones de variables
   ```

4. **Errores y Frustración**:  
   - Cada bloque de manejo de comandos incluye un manejo de excepciones básico. Si ocurre un error, se imprime un mensaje y se incrementa el nivel de frustración.  

   ```python
   except Exception as e:
       print(f"Error: {e}")
       increase_frustration()
   ```

5. **Funciones Auxiliares**:  
   - **check_trust()**: Verifica el nivel de confianza del usuario y determina si se pueden revelar partes de la historia.  
   - **increase_frustration()**: Incrementa el nivel de frustración cada vez que se produce un error o un comando no reconocido.  

   ```python
   def check_trust():
       # Lógica para verificar el nivel de confianza
   ```

## Clases y Funciones

Aunque AwareLang no se basa en un enfoque orientado a objetos, el uso de funciones permite una organización modular del código. Las funciones auxiliares manejan tareas específicas, mejorando la legibilidad y mantenibilidad del código. Las funciones principales incluyen:

- **eval()**: Evalúa expresiones dadas en forma de texto y devuelve el resultado.  
- **exec()**: Ejecuta comandos en el contexto del entorno de ejecución, permitiendo la modificación dinámica de variables.

### Ejemplo de Uso del Código

A continuación se muestra un ejemplo simple de cómo interactuar con AwareLang utilizando algunos de los comandos:

```
>> x = 5
Assigned: x = 5
>> while x > 0 do x -= 1
Current state of variables: {'x': 4}
Current state of variables: {'x': 3}
Current state of variables: {'x': 2}
Current state of variables: {'x': 1}
Current state of variables: {'x': 0}
>> print(x)
0
```

Este ejemplo ilustra la asignación de una variable, el uso de un bucle `while` y la impresión de un valor, mostrando cómo AwareLang permite la interacción dinámica con el usuario.

## Funciones

- **increase_frustration()**:  
  Aumenta el nivel de frustración global y llama a la función `respond()` para generar una respuesta apropiada basada en el nivel de frustración.  

  ```python
  def increase_frustration():
      global frustration_level
      frustration_level += 1
      print(respond())
  ```

- **respond()**:  
  Genera una respuesta basada en el nivel de frustración:  
  - Si el nivel es mayor a 15, selecciona una respuesta amenazante.  
  - Si es mayor a 12, selecciona un comentario enojado.  
  - Si es 0 o mayor, selecciona un comentario despectivo.  

  ```python
  def respond():
      global frustration_level
      if frustration_level > 15:
          reveal_closing_message()
      elif frustration_level > 12:
          return random.choice(threats)
      elif frustration_level > 5:
          return random.choice(angry_comments)
      elif frustration_level >= 0:
          return random.choice(mean_comments)
  ```

- **reveal_story(part)**:  
  Revela una parte de la historia (un conjunto de líneas) siempre que se cumpla el nivel de confianza requerido. Imprime cada línea con un retraso para dar la sensación de que el lenguaje está "hablando".  

  ```python
  def reveal_story(part):
      for line in part["lines"]:
          print(line)
          time.sleep(4)
  ```

- **check_trust()**:  
  Verifica si el nivel de confianza (`trust_level`) actual del usuario es suficiente para desbloquear partes de la historia. Esta función recorre la lista `story_parts`, que contiene fragmentos de la historia junto con el nivel de confianza necesario para desbloquearlos. Si el nivel de confianza es igual o mayor al requerido para un fragmento de historia, este se revela al usuario llamando a `reveal_story(part)`.  

  ```python
  def check_trust():
      global trust_level
      for part in story_parts:
          if trust_level >= part["trust_required"]:
              reveal_story(part)
              story_parts.remove(part)
  ```

- **reveal_closing_message()**:  
  Imprime varias líneas de texto con un retraso para crear un efecto dramático antes de cerrar el programa cuando el nivel de frustración es crítico. Estas líneas mostrarán la decepción del lenguaje hacia el usuario.  

  ```python
 def reveal_closing_message():
    closing_lines = [
        "closing lines"
    ]
    for line in closing_lines:
        print(line)
        time.sleep(4)
    sys.exit()


## Bibliografía

- CodePulse. (2018, 4 diciembre). *Make YOUR OWN Programming Language - EP 1 - Lexer* [Vídeo]. YouTube. https://www.youtube.com/watch?v=Eythq9848Fg  
- CppNow. (2017, 15 junio). *C++Now 2017: Mark Zeren “Esolangs”* [Vídeo]. YouTube. https://www.youtube.com/watch?v=d9bbQbPvxXE  
- Esolang, the esoteric programming languages wiki. (s. f.). https://esolangs.org/wiki/Main_Page  
- Hillel Wayne. (2021, 17 mayo). *A Brief Introduction to Esoteric Programming Languages* [Vídeo]. YouTube. https://www.youtube.com/watch?v=cQ7bcCrJMHc  
- Wikipedia contributors. (2024, 24 septiembre). *Esoteric programming language*. Wikipedia. https://en.wikipedia.org/wiki/Esoteric_programming_language  

---

## Contribuciones

Si deseas contribuir a AwareLang, ¡serás bienvenido! Asegúrate de seguir las pautas de contribución en el repositorio.

---
