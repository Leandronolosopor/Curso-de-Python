"""
Ejercicios:
Doble de los Números
Dada una lista de números [1, 2, 3, 4, 5], crea una nueva lista que contenga el doble de cada número usando una List Comprehension.
"""
ej1 = [1, 2, 3, 4, 5]
ej1_2 = [(i * 2) for i in ej1]
#print(ej1_2)
ej3 = ej1
#print(id(ej3), '\n', id(ej1))

"""
Filtrar y Transformar en un Solo Paso
Tienes una lista de palabras ["sol", "mar", "montaña", "rio", "estrella"] y quieres obtener una nueva lista con las palabras que tengan más de 3 letras y estén en mayúsculas.
"""
ej2 = ["sol", "mar", "montaña", "rio", "estrella"]
ej2_2 = [i for i in ej2 if len(i) < 4]
#print(ej2_2)

"""
Crear un Diccionario con List Comprehension
Tienes dos listas, una de claves ["nombre", "edad", "ocupación"] y otra de valores ["Juan", 30, "Ingeniero"]. Crea un diccionario combinando ambas listas usando una List Comprehension.
"""
keys = ["nombre", "edad", "ocupación"]
values = ["Juan", 30, "Ingeniero"]
diccionary = {keys[i]: values[i] for i in range(len(keys))}#tiene que ser con range porque los valores tienen que ser ints, si pongo solo keys me hara el de keys pero cuando valla a values tomara como que los valores de i son str y dara error
#print(diccionary)

"""
Anidación de List Comprehensions
Dada una lista de listas (una matriz):

pythonCopiar código
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Calcula la matriz traspuesta utilizando una List Comprehension anidada.
"""
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print (matriz)
transpusta = [[fila[i] for fila in matriz] for i in range(len(matriz))]#}Hago que cada posicion de la primera dimencion de la matriz se guarde en fila y todos sus valores
    #como dije que fila tendria una lista que se guardaria en i, entonces esas posiciones se guardan en i, y despues ya tengo las i, por lo tanto con otro for creo una
    #iteracion donde para cada i que tiene la posicion 0, 1 y 2 que dentro tienen cosas como [1, 2, 3], entonces que itere sobre eso en un rango que sea el largo de la matriz
print(transpusta)

"""
Extraer Información de una Lista de Diccionarios
Dada una lista de diccionarios que representan personas:

pythonCopiar código
personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]
Extrae una lista de nombres de personas que viven en “Madrid” y tienen más de 30 años.

"""
personas = [{"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
            {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
            {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
            {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
            ]
personas_filtradas = [i['nombre'] for i in personas if i['ciudad'] == 'Madrid' and i['edad'] >= 30]
#print(personas_filtradas)

"""

List Comprehension con un else
Dada una lista de números [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crea una nueva lista multiplicando por 2 los números pares y dejando los impares como están.
"""
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares_lista = [i * 2 if i%2 == 0 else i for i in lista2]
#print(pares_lista)