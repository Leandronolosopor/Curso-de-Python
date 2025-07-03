#Metodos estaticos y de clase en Python
class Order:

    @staticmethod
    def calculate_tax(amount, tax_rate):
    #A este metodo no le estamos poniendo self, eso es porque este metodo podra ser consultado
    # desde afuera sin realizar una instancia de la clase
        return amount * (tax_rate / 100)

#cuando queremos llamar a este metodo estatico lo hacemos llamando a la clase y luego al metodo
print(Order.calculate_tax(1000, 18))
    #el staticmethod es el que permite acceder directamente al methodo sin instanciar la clase
