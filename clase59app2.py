from clase59reportes import generate_sales_report #Aca estoy importando solo una cosa de reportes para no traer todo si es que no lo necesito

print(generate_sales_report('Noviembre', 12000))
# Y de igual manera puedo ver lo de reporte, pero no puedo si quiero llamar a expenses
print(generate_expoenses_report('Noviembre', 12000))


from clase59reportes import generate_sales_report, generate_expoenses_report #Y con esto ya podre llamarlo
