#uso de metodos magicos
#Los metodos magicos son funciones especiales que permiten personalizarel comportamiento de las clases
#El codigo fue hecho de ante mano por la profe
class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str: # Este es el primer methodo magico
    #Este methodo hace referencia a un string, lo que hace es deficini como se presenta un objeto
    # cuando es pasado a cadena de texto o nosotros estamos imprimiendo uno de estos objetos
        # Devuelve una representación amigable para el usuario
        return f"Persona: {self.nombre}, {self.edad} años"

    def __repr__(self) -> str: # Este es el methodo de representacion
    #Lo que hace es dar la informacion detallada del objeto
        # Devuelve una representación detallada del objeto para depuración
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"

    def __eq__(self, otra_persona) -> bool: # Este methodo es el de la comparacion
    #Compara un objeto cuando se usa el simbolo de igualdad
        # Compara si dos personas son iguales en función del nombre y la edad
        return self.nombre == otra_persona.nombre and self.edad == otra_persona.edad

    def __lt__(self, otra_persona) -> bool: # Este methodo compara menor que
    #Osea que compara si el objeto actual es menor que el objeto que le pasamos como 
    # argumento basado en el atributo que le pasemos
        # Compara si una persona es "menor" que otra en función de la edad
        return self.edad < otra_persona.edad

    def __add__(self, otra_persona): # Este methodo es el de sumatoria
    #Este methodo trae el valor de una variable del primer objeto y le suma la misma
    # variable pero de otro objeto
        # Sobrecarga el operador + para sumar las edades de dos personas
        return self.edad + otra_persona.edad

# Crear instancias de Persona
p1 = Persona("Ana", 28)
p2 = Persona("Luis", 35)
p3 = Persona("Ana", 28)

# __str__: Representación legible
#print(p1)  # Output: Persona: Ana, 28 años

# __repr__: Representación detallada
#print(repr(p2))  # Output: Persona(nombre='Luis', edad=35)

# __eq__: Comparación de igualdad
#print(p1 == p3)  # Output: True (son iguales en nombre y edad)

# __lt__: Comparación "menor que" por edad
#print(p1 < p2)  # Output: True (porque 28 es menor que 35)

# __add__: Sumar edades de dos personas
print(p1 + p2)  # Output: 63 (28 + 35)
