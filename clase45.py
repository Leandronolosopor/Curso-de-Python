#Decoradores aninados y con parametos
#vamos a hacer que un empleado administrador pueda elimnar a otro empleado

#Decorador que comprueba si un empleado tiene un rol especifico
def check_acces(required_role):
    def decorator(func):
        def wrapper(employee):
            #Comprobamos si el rol del empleado coincide con el rol requerido
            if employee.get('role') == required_role:#si el rol es igual al rol que requiero
                return func(employee)#devuelveme el empleado
            else:
                print(f'ACCESO DENEGADO. Solo {required_role} pueden realizar esta accion')
        return wrapper
    return decorator

def log_action(func):
    def wrapper(employee):
        print(f'Registrando accion para el empleado {employee['name']}')
        return func(employee)
    return wrapper

#El decorador que esta primero tiene la informacion del de adentro
#si el primer decorador es check_acces, la primera funcion que debo crear es check_acces y no log_action
@check_acces('admin')
@log_action
def delete_employee(employee):
    print(f'El empleado {employee['name']} ha sido eliminado')

admin = {'name': 'Carlos', 'role': 'admin'}
employee = {'name': 'Ana', 'role': 'employee'}

delete_employee(admin)
    #Como funciona. primero verifica que el rol es admin, y luego ejecuta su log, y luego elimina
#delete_employee(employee)
