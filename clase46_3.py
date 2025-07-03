#en este veremos el decorador property
class Circle:

    def __init__(self, radius: float):
        self._radius = radius

    @property
    def area(self) -> float:
        return 3.1416 * (self._radius ** 2)

    @property
    def radius(self) -> float:
        return self._radius

circle = Circle(5)
#Como se ve pude acceder al atributo sin tener que ponerlo entre parentesis, solo tuve que poner un . y el atributo
print(circle.area)    
#esto lo hacer property que nos permite acceder a los methodos pero como si fueran atributos
#como si fuera un .get()