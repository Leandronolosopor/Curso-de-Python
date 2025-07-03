#Ahora veremos anotaciones con classes
class Employee:
    name: str#Como se ve se define antes que parametros tendra en total la clase y que tipo seran
    age: int
    salary: float

    def __init__(self, name: str, age: int, salary: float):#y como no hay resultado o es multiple no defino el -> tipo dato
        self.name = name
        self.age = age
        self.salary = salary

    def introduce(self) -> str:#Como se ve, aca no le pongo variables, pero me devolvera algo esta funcion
        #y sera un string, por eso le anoto que el dato que me devolvera sera un str
        return f'hola, me llamo {self.name}, tengo {self.age}'

employee1 = Employee('Carlos', '30', 3500.0)#Como es flotante el salario tengo que poner que es con coma
#Si no le pongo la coma (osea el punto) no me dara error, pero es incorrecto a nivel practicas
print(employee1.introduce())
#ahora instalamos por consola la libreria mypy
#pip install mypy
#que hace esto, si no hay conflicto en el archivo nos lo dira 
"""
    Ejemplo
        PS E:\Cursos\Curso de Python> mypy clase41_2.py
        Success: no issues found in 1 source file
"""
#Pero hay otros donde si
"""
PS E:\Cursos\Curso de Python> mypy clase41_3.py
clase41_3.py:16: error: Argument 2 to "Employee" has incompatible type "str"; expected "int"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
"""
#Esto me dice que le estoy pasando un str donde yo le especifique que es un entero
#El codigo si lo ejecuto se ejecuta sin problema, pero generara errores si intento hacer sumas o esas cosas
