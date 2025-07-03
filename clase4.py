"""name = "Leandro"
print(type(name)) #Esto me dira que tipo de clase es, me dira str
"""

name = 'Leandro' #Esto muestra que el str puede ser con 'x', "x" o con '''x'''
caracter = "L"
print(type(caracter)) #Este me dira lo mismo

#pero las comillas triples son sensibles al salto de lineas
name = '''Leandro
Salzberg'''
print(name)

name = 'Leandro Salzberg'
print(name[0]) #Con esto al codigo le pido que me muestre el caracter que esta en la 
                #posicion que le pido en la cadena
print(name[1])
print(name[2])
print(name[-1]) #Y en esto le digo que empieze desde la ultima
print(name[-2]) #Y en esta de la ante ultima

name = 'Leandro Ezequiel'
last_name = 'Salzberg Plasencia'
print (name)
print(name + last_name) #Aca estoy concatenando el codigo, pero no hace el espacio.
                        # para eso deberia hacer print(name + " " + last_name)
#Una buena practica de python es no usar "" sino ''
print(name * 5) #Aca estamos haciendo que repita la concatenacion
print(name + ' ' + last_name)

#Y ahora hare una consulta de cual es la longitud con el comando len
print(len(name)) #16
print(len(last_name)) #18

#Ahora probare hacer que la sintaxis haga que lo vuelva minuscula y mayuscula,
#Para esto hay que usar un x.x porque le digo que viene un modificador a la variable
name2 = "LEANDRO       Ezequiel"
print(name.lower()) #Pone todo en minuscula
print(name.upper()) #Pone todo en mayuscula
print(name.strip()) #Deja como maximo un espacio donde antes habia mas de 1