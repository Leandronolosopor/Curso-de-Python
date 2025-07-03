#En esta clase veremos los enteros, flotantes y booleanos

x = 10
y = 5.678
print(x)
print(type(x)) #esto nos arrojara que el numero es un int, de interger, 
print(type(y)) #y esyo sera float, osea punto flotante

#en python se recomienda usar la anotacion cientifica para numeros muy grande, osea usar la e
z = 1.2e6 #Esto significa que 1.2e6 es equivalente a 1.2 * 10^6, 
        #lo que resulta en 1,200,000.0. La notación científica es útil para
        # trabajar con números muy grandes o muy pequeños
print(z) #Esto imprimira 1200000.0

a = 1.2e-6 #Esto es para que me muestre el valor usando esta nomenclatura, 
        #osea me mostrara 1.2e-06
print(a)

#Ahora intentaremos sumar
print (x + x)
print (x + y)
print (y + y)
    #Siempre que sume enteros con flotantes el resultado sera un flotante
    #a diferencia de C# puedo sumar int con float

#Ahora veremos booleanos
is_true = True #True esta em azul porque es una palabra reservada igual que false
is_false = False
print(type(is_true)) #Y esto nos dira que es un bool <class 'bool'>,
                # osea que es un booleano
                