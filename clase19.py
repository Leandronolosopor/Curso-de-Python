"""
def greet():#las funciones no se ejecutan si no las llamo
    print('Hola mundo')

greet()#aca la llamo
"""

"""
def greet(name):
    print('Hola', name)

greet('Leandro')#Como se ve, lo que pongo en los parentecis se guarda en la variable declarada de la funcion
greet('Carli')
"""
"""
def greet(name, last_name):
    print('Hola', name, last_name)

greet('Leandro', 'Salzberg')
greet('Carli', 'Florida')#Aca como se ve puedo guardar 2, pero si uno no tendria valor puesto, daria type error
"""
def greet(name, last_name = 'No tiene apellido'):#Esto hace que si no detecta variable declarada que sobrescriba a la variable del def, entonces enviara esto
    print('Hola', name, last_name)

greet('Leandro', 'Salzberg')
greet('Carli')
greet(last_name = 'Florida', name = 'Carli')#Hola Carli Florida, envia en el orden que tengo en el def por mas que lo pongo en otro orden
