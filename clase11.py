#matrices y tuplas
"""Si tengo una matris de 
    1 2 3
    4 5 6
    7 8 9
    va a estar dividida por filas y columnas,
    a la vez en python tendre que hacer que cada posicion sea una fila entera,
     el cambio de posicion sera cambio de fila, y la posicion interna de la sublista
      sera la columna """
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix)
print(matrix[0])
#bueno, si quiero entrar a una posicion interna de otra posicion debo hacer lo siguiente
print(matrix[2][1])
#accedo a la posicion 3, luego itero a la posicion 2

#ahora las tuplas, las mismas van con parentecis en vez de corchetes
numbers = (1,2,3,4,5)
print(numbers)
print(type(numbers))#<class 'tuple'>
print(numbers[0])#me devolvera 1
#ahora si quiero modificar la tupla me arrojara error
"""sumary_linenumbers [0] = 'uno'
print(numbers) #TypeError: 'tuple' object does not support item assignment
"""

