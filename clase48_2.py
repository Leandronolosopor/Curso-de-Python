#Sobrecarga de coparacion ==, <, >
# La sobrecarga no se limita a operadores aritmeticos, sino tambien comparadores

#En este ejemplo __eq__ sobrecarga al comparador ==
# Por defecto == compara si dos objetos son el mismo en memoria, osea si son exactamente el mismo objeto
#  pero con __eq__ puedo personalizar que compara, haciendo que compare atributos en especifico
    #Sin __eq__ esto daria false porque p1 y p2 diria que son instancias distintas 
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __eq__(self, otra_persona):
        return self.nombre == otra_persona.nombre and self.edad == otra_persona.edad
    
    # Y aca uso lt para sobrecargar a <, permite comparar edades de 2 personas y sin lt daria o error o false
    # porque no puede buscar en una lista, mientras que el dato de edad esta en una lista
    # Gracias a lt puede ingresar a la lista y comparar si es menor
    def __lt__(self, otra_persona):
        return self.edad < otra_persona.edad

p1 = Persona("Ana", 30)
p2 = Persona("Ana", 30)

print(p1 == p2)  # Output: True (Ambas personas tienen el mismo nombre y edad)


p3 = Persona("Ana", 25)
p4 = Persona("Luis", 30)

print(p3 < p4)  # Output: True (Ana es menor que Luis)