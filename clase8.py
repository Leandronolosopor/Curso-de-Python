#En python puedo pedir que me ingrese algo y se guarde con un input
name = input("Ingrese su nombre: ")
print (name)
print(type(name))
"""age = input("Ingrese su nombre: ")
print (age)
print(type(age))""" #ambos type me dira que es tipo string, para que input no sea string
    #hay que realizar un artificio, osea cambiar el valor a interger
age = int(input("Ingrese su nombre: "))
print (age)
print(type(age))

age = float(input("Ingrese su nombre: "))#esto es si lo debo volver float
print (age)
print(type(age))

#Pero si ingresamos algo que no es un dato int o float me dara un error
#ValueError: invalid literal for int() with base 10: 's'
