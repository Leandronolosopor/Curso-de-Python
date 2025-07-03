#Crear un iterador para los numeros impares

#Limite
limit = 10

#Cear iterador
odd_iter = iter(range(1, limit+1, 2))#Aca le digo que el rango ira de 1 a el limite
            #y que al rango que itera finaliza en uno superior al limite, asi puede terminar en 10 si ese necesario
            #y la segunda , hace que salte de en 2
#Usar el iterador
for num in odd_iter:
    print(num)
