#Ahora verenmos las enumeraciones
from enum import Enum

class OrderStatus(Enum):
    PENDING = 1 #Pendiente
    SHIPPED = 2 #Enviado
    DELIVERED = 3 #Entregado
"""
    los parámetros PENDING, SHIPPED y DELIVERED se definen en mayúsculas para 
    indicar que son constantes que representan estados específicos de una orden.
    Esta práctica mejora la legibilidad del código y ayuda a evitar errores al 
    utilizar valores incorrectos.
"""
def check_order_status(status: OrderStatus):#Aca le digo que el parametro o variable status es del tipo del estado de la orden
    # Comprueba el estado del pedido y devuelve un mensaje
    if status == OrderStatus.PENDING:#Comprueba el estado del pedido
        return "Order is still pending."
    elif status == OrderStatus.SHIPPED:
        return "Order has been shipped."
    elif status == OrderStatus.DELIVERED:
        return "Order has been delivered."
    
print(check_order_status(OrderStatus.DELIVERED))#Como se ve aca directamente llamo a la clase
    #y le pido que se ejecute directamente DELIVERED, esto se hace porque es posible
print(check_order_status(OrderStatus.SHIPPED))