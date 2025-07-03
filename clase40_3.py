#Existe una palabra reservada de python que permite volver a una variable global
x = 5 #Variable global

def modify_global():
    global x#Vuelve el valor global, por lo tanto el valor de la x de abajo sera global
    x += 3
    print(f'Valor modificado: {x}')

modify_global()
print(x)
"""
El resultado sera que agarra la x y le suma 3, entonces dara un 8, pero la x de abajo se volvio global
asi que el segunda x tambien sera global
Valor modificado: 8
8
"""