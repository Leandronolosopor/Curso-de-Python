#Variables protegidas y privadas 
class BaseClass:
    def __init__(self):
        self._protected_variable = 'Proctected' #Cada vez que trabajemos con metodos o variables protegidas hay que usar la convencion de ponerle _ al principio
            #Esto significa que vamos a poder acceder desde fuera de la clase
            # Pero estamos dando otra informacion cuando una persona vuelva a leer nuestro codigo
        
    def _protected_method(self):
        print('Este es un metodo protegido')

base = BaseClass()
print(base._protected_variable)
base._protected_method()
#en ambos caso estoy pudiendo acceder a la informacion, eso es porque python no esta
# restringiendo el codigo, lo hacemos por convencion para que si otro programador ve el codigo
#  sepa que tiende que estar protegido