#si yo quiero copiar una lista en otra y usar espacio extra para poder modificar 1 y no la otra
#para esto usare el slicing
a = [1,2,3,4,5]
b = a
print(a)
print(b)
del a[0]
print(id(a))#aca la consola me dar el mismo id porque b tambien es a
print(id(b))#cualquier modificacion de a me modifica b
c = a[:]#aca con el slicing copio la lista pero pongo la misma referencia
    #por lo tanto c esta guardado en otro lugar
print(id(c))
#ahora al agregar algo a me modificara a y b pero n oc
a.append(6)
print(a)
print(b)
print(c)
