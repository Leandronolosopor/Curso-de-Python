#Estrucutas de datos avanzadas en python
#para esto necesitamos librerias que nos den collections y enumeraciones
from collections import defaultdict#defaultdic establece un valor por defecto en caso 
#de que este valor no exista en el diccionario

from collections import defaultdict

def count_products(orders: list[str]) -> defaultdict:#como se ve decimos que el parametro es una lista, y que sus claves son de tipo string
    #y que el valor que devuelve la funcion es un defaultdict, osea crea un diccionario por defecto
    
    #Crea un diccionario con valor por defecto 0 
    product_count = defaultdict(int)#creamos una defaultdict que guardara int
    for product in orders:#luego iteramos y guardamos cada orders en producto y cada producto
        # sera parte de una lista de que es la de produc_count, a la cual se ira sumando a si misma mas 1
        product_count[product] +=1
    return product_count#y devuelve el resultado de esto y lo vuelve un diccionario por como creamos el parametro

orders = ['laptop', 'smartphone', 'laptop', 'tablet']
count = count_products(orders)
print(count)