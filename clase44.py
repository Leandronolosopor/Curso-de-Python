#Decoradores
#Los decoradores permiten exteneder o modificar el comportamiento de una funcion sin
# cambiar su codigo interno, y pare eso se usa el simbolo "@"

# Osea, los decoradores es una funcion que toma otra funcion como argumento y le 
# agrega funcionalidad adicional y devuelve una nueva funcion modificada

def log_transaction(func):#Esta es la funcion decoradora
    def wrapper():#Esta se llama funcion enboltorio
        print('1 Log de la transaccion...')
        func()#Aca estamos llamando la parametro de la funcion para que se ejecute
        print('3 Log terminado...')
    return wrapper#Hay que returnar la funcion enboltorio



@log_transaction#Y asi volvemos decorador a la funcion
#Lo que hara esto primero es llamar a la funcion log_transaction, despues entra en su funcion
# interna que es la funcion envoltorio, luego imprime el Log de la transaccion
#Luego se ejecutara process_payment porque ejecuta func()
# y como def procces_payment esta despues de un decorador se entiende que es la funcion modificada
# y luego continuara con print lo terminado
def process_paymet():#Todo esto es equivalente a "process_paymet = log_transaction(process_paymet)"
    print('2 Procesando pago...')
    #Lo que vamos a darle es darle funcionalidad antes y despues a esto

process_paymet()