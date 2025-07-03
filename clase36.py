#Proyecto, batalla naval, tengo que crear un batalla naval en base a todo lo que aprendi
#tendre un tablero de 10x10, del 1 al 10 y de la A a la J
#Los barcos deben se de distinto tamaño


class Barco:
    def __init__(self, tamaño, nombre):
        self.tamaño = tamaño
        self.nombre = nombre
        self.barcos = []
        self.golpes = 0

    def ubicacionDelBarco(self, tamaño, nombre, ):
        pass


class Tablero:
    def __init__(self):
        self.posiciones = [[]]
        self.valida = True

    def posicion(self, barco):
        if self.valida:
            self.valida = False
            print(f'Le haz dadado a un barco en la posicion {self.posiciones}')
            barco.vidaBarco()



            
    
class Jugador:
    def __init__(self, bando):
        self.bando = bando
    
    def elegirBando(self, bando):
        bando = input()
        if bando == 'Rojo':
            print ('Usted eligio Rojo')
        elif bando == 'Azul':
            print ('Usted eligio Azul')
        else:
            print('Usted debe elegir Azul o Rojo, respete las mayuscula')

    def Atacar(self, tablero):
        if tablero.posicion():
            pass





