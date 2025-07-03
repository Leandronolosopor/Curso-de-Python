#La programacion orientada a objetos tiene clases que son moldes de una entidad
#El objeto es la ocurrencia de esa clase, osea la individualizacion
class Person:#aca estamos poniendo nombre a la clase y luego una funcion como creador
    def __init__(self, name, age):#Esto esta creando a la clase, osea es el constructor
        #self es una referencia al objeto actual de la clase, y se utiliza para acceder a las propiedades
        #y metodos de la clase dentro de ella
        #__init__ es un metodo especial en python conocido como el constructor de uan clase
        #Se invoca automaticamente al crear una nueva instancia (objeto) de esa clase.
        #Su proposito es inicializar los atributos del objeto
        self.name = name
        self.age = age
    
    def greet(self):#Aca estoy creando una funcion que tiene, un metodo, y se tiene que saludar a si
        #mismo y por eso se usa self
        print(f'Hola, mi nombre es {self.name} y tengo {self.age}')

person1 = Person('Ana', 30)#con esto hago que guarde en name ana y en age 30
person2 = Person('Luis', 25)

person1.greet()#con esto ago que persona1 salude
person2.greet()
