#Listas
to_do = ["Dirigirnos al hotel",
         "Ir a almorzar",
         "Visitar un museo",
         "Volver al hotel"]#Toda lo de las listas debe estar dentro de los corchetes
    #Ademas que deben estar separados por coma
print(to_do)
numbers = [1,2,3,4, "cinco"]
print(type(numbers))#python conoce a este tipo de dato como <class 'list'>
    #asi que puedo guardar distintos tipos de datos
mix = ["uno", 1, 3.14, True, [1, 2, 3]]#aca incluso estamos guardando una lista dentro
    #de la lista
print(mix)
print(len(mix))#nos dira que el largo de la lista es 5, porque tiene 5 datos
    #aun cuando hay una lista interna que agregaria mas
#Ahora haremos lo que se llama slicing, que me trae el lugar que le pido
print("Primer elemento", mix[0])
print("Segundo elemento", mix[2])
print("Ultimo elemento", mix[-1])
string = "Hola mundo"
print("Primer elemento", string[0])
print("Segundo elemento", string[2])
print("Ultimo elemento", string[-1])
#Ahora con un x:y le pido que me traiga los datos desde el 0 hasta la posicion anterior a y-1
print(mix[0:2])#me trae de la 0 a la 1, que seria uno, 1
print(mix[2:])#si no especifico el final va hasta el final
print(mix[:3])#si no especifico el inicio va desde el inicio hasta donde especifique - 1

print(mix)
mix.append(False)#Le agregamos una ultima linea en la lista, que en este caso es false
print(mix)
mix.append(["a", "b"])#Agrego a la posicion 6 una nueva lista que es independiente como
    #la anteriro lista
print(mix)
mix.insert(1,["a","b"])#Aca estoy diciendo que lo agregue especificamente a la
    #poscion 1, por lo tanto al numero 1 lo correra a la posicion 2
print(mix)

print(mix.index(["a","b"]))#Esto debolvera en que posivion esta, pero me dara 1
    #esto porque devolvera en que lugar lo encontro primero, no todos los lugares
numbers = [1,2,100,90.45,3,4,5]
print('Mayor:',max(numbers))#Aca le pido que me diga cual es el elemento mayor
print('Minimo:',min(numbers))#Aca le pido que me diga cual es el elemento menor
"""numbers_1 = ['chau','holaaaa', 5]
print('Mayor:',max(numbers_1))#Aca me dara error porque no puede analizar si hay
    #instancias str y un int
print('Minimo:',min(numbers_1))"""
numbers_1 = ['chau','holaaaa']
print('Mayor:',max(numbers_1))#Aca me dara el hola porque vera el de mayor caracteres
print('Minimo:',min(numbers_1))

#vamos a intentar borrar
del numbers [-1]#le pido que elimine la posicion final, osea el 5
print(numbers)
del numbers[:2]#Le pido que elime todo lo anterior a la posicion 2 - 1,
#osea la posicion 0 y 1
print(numbers)
del numbers
print(numbers)#Aca nos dara NameError: name 'numbers' is not defined. porque ya 
#no existe la lista