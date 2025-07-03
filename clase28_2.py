class LivingBeing:#ser vivo
    def __init__(self, name):#crea con el metodo constructor
        self.name = name

class Person(LivingBeing):#crea a la persona como clase hija
    def __init__(self, name, age):#le agrega edad
        super().__init__(name)#para eso llama al metodo cosntructor con un super()
        self.age = age

class Student(Person):#estudiante sale de persona y le agrega id
    #por lo tanto puedo ir haciendo herencias de herencias anteriores
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, and my student ID is {self.student_id}")
    
student = Student("Carlos", 21, "S54321")
student.introduce()  