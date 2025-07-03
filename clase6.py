print("Nunca", "pares", "de", "aprender")
#La coma dentro de la función print se usa para separar varios argumentos.
# Al hacerlo, Python añade automáticamente un espacio entre los
# argumentos. Esto es diferente a concatenar cadenas con el operador +,
# que no añade espacios adicionales.

#Tambien se puede hacer de manera explicita con comillas
print("Nunca" + " " + "pares" + " " + "de" + " " + "aprender")

print("Nunca", "pares", "de", "aprender", sep=", ")
#El parámetro sep permite especificar cómo separar los elementos al imprimir.
# En este ejemplo, los elementos “Nunca”, “pares”, “de” y “aprender” se imprimirán
# con una coma y un espacio entre ellos, resultando en “Nunca, pares, de, aprender”.
# Puedes cambiar sep por cualquier cadena de caracteres que desees usar como separador.
print("Nunca", "pares", "de", "aprender", sep=", cham ")
    #Nunca, cham pares, cham de, cham aprender

print("Nunca", end=" ")
print("pares de aprender")
#El parámetro end cambia lo que se imprime al final de la llamada a print.
# En lugar de imprimir cada mensaje en una nueva línea, end="" asegura que
# “Nunca” y “pares” se impriman en la misma línea, resultando en “Nunca pares”.

frase = "Nunca pares de aprender"
author = "Platzi"
print(f"Frase: {frase}, Autor: {author}")
"""Las f-strings permiten insertar expresiones dentro de cadenas de texto.
Al anteponer una f a la cadena de texto, puedes incluir variables directamente
dentro de las llaves {}. En este ejemplo, frase y author se insertarán en la cadena,
resultando en “Frase: Nunca pares de aprender, Autor: Platzi”"""

frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase: {}, Autor: {}".format(frase, author))
"""El método format es otra forma de insertar valores en cadenas de texto.
Usando {} como marcadores de posición, puedes pasar los valores que quieres
insertar como argumentos de format. En este ejemplo, se imprimirá
“Frase: Nunca pares de aprender, Autor: Platzi”.Es una forma flexible y poderosa de
formatear cadenas, aunque las f-strings son más concisas."""

#Puedes controlar el formato de los números al imprimir. En este ejemplo,
# :.2f indica que el número debe mostrarse con dos decimales.
# Así, imprimirá “Valor: 3.14”, redondeando el número a dos decimales.
# Esto es especialmente útil cuando trabajas con datos numéricos y necesitas un
# formato específico.
valor = 3.14159
print("Valor: {:.2f}".format(valor))

#Los saltos de línea en Python se indican con la secuencia de escape \n. Por ejemplo,
# para imprimir “Hola\nmundo”, que aparecerá en dos líneas:
print("Hola\nmundo")

#Para imprimir una cadena que contenga comillas simples o dobles dentro de ellas,
# debes usar secuencias de escape para evitar confusiones con la sintaxis de Python.
# Por ejemplo, para imprimir la frase “Hola soy ‘Carli’”:
print('Hola soy \'Carli\'')

#Si necesitas imprimir una ruta de archivo en Windows, que incluya barras invertidas,
# también necesitarás usar secuencias de escape para evitar que Python interprete las
# barras invertidas como parte de secuencias de escape. Por ejemplo:
print("La ruta de archivo es: C:\\\\Users\\Usuario\\Desktop\\archivo.txt")