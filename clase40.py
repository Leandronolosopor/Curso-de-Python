#en este volveremos a los comentarios mal hechos para poder tomar notas de clase
#En esta clase veremos el tiempo de vida y alcance de variables
def local_function():
    x = 10 #Variable local
    print(f'El valor de la variable es {x}')

local_function()#Podremos acceder al valor de x mientras se ejecute la funcion
"""
print(x)#Pero no pudemos acceder a los valores dentro de la funcion de manera directa
#Esto genera error
"""

x = 100

def show_global():
    print(f'El valor de la variable global es {x}')

print(x)#Ahora, esta si me dara el valor de x, eso significa que x es uan variable local