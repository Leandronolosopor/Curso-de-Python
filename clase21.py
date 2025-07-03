#Recusividad en python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)#si tenemos 5, n es 5 mas el 4 menos 1, y asi ira hasta tener valor 0 que retornara 1

factorial_5 = print(factorial(9))

#caso fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci (n-1) + fibonacci (n-2)

number = 8
print(fibonacci(number))

#Ejercicio, obtener los numeros naturales
def recursividad_natural(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)