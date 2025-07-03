x = 'global' # Variable global

#Funcion externa
def outer_function():
    x = 'enclosing'
    #Esta x sera local, osea que persiste solo dentro del cuerpo de la funcion

    #Funcion interna
    def inner_function():
        x = 'local' #Variable local
        print(x)
    
    inner_function()
    print(x)

outer_function()
print(x)
"""
Todo esto imprimira

    local
    enclosing
    global
Esto es porque me accede a la funcion ,luego ingresa a la sub funcion y ve que imprime x, pero aca es local
Luego va abajo y imprime x, pero no puede acceder a la sub funcion
    """

