#En esta aprendere a trabajar archivos JSON, osea archivos javascript, pero no es exactamente js, es un poco mas
#primero debemos importar la libreria json

import json

with open('clase32products.json', mode='r') as file:
    products = json.load(file)#Esto quiere decir que estoy diciendole a python que cargue la informacion del archivo
        #Con esto tenemos la lectura del archivo

#Mostrar el contenido
for product in products:#para cada i(product) que este en products, imprime lo siguiente
    """
    print(product)
    #Como el json ya esta en formato diccionario ya nos dara las claves con su correspondiente valor
    """
    print(f'Product: {product['name']}, Price: {product['price']}')#Y aca extraigo lo que quiero de infromacion como lo hice con el csv

