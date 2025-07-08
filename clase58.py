#La diferencia entre concurrencia y asincornia es
"""
Concurrencia: ejecucion intercala de tareas
Asincronia: Tareas se suspenden y reanudadn
"""
#Crearemos un sistema de gestion de usuarios en una base de datos con gestion de inventario y gestionaremos el pago de los clientes
# tendremos una division de taresas
#  verificacion de inventario
#  Calculo de costo total
#  procesamiento de pagos

"""
Se usara la asincronia para tareas que tengan entrada y salida de datos
Y la concurrencia para tareas que pueden tener mucho tiempo de ejecucion de gpu
"""
import asyncio
import time
import random
import multiprocessing

# Crearemos una funcion asincrona para verificar el inventario
#  Esta funcion verificara la entrada y salida de la base de datos de manera simulada
async def check_inventory(item):
    print(f'Verificando inventario para {item}')
    #Hacemos que espere(await) y que eso lo haga de manera asincronica durmiento(asyncio.sleep)
    # en un lapso aleatorio de enteros entre 3 y 6 segundos
    await asyncio.sleep(random.randint(3, 6))
    print(f'Inventario verificado para {item}')
    #Y con esto simulamos la disponibilidad del producto
    return random.choice((True, False))

#Funcion asincrona para procesar el pago
async def process_payment(order_id):
    print(f'Procesando pago para la orden {order_id}...')
    #Ahora simularemos el tiempo de espera que tiene un servicio de pago
    await asyncio.sleep(random.randint(3, 6))
    print(f'Pago procesando para la orden {order_id}')
    return True #Y como ya terminamos la orden deve devolver un true

#Funcion intensiva en CPU para calcular el costo total del pedido
def calculate_total(items):
    #Imprimimos diciendo cuantos items son, por eso del largo de items
    print(f'Calculando el costo total para {len(items)} articulos...')
    #Ahora le decimos que espere 5 segundos
    time.sleep(5)
    #Y pedimos un total que tine que ser la suma de que por cada precio de cada item
    # osea que extraemos el precio de los item y lo iteramos por cada 1
    total = sum(item['price'] for item in items)
    print(f'Costo total calculado: {total}')
    return total

#Funcion que nos ayudara a procesar la orden
async def process_order(order_id, items):
    print(f'Iniciando el procesamiento de la orden {order_id}...')
    #Verificar de manera asincrona el inventario para cada articulo
    #Vamos a guardar cada item en una lista de items
    inventory_checks = [check_inventory(item['name']) for item in items]
    # Y despues vamos a pausar la operacion
    #  asyncio.gather permite ejecutar multiples corutinas de manera concurrente en python
    # Toma como argumentos varias tareas asíncronas y las ejecuta simultáneamente, esperando
    #  a que todas se completen antes de continuar
    inventory_result = await asyncio.gather(*inventory_checks)#y lo escribimos como *args para que reciba varios tipos de parametros no definidos

    #Ahora verificaremos si el producto no esta
    if not all(inventory_result): #Estamos diciendo que si no esta en todos los productos, le decimos que se cancela el pedido
        print(f'Orden {order_id} cancelada: Producto no esta disponible')
    
    with multiprocessing.Pool() as pool:#Agora llamamos al multiprocesamiento y hacemos un pool
        total = pool.apply(calculate_total, (items,))

    #Procesar el pago asincronicamente
    paymet_result = await process_payment(order_id)

    if paymet_result:
        print(f'Orden {order_id} completad con exito. Total: {total}')
    
    else:
        print(f'Error al procesar el pago de la orden {order_id}')

#Y ahora haremos una funcion principal que tendra las ordenes de 3 usuarios
async def main():
    orders = [
        {'order_id': 1, 'items': [{'name': 'Laptop', 'price': 1000}, {'name': 'Mouse', 'price': 50}]},
        {'order_id': 2, 'items': [{'name': 'Teclado', 'price': 80}, {'name': 'Monitor', 'price': 300}]},
        {'order_id': 3, 'items': [{'name': 'Smartphone', 'price': 700}, {'name': 'Funda', 'price': 20}]}
    ]#Cada ordent tiene un id y su informacion de los articulos que se pidieron
    
    #Procesar multiples ordenes concurrentes
    tasks = [process_order(order['order_id'], order['items']) for order in orders]
    await asyncio.gather(*tasks)

#Creamos el event loop
if __name__ == '__main__':
    asyncio.run(main())