#Desempaquetado args
def add(a, b, c):
    return a + b + c

values = (1, 2, 3)
#como se ve aca, estoy pasando los *args como value, porque el nombre que le ponga es le que quiera
# pero por convencion es args
#como aca estamos desempaquetando los valores mantenemos el nombre
print(add(*values))

#Desempaquetado kwargs

def print_info(name, age):
    print(f'Name: {name}, Age: {age}')

data = {'name': 'Ana', 'age': 30}
print_info(**data)