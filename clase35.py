#En esta clase haremos analisis estadistico de ventas con python
#Para eso primero tengo que importar la libreria de stadisticas y la de csv

import statistics
import csv

#Ahora leeremos los datos de ventas mensuales desde el archvio csv
#para eso haremos lo de generar un diccionario, abriremos el archvio
#leeremos el archvio como un diccionario
#y luego iteraremos para que cada fila del diccionario se guarde como quiero
#el primer dato que sea diga 'month' lo guardare como llave y el segundo que diga 'sales' y los sigueintes segundos
#los guardare como values

monthly_sales = {}
with open('clase35monthly_sales.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
print(sales)

#Ahora hallaremos la media de las ventas
mean_sales = statistics.mean(sales)#.mean es el methodo que me da la media
print(f'La media es: {mean_sales}')
    #La media es: 174.58333333333334

#Ahora hallaremos la mediana
median_sales = statistics.median(sales)#.median me trae la mediana
print(f'La mediana es: {median_sales}')

#Hallar la moda
mode_sales = statistics.mode(sales)#.mode me trae la moda
print(f'La moda es: {mode_sales}')

#Desviacion Estandar
stdev_sales = statistics.stdev(sales)#.stdev me trae la desviacion estandar
print(f'La desviacion estandar es: {stdev_sales}')

#Hallar la varianza
variance_sales = statistics.variance(sales)#.variance me trae la mvarianza
print(f'La moda es: {variance_sales}')

max_sales = max(sales)
min_sales = min(sales)

range_sales = max_sales - min_sales
print(f'Rango de ventas: {range_sales}')