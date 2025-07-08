# El threading y multiprocessing es para poder gestionar de manera eficiente el uso de la cpu

# Sinconizacion de hilos en python
#  Cuando varios hilos intentan acceder a un mismo recurso habra problemas, para evitar esto
#   se utilizan mecanismos de sincronizacion como Lock y RLock

#Ejemplo de Lock
import threading

# Variable compartida
saldo = 0
lock = threading.Lock()  # Crear un Lock

def depositar(dinero):
    global saldo
    for _ in range(100000):
        with lock:  # Bloquear el acceso para evitar condiciones de carrera
            saldo += dinero

hilos = []
for _ in range(2):
    hilo = threading.Thread(target=depositar, args=(1,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print(f"Saldo final: {saldo}")  # Esperamos ver 200000 como saldo

# El uso de lock asegura que solo un hilo modifique la variable saldo en un momento dado,
#  evitando que el resultado final sea incorrecto
# Ademas, si 2 hilos al mismo tiempo intenta hacer lo de saldo += dinero
#  Ambos hacen lo mismo y pisan el valo de saldo, haciendo que el resultado sea distinto
#   Asi que ademas, el resultado al poder pisarse, puede ser impredecidble.
# RLock es una versión especial de Lock que permite que el mismo hilo adquiera el candado varias veces sin quedarse bloqueado.
#  RLock permite que el mismo hilo entre varias veces al mismo bloqueo, y solo se libera cuando lo libera la misma cantidad de veces.




#Compartir Datos entre procesos con multiprocessing
# A diferencia de los hilos, los procesos no comparten memoria de forma prederminada
#  Para que dos procesos puedan compartir datos, python proporciona herramientas como
#   multiprocessing.Queue y multiprocessing.Value.

#Ejemplo de datos con Queue
import multiprocessing

def calcular_cuadrado(numeros, cola):
    for n in numeros:
        cola.put(n * n)
        #.put agrega un elemeno a la cola compartida entre procesos

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5]
    cola = multiprocessing.Queue()

    proceso = multiprocessing.Process(target=calcular_cuadrado, args=(numeros, cola))
    proceso.start()
    proceso.join()

    # Extraer resultados de la cola
    while not cola.empty():
        print(cola.get())

#Usamos Queue para que el proceso secundario pueda pasar datos de vuelta al proceso principal.
