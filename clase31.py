#En esta clase aprenderemos a leer archviso CSV
#para usar csv hay que importarlos

import csv
#Los csv estan en la misma carpeta que estoy trabajando, por eso no especificare la ruta de donde tiene que sacarlo

#Leer un archivo
"""
with open('clase31products.csv', mode='r') as file:#mode lo que hace es que sea de manera especifica, es un modismo quizas, no se
    csv_reader = csv.DictReader(file)#Esto lo uqe hace es decirle que al formato .csv lo habra en forma de diccionario
    for row in csv_reader:#despues esto es para imprimir cada fila
        print(row)

"""

#Mostrar la informacionm por columnas
with open('clase31products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f'Producto: {row['name']}, Precio: {row['price']}')
#Gracias a csv.DictReader, Python convierte cada fila del CSV en un diccionario usando la primera linea del archivo como claves del diccionario
#el csv empieza con el texto name,price,quantity,brand,category,entry_date
#Osea, python transforma cada texto que este en la primera fila como claves y entiende que cada sigueinte es la totalidad de los atributos
#y que las "," seran como la division de columnas asi que entendera que el primero de cada fila ira a name
#y que el segundo a price, y asi sucesivamente