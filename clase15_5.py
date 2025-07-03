#generador de fibonacci
#La serie de Fibonacci es una secuencia infinita de números donde cada término se obtiene sumando los dos anteriores, comenzando con 0 y 1. La secuencia se ve así: 0, 1, 1, 2, 3, 5, 8, 13, 21

def fibonacci(limit):
    a, b = 0, 1#puedo poner variables en una sola linea si pongo una , de por medio
    while a < limit:
        yield a
        a, b = b, a+b

for num in fibonacci(10):
    print(num)