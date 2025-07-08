#La diferencia entre un paquete y modulo es que un modulo es el archivo que termina en .py y el paquete es donde estan los modulos.
# Comunmente una carpeta, la carpeta tiene que tener un archivo __init__.py porque indica que se esta trabajando con un paquete
# Lo haremos desde la carpeta clase60 y esto sera el main
#  Primero eidtare inventory
#   Despues a sales
#    Despues tenemos que importartar en en este archivo main, e importaremos el paquete junto al modulo que queremos

#Importar funciones de los modulos dentro del paquete
from clase60ecommerce.inventory import add_product, remove_product
from clase60ecommerce.sales import process_sales

add_product('Laptop', 10)
remove_product('Laptop')
process_sales('Laptop', 2)
"""
Producto Laptop agregando con 10 unidades.
Producto Laptop elminado del inventario
Venta procesada: 2 unidades de Laptop
"""
#Que la consola nos imprima esto muestra que pudo acceder a los modulos
