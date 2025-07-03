#Uso de property, el decorador

class Employee:
    #Estamos recibiendo 2 atributos, un nombre y un salario
    #en el caso de salario estamos diciendo que va a ser un atributo protegido, no privado, pero si protegido
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary 

    #estamos diciendo con este decorador que el mothodo sera de tipo getterm osea que nos va a retornar
    # la informacion
    @property
    def salary(self):
        #esta funcion retornara el atributo protegido
        return self._salary

    #Aca que estamos cambiando o modificando el atributo
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = new_salary

    #Y aca estamos diciendo que se elimine
    @salary.deleter
    def salary(self):
        print(f"The salary of {self.name} has been deleted")
        del self._salary

# Crear instancia de Employee
employee = Employee("Ana", 5000)
print(employee.salary)  
    # Y aca nos devuelve el salario

# Modificar el salario de forma controlada
employee.salary = 6000
print(employee.salary)  

# Intentar establecer un salario negativo
employee.salary = -1000  
    #Y esto dara value error
# Eliminar el salario
del employee.salary 
    #Y aca eliminamos el salario de ana