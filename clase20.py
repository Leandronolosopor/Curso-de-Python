#funciones lambda, son cuando necesitamos operaciones sensillas donde no necesitamso crear funciones con nombre
#solo necesita parametros y la operacion

add = lambda a, b: a + b
print(add(10,4))

multiply = lambda a, b: a * b #Como se ve, lambda me permite realizar una operacion simple sin if, sin for, sin def
print(multiply(80, 5))

#Cuadradro de cada numero
numbers = range(11)#Como quiero los numeros del 0 al 10 puedo poner (0,10) o (11)
squared_numbers = list(map(lambda x: x**2, numbers))#list crea lista a partir de un iterable
    #osea list('abc') devuelve ['a', 'b', 'c']
    #map() hace que se haga lo mismo a cada elemento de la lista, osea que si en la lista pongo que se multiplica por 2
    #lo que hace es que a cada elemento lo multiplica por 2
print('Cuadrados:', squared_numbers)

#Pares
even_numbers = list(filter(lambda x: x%2 == 0, numbers))#filter hace que se seleccione en una lista los elementos que cumplan con una condicion
print('Pares:', even_numbers)