#Para hacer una proteccion real debo hacer lo siguiente que hago en el methodo 3
class BaseClass:
    def __init__(self):
        self._protected_variable = 'Proctected'
 # la doble guion bajo __dice que le methodo es privado
        self.__private_variable = 'Privado'

    def _protected_method(self):
        print('Este es un metodo protegido')

    def __private_method(self):
        print('Esto es un metodo privado')

    #Ahora, como tengo methos y parametros privados, lo que puedo hacer es tener una funcion publica que los llame
    def public_method(self):
        self.__private_method()

base = BaseClass()
#print(base._protected_variable)
#base._protected_method()

base.public_method()
# Llamando a este methodo si podemos entrar al methodo privado porque esta dentro del codigo
    #Esto es un metodo privado

base.__private_method()
# AttributeError: 'BaseClass' object has no attribute '__private_method'. Did you mean: '_protected_method'?PS E:\Cursos\Curso de Python> 
    #No se pudo acceder, porque es privada y estoy fuera del codigo

print(base.__private_variable)
#Y dara el mismo error, dira que no existe, porque no lo puede encontrar gracias a __