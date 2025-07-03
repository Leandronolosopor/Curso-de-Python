import csv
new_product = {
    'name': 'Wireless Chatger',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accesories',
    'entry_date': '2025-06-24' 
}#Estamos creando una fila que vamos a agregarle al csv

"""
with open('clase31products.csv', mode='a', newline='') as file:#mode=a es que se append
    #osea que se va agregar, newline='' dice que sea sin espacios
    #file.write('\n')
    csv_writer = csv.DictWriter(file, fieldnames = new_product.keys())#Aca estoy diciendo que en vez de leerlo en diccionario, que le escriba un diccionario
        #ademas del archivo hay que pasarle las llaves que tengo
        #fieldnames es una variable que creo aca
        #Esto de var = lista.key() se tiene que hacer para que los datos se alinean con sus respectivas columnas
    csv_writer.writerow(new_product)#writerow hace que se escriba en una fila
        #por lo tanto le decimos que a la variable que tiene guardada el archivo como diccionario para escribir
        #escriba una nueva fila con la lista
    #Todo esto lo que hace es añadrilo, pero pegado a la ultima linea, esto es porque antes de ejecutar el 
    #archivo hay que poner que haga un salto de linea, sino lo pegara y entonces sera parte del ultimo diccionario
"""

#Por eso haremos lo mismo solo que diremos que escriba un salto de linea antes de hacer lo que sigue
with open('clase31products.csv', mode='a', newline='') as file:
    file.write('\n')
    csv_writer = csv.DictWriter(file, fieldnames = new_product.keys())
    csv_writer.writerow(new_product)
