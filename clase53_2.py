#Ahora intentaremos ver que pasara si queremos elimnar la informacion pero no establecimos esa propiedad
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary 

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = new_salary


# Crear instancia de Employee
employee = Employee("Ana", 5000)
print(employee.salary)  

# Modificar el salario de forma controlada
employee.salary = 6000
print(employee.salary)  

# Intentar establecer un salario negativo
#employee.salary = -1000  

# Eliminar el salario
del employee.salary  
"""
Y ahora como no establecimos este objeto dira que no puede elimnar algo que no tiene en memoria
"""
