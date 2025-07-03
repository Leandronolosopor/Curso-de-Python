#Ahora veremos **kwargs

# Como no sabemos cuantos datos va a recibir la funcion que tiene que imprimir
#  Pero si tendremos el caso donde tendremos variables especificas donde se almacena la informacion
#   entonces se usa **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

#En este caso estamos pasando los argumentos posicionales, los estamos especificando
# Pero hay casos donde no sabremos cuantos van a ser, y ahi se usa kwargs
print_info(name = 'Leandro', age = 26, city = 'Lujan')
print_info(name = 'Leandro', age = 26, city = 'Lujan', country = 'Argentina')
"""
name: Leandro
age: 26    
city: Lujan
Como se ve hasta aca paso lo que puse
name: Leandro
age: 26
city: Lujan
country: Argentina
Y como se ve aca, le agregue una nueva llave y sin problema la agrego
"""
