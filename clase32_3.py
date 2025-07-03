import json
#importo json

file_path = 'clase32products.json'
#abro el archivo

new_product = {
    "name": "Wireless Charger",
    "price": 75,
    "quantity": 100,
    "brand": "ChargeMaster",
    "category": "Accessories",
    "entry_date": "2024-07-01"
}#Y lo abro primeramente en modo lectura, hay que recordar que hay que respetar los formatos
#en el json se usa comilla doble "", y no '', por eso los datos tendrian que tener comilla doble


with open(file_path, mode='r') as file:
    products = json.load(file)#Y aca hago lo de abrir el archivo y cargarle el json

products.append(new_product)

with open(file_path, mode='w') as file:
    json.dump(products, file, indent=4)#esto permite guardar datos de manera estructurada y facil de leer
        #recibe 3 parametros, le objeto que deseo volvar, el objeto archivo donde se escribira
        #y un parametro opcional de indetacion para hacer que el JSON sea mas legible
            #La identacion son los espacios en blanco al inicio de cada linea de codigo.
            #por lo tanto ident = 4 es 4 espacios
#Todo este proceso agregara un diccionario mas al archivo json