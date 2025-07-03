#En esta clase veremos las buenas practicas de lso comentarios y Docstring
#Ademas de ser claro no hay que abusar de la cantidad de comentarios

#Ahora todas mis notas propias empezaran con un Todo y en naranja para diferenciarlo
#Todo esto es como se usa el docstring

def calculate_average(numbers):
    """
    Calcula el promedio de una lista de numeros.

    Parametros:
    numbers (list): Una lista puede ser numeros enteros o flotantes

    Retorna:
    float: El promedio de los numeros en la lista
    """
#Todo lo que ponemos en el docstring es que va hacer lo que ponemos dentro, que parametros le damos,
#Todo. explicacamos que dato es en parentesis y que valores puede tomar
#Todo. luego decimos que retorna como dato de salido
    return sum(numbers) / len(numbers)

#Todo comentario deberia tener un espacio adelante del # para mas legibilidad, a la vez
#Todo. , lo que estamos poniendo en el comentario es que hace una funcion asi no mas
# Imprimiendo el resultado de la funcion
print(calculate_average([1,2,3,4,5]))


#Todo lo siguiente son malas practicas

def calculate_area(base, height):
    """
    Calcula el area de un triangulo
    """
    #Multiplicamos la base por la altura y luego la dividimos entre dos
    return (base * height) / 2
#Todo esto es mal porque estamos repitiendo el titulo de la funcion en la explicacion del docstrign
#Todo. tambien lo que devuelve el return ya muesta que esta haciendo, asi que no es necesario comentar que hace
#Todo. Si explica algo que se ve visualmente entonces esta mal
