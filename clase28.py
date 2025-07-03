#La funcion super() en python permite que una subcalse acceda y exitienda los metodos
# y atributos de su superclase sin referencialos explicitamente

#Construcutor es el que dice que inicie la informacion

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print('Hello! I am a person.')
    
class Student(Person):#Ya aca estamos aclarando herencia
    def __init__(self, name, age, student_id):#Tengo que pedir exactamente los mismso atributos que persona pero un estudiante
        #Tiene un id tambien, asi que deberemos usar el super() para poder modificarlo
        #para eso tenemos que llamar a su metodo constructor y tengo que ponerle los atributos
        #que conforman a la clase padre
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):#Ahora, el estudiante tiene que decir mas que es una persona
        super().greet()#por eso tambien se usa super, porque voy a modificar el metodo de saludo de persona
        print(f'Hello, my student ID is {self.student_id}')

student = Student('Ana', 20, 'S123')#esta informacion hara referencia a la clase padre por lo tanto le dara a person tambien estos atributos
student.greet()#Hello! I am a person.
        #Hello, my student ID is S123 
        #Si, ejecuta ambos greet
