#Vamos a intentar leer archivos, en este caso el cuento que tenemos como txt de clase30_caperusita
#Leer un archivo linea por linea
"""
with open('clase30_caperusita.txt', 'r') as file:#hay que ponerle la 'r' de read, y as file es del archivo, asi que es necesario ponerlo
#with me abrira un archivo y me lo cerrara de manera eficiente
    #Al estar en la misma carpeta solo debo decirle el nombre del archivo
    for lineas in file:#Le digo que lea el archivo y que por cada cosa que lee
        print(lineas.strip())#borre los espacios de mas
            #si no pongo el strip() lo que hara es que agregara un salto de linea de mas
"""
#Ahora leeremos todas las lineas pero en una lista
"""
with open('clase30_caperusita.txt', 'r') as file:
    lines = file.readlines()#readlines ya es un metodo de pyhton que entiende que tiene que leer todo
    print(lines)
    #y esto nos mostrara separada cada linea con \n', ademas de ller todo en conjunto.
    #nos mostrara \n porque lee todo en una misma linea
"""
#Agrear una linea al archivo
"""
with open('clase30_caperusita.txt', 'a') as file:#a lo que hace es añadir, es un add
    file.write('\n\nBy:ChatGPT')#Esto añade al final del archivo lo que le escribi
    #osea modifico el archivo
"""

#Sobreescribir el texto
with open('clase30_caperusita.txt', 'w') as file:#Esto significa que lo estoy abriendo en modo escritura
    file.write('\n\nBy:ChatGPT')#Esto sobreescribio todo el texto y le puso esto ultimo que le mandamos
