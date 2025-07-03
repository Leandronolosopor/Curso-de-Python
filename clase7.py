#Estamos utilizando operadores numericos
a = 10
b = 3
print("Suma: ", a + b)
print("Resta: ", a - b)
print("Multiplicacion: ", a * b)
print("Division: ", a / b)

#Operaciones de la programacion
#Modulo nos da el resto de una division, esto lo hace el simbolo %
print("Modulo: ", a % b)
    #Hay que tener cuidado, porque si la division es por 0 nos dara un error de division by zero
#Doble division, lo que nos da es la parte entera de la division
print("Parte entera de la division: ", a // b)
#Potenciacion se realiza con el doble asterisco **
print("Multiplicacion: ", a ** b)
#Variable shark, lo que hago es repetir el simbolo y sumarlo a si mismo mas otro numero
#sin shark
a = a + 2
print(a)
#con shark
a += 2
print(a)
a -= 2
print(a)
a *= 2
print(a)
a /= 2
print(a)
a **= 2
print(a)

#Python ejecuta de izquierda a derecha y respeta los parentecis
operation_3 = (2+3) * (4**2) / 8 - 2
    #hara los parentecis y luego la multiplicacion antes de la division, porque va
    #de izquierda a derecha
#booleanos devolvera true o false
a = 10
b = 8
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print(a == b)
print(a != b)
##Si pondria que b es 10.0 tambien me dara true porque no diferencia float de int si 
#su valor es el mismo
b = 10.0
print(a == b)