#iterador de cadenas
#Creandro la cadena
text = 'Hola mundo'

#Creandro el objeto iterador
iter_text = iter(text)

#Iterar en la cadena
for char in iter_text:
    print(char)#Como los valores de iteracion es cada caracter, me devolvera 1 a la vez
