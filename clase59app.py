import clase59reportes # Como se ve lo que importo es el nombre del archivo

#Generar reportes de ventas y gastos usando funciones del modulo
sales_report = clase59reportes.generate_sales_report('Octubre', 10000)
expense_report = clase59reportes.generate_expoenses_report('Octubre', 50000)

print(sales_report)
print(expense_report)
#Y esto nos dara lo que pusimos en el modulo de reportes, lo que nos permite interactuar entre modulos
