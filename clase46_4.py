#en este veremos el decorador setter
class Circle:

    def __init__(self, radius: float):
        self._radius = radius

    @property
    def area(self) -> float:
        return 3.1416 * (self._radius ** 2)

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter#Este es un decorador llamado setter, lo que hacees cambiar la informacion de un methodo
    def radius(self, value: float):
        if value < 0:#estasmos preguntando si el valor es menor que 0
            raise ValueError('El radio no puede ser negativo')#entonces hacemos la exepcion que de un value error
        self._radius = value# y si no es asi entonces que guarde en radius el valor

circle = Circle(5)
#print(circle.area)    
circle.radius = -10
print(circle.radius)
"""
raise ValueError('El radio no puede ser negativo')#entonces hacemos la exepcion que de un value error 
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: El radio no puede ser negativo
"""
#Osea, property nos devuleve informacion y setter modifica informacion