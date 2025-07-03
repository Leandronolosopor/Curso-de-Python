#Los diccionarios
numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers)#Me imprime exactamente lo que puse, {1: 'uno', 2: 'dos', 3: 'tres'}
print(numbers[2])#Aca si solo me dara el valor que alla puesto en el numero 2
    #si en el puesto 2 ponia 4 me da error, y si ponia 4 me da el valor que alla puesto en 4:
information = {"Nombre": "Leandro",
               "Apellido": "Salzberg",
               "Altura": 1.60,
               "Edad": 26}
print(information)
print(information["Apellido"])#Y asi me traera Salzberg, si ponia todo en minuscula
    #o ponia 2, me daria error
#ahora intentare borrar edad, recuerda que el borrar va con []
del information["Edad"]
print(information)

#Ahora vere las propediades propias de los diccionarios
#metodo keys
claves = information.keys()#estoy guardando las llaves, lo que serian los punteros en sql
    #es lo que va antes de los :
print(claves)#dict_keys(['Nombre', 'Apellido', 'Altura'])
print(type(claves))#<class 'dict_keys'>

values = information.values()#estoy guardando los valores es lo que va despues de los :
print(values)

pairs = information.items()#me dara la key y el value que tiene, luego cierra un parentecis y me dice el siguiente
print(pairs)#dict_items([('Nombre', 'Leandro'), ('Apellido', 'Salzberg'), ('Altura', 1.6)])

print('n')
#vamos a creear un diccionario de contactos
"""Para que yo pueda acceder a la informacion de uno de los archivos si es que 
tengo mas de 1, tengo que ponerle un valor como llave, entonces lo que hare es
borrar nombre y pondre el valor de nombre adelante de la llave, "Leandro": {}"""
contacts = {"Leandro": {"Apellido": "Salzberg",
               "Altura": 1.69,
               "Edad": 26},
               "Carla": {"Apellido": "Florida",
               "Altura": 1.60,
               "Edad": 29}}
print(contacts["Leandro"])#Y accedere con esto a todos los datos de Leandro