def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)
print_exception_hierarchy(Exception)#Esto nos mostrara en la consola todos las exepciones que podemos usar
    #por ejemplo, nos mostrara que cualquier error se puede evitar si usamos Exeption, pero si son flotantes
    # o zero a la vez y no mas, puedo usar ArithmeticError
