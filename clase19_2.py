#Calculadora, funcion

def add(a, b):
    return a + b #return devuelve un valor de una funcion al lugar donde se llamo a la funcion
    #Este valor puede ser utilizado posteriormente en el codigo por lo tanto queda guardado

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculator():
    while True:
        print('Seleccione una operacion')
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplicacion')
        print('4. Division')
        print('5. Salir')

        option = input('ingresa una opcion (1,2,3,4,5): ')

        if option == '5':#como el dato es un str hay que poner que los inputs son str
            print('Esta saliendo de la calculadora')
            break #Para salir de un while con un true hay que poner un break
        if option in ['1','2','3','4']:
            num1 = float(input('Ingrese el primer numero: '))
            num2 = float(input('Ingrese el segundo numero: '))

            if option == '1':
                print('La suma es:', add(num1, num2))
            elif option == '2':
                print('La resta es:', substract(num1, num2))
            elif option == '3':
                print('La division es:', divide(num1, num2))
            elif option == '4':
                print('La multiplicacion es:', divide(num1, num2))
        else:
            print('Opcion no valida')

calculator()
