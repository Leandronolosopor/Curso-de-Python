#Ahora veremos el paralelismo
#lo anterior era para poder trabajar con hilos
import multiprocessing

#Funcion que calcule el cuadrado de un numero
def calculate_square(n):
    return n*n

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]

    #crear un pool
    with multiprocessing.Pool() as pool:
        #Esto permitira ejutar hilos pero en paralelo
        results = pool.map(calculate_square, numbers)
        #.map aplica una funcion a todos los elementos de un iterable y devuelve una lista con los resultados

    print(f'Resultados: {results}')
