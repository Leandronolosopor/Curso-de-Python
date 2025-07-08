#Modulos y paquetes
# Un modulo es un archivo que contine definiciones y declaraciones que pueden ser funciones, variables y tambien clases
#  Al dividir el codigo en modulos mejora su funcionalidad, funcionamiento y mantenibilidad
#Para eso haremos un archivo de reportes y otro que sea la app

# Generaremos un informe de ventas para un mes especifico y uno de gastos

# Genera un informe de ventas para un mes especifico.
def generate_sales_report(month, sales):
    return f'Sales Report - {month}: Total sales: ${sales}'

#Generar un informe de gastos para un mes especifico
def generate_expoenses_report(month, expenses):
    return f'Expenses Report - {month}: Total expenses: ${expenses}'