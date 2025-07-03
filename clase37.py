#De aca en adelante veremos las mejores practicas de python

#aca tenemos como no hay que hacer

numbers = [1, 2, 3, 4, 5]
squares = []

for number in numbers:
    square = number ** 2
    squares.append(square)

print(squares)
#No se hace asi porque es mas costozo y ocupa mas lineas de codigo

#forma correcta
numbers = numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)
