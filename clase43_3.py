from collections import deque
#deque lo que hace es permitir analisar las colas ambos extremos y agregar y eliminar de manera eficiente
#tiene un rendimiento mas bajo al eliminar elementos del inicio

def manage_delivery_queue() -> deque:#Le decimos que nos devolvera una deque, osea es una lista al fin y al cabo
    # Crea una cola para gestionar entregas de productos
    delivery_queue = deque(["order_1", "order_2", "order_3"])#creo la lista y digo que sera un deque
    delivery_queue.append("order_4")  # Agrega al final de la cola
    delivery_queue.appendleft("order_0")  # Agrega al principio de la cola
        # Esto es especifico de este methodo, osea del deque
    delivery_queue.pop()  # Elimina del final
        # Esto es especifico de este methodo, osea del deque
    delivery_queue.popleft()  # Elimina del principio
        # Esto es especifico de este methodo, osea del deque
    return delivery_queue

queue = manage_delivery_queue()
print(queue) 
#Una lista solo deja agregar en un extremo, que es el final