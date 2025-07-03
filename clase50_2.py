class MultiplierFactory:

# new tiene que ir al principio en vez de init, porque en new estamos creando la instncia
#  
    def __new__(cls, factor: int):
        print(f"Creando instancia con factor {factor}")
        return super(MultiplierFactory, cls).__new__(cls)
    
    def __init__(self, factor: int):
        print(f"Inicializando con factor {factor}")
        self.factor = factor
    
    def __call__(self, number: int) -> int:
        return number * self.factor
# Vamos a crear un objeto
multiplier = MultiplierFactory(5) #Le daremos un valor de 5

#le daremos un numero 10 que queremos que se multiplique con el 10
result = multiplier(10)
print(result)
"""
    Creando instancia con factor 5
    Inicializando con factor 5
    50
"""

#La metaprogamacion no es necesaria cada ves que se crea una clase