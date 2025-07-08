#El asincornismo es cuando puedo enviar multiples tareas al servidor en ves de enviar una a la vez
#Para esto necesitamos usar la libreria asyncio
import asyncio

async def process_data(data):
    print(f'Procesando {data}...')
    #Simular una operacion
    await asyncio.sleep(10) # Esto ayuda que junto a la libreria se defina la espera del programa sin afectar lo que seria
        # el loop del evento
    print(f'{data} procesado.')
    return data * 2

async def main():
    print('Inicio de procesamiento')
    result = await process_data('archivo.txt')
        # estamos diciendo que el resultado es igual a que vamos a esperar el event loop
        # ademas con la funcion simulando que le mandamos un archivo txt
    print(f'Resultado: {result}')

#Una ves definidas ambas funciones llamamos con un asyncio.run()

asyncio.run(main())