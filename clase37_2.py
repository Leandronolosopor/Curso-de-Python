#En python se usa el documento pip 8 como documento con las buenas practicas de python.
#A continuacio veremos 4 practicas que se mencionana

#El primero es que se usara mayuscula para el nombre de la clase.
#pero todo lo demas usara minuscula y se separara por un _
class Calculator:
    def add_numbers(self, first_number, second_number):#Que cada identacion sea de 4 espacios tambien es parte de esas buenas practicas
        #Tambien hay una longitud de linea sugerida, las lineas deben ser igual a 79 caracteres
        result = first_number + second_number#Tambien esta el espacio, hay que hacer espacio entre simbolos como + o -
        #y cuando se usa una , hay que hacer espacio solo despues de ponerla
        return result

calc = Calculator()

print(calc.add_numbers(5, 3))
