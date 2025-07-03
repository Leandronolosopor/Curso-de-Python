#Ahora veremos la libreria que permite usar conjuntos aleatorios
import random

#Ahora vamos a generar un numero entero aleatorio
random_number = random.randint(1, 10)#random genera la aletoriedad
    #y randint da un es un método de la librería random en Python que genera un número entero aleatorio dentro de un rango específico
print(random_number)#y a mi aleatoriamente me a ido dando numeros distintos

#Ahora intentaremos elegir desde una lista
#hare una eleccion de colores aleatorios
colors = ['Rojo', 'Azul', 'Verde']
random_color = random.choice(colors)#y .choise le digo que elija de lo que le pongo adentro del parentecis
print(random_color)

#Ahora haremos que de vuelta los valores de las cosas como una baraja de cartas
#barajar una lista de cartas
cards = ['As', 'Rey', 'Reina', 'Jota', '10']
random.shuffle(cards)#Y .shuffle desordena los valores, los pone en otro orden al valor inicial
print(cards)