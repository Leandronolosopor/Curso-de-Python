class Employee:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.skills = args
        self.detail = kwargs
    
    def show_employee(self):
        print(f'Employee: {self.name}')
        print('Skills', self.skills)
        print('Details', self.detail)

#python, java y c++ como no son posicionales va a pasar directo a args
#y age y city que estamos mandando de manera directa iran a kwargs
employee = Employee('Leandro', 'Python', 'Java', 'C++', age = 26, city = 'CABA')
employee.show_employee()
#Como se ve en este resultado guardo skills en una lista y datils en un diccionario como es que funciona
# osea *args guarda listas y **kwargs diccionarios
""" 
Employee: Leandro
Skills ('Python', 'Java', 'C++')   
Details {'age': 26, 'city': 'CABA'}

"""