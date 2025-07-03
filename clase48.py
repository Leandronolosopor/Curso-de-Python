#Sobrecarga de operadores
# Los operadores como + o == funcionana con tipos de datos predefinidos, numeros, cadenas
# Con la sobrecarga podemos modificar esto
# Ejemplo de sobrecarga de +

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 1)

v3 = v1 + v2  # Sobrecarga de `+`
print(v3)  # Output: Vector(6, 4)

#aca gracias al methodo magico __add__ la operacion + puede sumar vectores
#si no estaraia esta sobrecarga daria type error porque "+" no puede sumar vectores
# Tambien __repr__ sobrecargar no a un operador, sino a como se imprime en consola.
# Osea sobrecarga al print haciendo que tenga que imprimir como lo define __repr