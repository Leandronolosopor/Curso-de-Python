#Decoradores en POO
class Caluculator:

    @staticmethod#Este decorador es cuando no estamos interactuando con otros atibutos ni clases
    def add(a: int, b: int) -> int:
        return a + b
