#Ejecutar scripts Python

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError('No se puede dividirentre 0')
    return a / b

#Ahora veremos como automatizar el ingreso de informacion para no tener que poner la funcion y el valro que le paso
if __name__ == '__main__':#Se escribe esto, osea que name es igual a main
    """
Esto significa
Ejecutá este bloque de código solo si este archivo se está ejecutando directamente,
 no si está siendo importado como módulo desde otro archivo
    """
    print('Operaciones')
    res_1 = add(3, 4)
    print(f'Suma: {res_1}')
    print(divide(10, 7))

#Ahora, si en la consola pongo  python clase49.py 
# me ejecutara el archivo sin que le de a ejecutar y me imprimira en consola lo que tenia que imprimir
