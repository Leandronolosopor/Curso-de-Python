#Ahora usaremos la palabra reservada raise
#raise es una sentencia en Python que se utiliza para lanzar
# excepciones. Puedes usarla para generar una excepción específica, proporcionando un
# mensaje que explique el error.
def divide(a: int, b: int) -> float:
    #validad que ambos parametros sean enteros
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('Ambos parametros deben ser enteros.')
    if b == 0:
        raise ValueError('El divisor no puede ser cero.')
    return a/b

#res_1 = divide(10, '2')
"""
Traceback (most recent call last):
  File "e:\Cursos\Curso de Python\clase42_2.py", line 13, in <module>
    res_1 = divide(10, '2')
  File "e:\Cursos\Curso de Python\clase42_2.py", line 8, in divide
    raise TypeError('Ambos parametros deben ser enteros.')
TypeError: Ambos parametros deben ser enteros.
"""
#res_2 = divide(10, 0)
"""
Traceback (most recent call last):
  File "e:\Cursos\Curso de Python\clase42_2.py", line 20, in <module>
    res_2 = divide(10, 0)
  File "e:\Cursos\Curso de Python\clase42_2.py", line 10, in divide
    raise ValueError('El divisor no puede ser cero.')
ValueError: El divisor no puede ser cero.
"""
#Como se ve me esta arrojando mas informacion del error y el tipo de error ademas del mensaje que le pedi que me de

#res_3 = divide(10, 2)
#print(res_3) 

#Ahora veremos el ejemplo de uso
try:#Le digo que intente
    res = divide(10, '2')#instertar estos datos y dara un Error de tipo
    print(res)
except TypeError as e:#Y en exepcion manejaremos el tipo de dato que queremos exeptuar
    print(f'Error {e}')
    #Y esto nos dara de informacion espeficamente lo que le pedi imprimir en el raise y no toda la informacion sobre el error

try:
    res = divide(10, 0)#Error de division
    print(res)
except ValueError as e:
    print(f'Error {e}')

try:
    res = divide(10, 2)#Division correcta
    print(res)
except (ValueError, TypeError) as e:
    print(f'Error {e}')
    #Y aca me imprimira el numero y si le pongo un cero me dira que no puede ser divisible por cero