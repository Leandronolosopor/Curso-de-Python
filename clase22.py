#Manejo de Expeciones y Errores en Python
try:
    pass#pass es que pase, osea que el codigo pase a xxx
except:
    pass
"""
try:
    divisor = int(input('Ingresa un numero divisor: '))
    result = 100/divisor
    print(result)
except:#Solo funciona cuando la exepcion es 1
    print('Error: El divisior no puede ser cero')
"""

"""
try:
    divisor = int(input('Ingresa un numero divisor: '))
    result = 100/divisor
    print(result)
except ZeroDivisionError:#por lo tanto las ecepciones se pondran el tipo de error
    print('Error: El divisior no puede ser cero')
except ValueError:#Entonces aca no expecificare error por un solo simbolo, sino por cualquier valor que no sea un numero
    print('Error: Debes introducir un numero valido')
"""

try:
    divisor = int(input('Ingresa un numero divisor: '))
    result = 100/divisor
    print(result)
except ZeroDivisionError as e:#Aca estoy agarrando la variable y mostrando cual es el error a nivel funcionamiento de python
            #Esto arrojara Ha ocurrido un error:  division by zero
    print('Error: El divisior no puede ser cero')
    print('Ha ocurrido un error: ', e)
except ValueError as e:
    print('Error: Debes introducir un numero valido')
    print('Ha ocurrido un error: ', e)# Este por ejemplo nos dira "invalid literal for int() with base 10: 'hola'"
 