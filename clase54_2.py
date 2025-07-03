class Order:
    global_discount = 10

    def __init__(self, amount):
        self.amount = amount

    #Ahora vamos a hacer un metodo que accedera a la variable global que es global_discount
    #Pero sin instanciar la clase
    #Para esto usaremos el decorador classmethod    
     # para que class method funcione se requiere que el primer parametro sea uno que se refiere a la clase
      # para eso usaremos cls
    @classmethod
    def update_global_discount(cls, new_discount):
        cls.global_discount = new_discount
    
#Aca usamos esta mecanica de modificar un metodo sin instaciar
Order.update_global_discount(15)
#y despues lo imprimimos sin instanciar
print(Order.global_discount)