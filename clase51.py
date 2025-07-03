#*args y **kwargs
    #los args permite enviar multiples argumentos posicionales a una funcion. Se recibe como una tupla,
    # lo que significa que la cantidad de argumentos no es fija
    #Los kwargs permite enviar argumentos nombrados a una funcion. Se recibe como un diccionario,
    # permitiendo una forma fleible de pasara parametros donde puedes especificar nombres de variables

#En los parametros pondremos los nombres pero no sabemos con cuanta cantidad llegaran
# la convencion entonces dice que tenemos que usar * seguido del nombre que le pondremo
#  El nombre no es restrictivo, pero por buenas practicas se usa args
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2 ,3 ,4 ,5))
print(sum_numbers(1, 2))
print(sum_numbers(1, 2 ,3 ,4 ,5, 6, 7, 8, 9, 10))
#En estos casos args nos ayuda a sumar todos cuando no tengo la certesa de cuantos son los parametros
# Sin el * dara error TypeError: sum_numbers() takes 1 positional argument but 5 were given
