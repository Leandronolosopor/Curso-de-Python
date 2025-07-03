#Ahora veremos decorador con accesos de administrador o no para eliminar un usuario
#Para que se entienda, la segunda funcion, delete_employee es mi funcion original
# despues creo una funcion arriba que es algo que extiende a la funcion original que a 
# nivel visual se vera como la segunda
def check_acces(func):
    def wrapper(employee):#no es necesario darle un parametro, pero aqui yo quiero que reciba la totalidad del diccionario
        # Comprobar si el empleatdo tiene rol 'admin'
        if employee.get('role') == 'admin':#consulta si el empleado tiene en la llave rol, el valor admin
            return func(employee)#Y si es asi le retornaremos la funcion
        else:
            print('ACCESO DENEGADO. Solo los administradores pueden acceder.')
    return wrapper


@check_acces
def delete_employee(employee):
    print(f'El empleado {employee['name']} ha sido eliminado')

admin = {'name': 'Carlos', 'role': 'admin'}
employee = {'name': 'Ana', 'role': 'employee'}

delete_employee(admin)
delete_employee(employee)
