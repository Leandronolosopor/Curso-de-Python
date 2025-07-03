import csv

file_path = 'clase31products.csv'#Estamos poniendo a una variable el valor del archivo
updated_file_path = 'clase31products_updated.csv' #y aca lo mismo pero este archivo no existe, lo voy a crear

with open(file_path, mode='r') as file:#Lo abre en modo lectura porque solo necesito abrirlo y leerlo para añadirlo al nuevo csv
    csv_reader = csv.DictReader(file)#Volvemos a cada fila en un diccionario usando la primera linea como claves
    #Obtener los nombres de las columnas existentes
    fieldnames = csv_reader.fieldnames + ['total_value']
    #Aca estoy diciendo que del csv, del reader, le vamos a preguntar cuales son los nombres de la columna
    #y como vamos a crear una columna nueva, vamos a calcular el valor total
    #para eso tengo que crear una lista en la que guardo el str
#Por si no se entendio, osea yo mismo no me entendi, lo que hago es que listo todos los nombres de columna
#name, price, etc, y le sumo una nueva a esa lista, y va a ser total_value

    with open(updated_file_path, mode='w', newline='') as updated_file:#como tenemos que crearlo y escribir ahi lo abriremos en formato escritura
        #osea, al no encontrar el archivo con este nombre, lo crea, y newline='' evita lineas en blanco extra
        #Esto se hace para que no halla saldos de lineas ni espacios que puedan ocupar espacio o dificulatar su lectura por codigo
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)#Esto crea un escritor que usara las columnas definidas en fieldnames
        #recordemos que fieldnames lo defini arriba en el with open original
        csv_writer.writeheader()#Escribir encabezado, eso hace writeheader
            #osea que escribe la primera linea en el nuevo csv
            #Y le escribira lo que guarde en fieldnames

        #Este fila itera sobre cada fila del csv original, y row sera un diccionario
        for row in csv_reader:
            row['total_value'] = float(row['price']) * int(row['quantity'])
                #row[price] cpmvoerte el precio que es una cadena de texto en un numero decimal
                #lo mismo con row[quiality]
                #Estamos haciendo que la cantidad de productors que tenemos se multiplique por el precio y eso me dara el valor total
            csv_writer.writerow(row)#Escribe la fila actualizada ahora con totla_value en el archivo de salida
            #y como es un for lo hara hasta que se quede sin filas
#Todo esto me va a haber creado una nueva lista y en esa nueva lista va a haber una nueva columna llamada total_value

