"""Desafío: ¿Cuántas líneas tiene el cuento de Caperucita Roja?
Ahora, te dejo un reto: cuenta el número de líneas en el archivo caperucita.txt y
comparte tu resultado en los comentarios. Este ejercicio no solo reforzará tus habilidades, sino que también te acercará a comprender el poder del manejo de archivos en Python.
"""

"""
with open('clase30_caperusita.txt', 'r') as file:
    line = file.readline()
    for i in line:
        if i == '\n':
            e = 1
            print(e)
            print(i)
            e += 1
        else:
            continue
"""
with open('clase30_caperusita.txt', 'r') as file:
    cantidad_lineas = sum(1 for _ in file)
print(f'Cantidad de líneas: {cantidad_lineas}')
