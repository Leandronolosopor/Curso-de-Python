#Iteracion y control de flujo con bucles
numbers = [1, 2, 3,4, 5, 6]
for i in numbers:
    print('Aqui i es igual a: ', i+1)

for i in range(10):#Esto hase que recorra todo desde el rango 0 al 9
    print(i)

for i in range(3,10):#Esto hace que recorra todo desde el rango 3 al 9, por lo tanto esta salteando los 3 primeros y empieza por el cuarto
    print(i)

fruits = ['Manzana', 'Pera', 'Uva', 'Naranja', 'Tomate']
for fruit in fruits:#Como se ve en el for se crea una variable, que es la que va despues del for
    print(fruit)
    if fruit == 'Naranja':
        print('Naranja encontrada')

x = 0
#While significa mientras, osea mientras se cumpla una condicion entro al cuerpo de while
"""while x < 5:
        print(x)#El while entra en un bucle en este caso, porque entra constantemente mientras se cumpla la condicion
"""
while x < 5:
    print(x)
    x += 1#Con esto ira sumando en cada iteracion hasta ser 5 y ya no entrar

while x < 5:
    if x == 3:
        break#Esto hace que termine de manera abrupta cuando llega a x = 3
    print(x)
    x += 1

numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    if i == 3:
        break
    print('Aqui i es igual a: ', i)#Aca hara como arriba, terminara cuando sea igual a 3, osea te mostrara que es igual a 1 y a 2 no mas
    