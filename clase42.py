#validacion de tipos y manejo de exepcion
#es importante validar los tipos de datos porque puede ser que use datos externos de los cuales no tengo control
"""
def divide(a: int, b: int) -> float:
    return a/b

print(divide(10, '2'))#esto dara un error porque estoy pidiendo un int que va a generar una division
#y le pase un str, el error sera TypeError
"""
#Ahora intentaremos validando que ambos parametros sean enteros
def divide(a: int, b: int) -> float:
    #validad que ambos parametros sean enteros
    if not isinstance(a, int) or not isinstance(b, int):#Estamos llamando a una funcion
        #esto para saber poder consultar si el dato es una instancia y si es del tipo que pido
        #entonces pregunta si a es una instancia y del tipo entero
        #Como queremos verificar que esto sea falso, le decimos que esto no sea una instancia
        #o que b tampoco es una instnacia y entero
        print('Error: ambos parametros deben ser enteros o flotantes')#Imprimimos un mensaje de error
        return None#Y le retornamos un none que es que no devuelva nada especificamente
    #Verificamos que el divisor no sea cero
    if b == 0:
        print('Error: El divisor no puede ser cero')
        return None
    return a/b

res_1 = divide(10, '2')#Error: ambos parametros deben ser enteros o flotantes
res_2 = divide(10, 0)#Error: El divisor no puede ser cero
res_3 = divide(10, 2)
print(res_3) 