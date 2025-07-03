#En una funciona las anotaciones ayudan a definir los tipos de datos que los parametros
#deben recibir y el tipo de dato que devolvera la funcion.

def add_empoyee_ids(id1: int, id2: int) -> int:#como se ve, se define el dato como una anotacion comun
    #pero la final se hace un -> y se vuelve a poner el tipo de resultado que dara la funcion
    return id1 + id2

print(add_empoyee_ids(201, 202))
