#Metaprogramacion, methot new y init
"""
La metaprogramación en Python se refiere a la capacidad de escribir código que
 manipula o crea otro código, ya sea en tiempo de ejecución o en tiempo de compilación
"""
class MultiplierFactory:
    
    
    def __init__(self, factor: int):#Metodo iniciador
        print(f"Inicializando con factor {factor}")
        self.factor = factor

# Metodo new, este metodo crea una nueva instancia y desde aqui controlamos la creacion de 
# cada uno de los objetos
    def __new__(cls, factor: int):
        print(f"Creando instancia con factor {factor}")
        # Aca estamos creando los objetos
        return super(MultiplierFactory, cls).__new__(cls)
    
#Todo En la meta progrmacion tiene una buena practica a que es escribir el codigo en otro orden
# En el archivo clase50_2.py estara como debe ser
    
    def __call__(self, number: int) -> int:
        return number * self.factor
    
