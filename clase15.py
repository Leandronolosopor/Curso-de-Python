#Iteradores y Generadores sin indices para uso eficiente de Memoria
#Ejemplo de iterador

#Crear una lista
my_list = [1, 2, 3, 4]

#Obtener el iterador
my_iter = iter(my_list)#iter() es un iterador que se usa en listas, tuplas o cadenas sin necesidad de usar indices

#Usar el iterador
print(next(my_iter))#Nos arroja el siguiente valor de un iterador, osea el siguiente elemento a representan.
            #Primero nos arrojara 1, hasta ponga otro next() y ahir me arrojara 2 y asi sucesivamente
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))#Como ya no tengo almacenado en memoria un siguiente iterador me arrojara un "StopIteration"
