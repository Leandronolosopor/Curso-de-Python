#generador y ahora vamos a usar la palabra de funcion de python que es def

def my_generator():
    return (1)
    yield 1#yield pausa la ejecución de la función y devuelve un valor, permitiendo que la función se reanude en el mismo punto en la siguiente llamada.
    yield 2
    yield 3

value = my_generator()
print(value)