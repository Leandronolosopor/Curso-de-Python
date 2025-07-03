#Si nosotros queremos trabajar con calculos matematicos que requieran calculos precisos
#porque sea que uso numeros infinitos como pi o con una , muy larga tengo que usar la libreria math
import math
#El archivo no puede llamarse exactamente como la libreria, osea el archivo no puede llamarse math
#por suerte este se llama clase34_2

#Ahora hallaremos el area y perimetro de un circulo
radius = 5
area = math.pi * radius ** 2
    #math ya me trae especificamente el valor de lo que le pido, y en este caso pi ya tiene guardado cuanto vale
perimeter = 2 * math.pi * radius
print(area)
print(perimeter)