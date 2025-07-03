#Listas por compresion en python es poder hacer una lista y su recorrido en una sola linea en vez de en muchas
squares = [x**2 for x in range(1,11) ]#creo toda una funcion para generar la lista
#print('Cuadrados:', squares)#Cuadrados: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) * 32 for temp in celsius]
#print('Temperatura en grados F:', fahrenheit)

#Numeros pares
evens = [x for x in range(1, 21)
         if x%2 == 0]#por cada valor de x que esta en el valor del rango, si x modulo 2 es igual a 0 "osea es par" se añade a la lista
#print(evens)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    #Lo que estoy diciendo es que por fila (row) en la matrix entre, e itere en la matrix
    #por lo tanto entrara a cada fila, pero row tambien ejecuta i, y en el siguiente
    #for, pongo que i estara en el rango del largo de la matrix empezando de 0,
    #y el largo sera el final de cada fila de la matrix
print(matrix)#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#print(transposed)#[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    #Esta lo hace manera distinta porque me muestra las posiciones por columna

transposed = []#Asi seria lo mismo que la compresion list de antes pero sin el compresion list
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)
#El compreshion list hace mas eficiente, lo hace mas rapido ademas de ser mas legible
