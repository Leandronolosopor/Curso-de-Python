def outer_function():
    x = 'enclosing'
    def inner_function():
        nonlocal x#Con esto vuelvo no local a la x
        x = 'modified'
        print(f'El valor en inner es: {x}')
    inner_function()
    print(f'El valor outer: {x}')


outer_function()#Por lo tanto en ambos def tendre modified
print(y)#pero el valor sera dentro de la funcion porque no es local para la funcion, pero el nonlocal es para una subfuncion
#por lo tanto fuera de la funcion muere