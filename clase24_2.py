"""
Reto
Desarrolla una concesionaria de vehículos en la cual se puedan gestionar las compras y ventas de vehículos.
Un usuario podrá ver los vehículos disponibles, su precio y realizar la compra de uno. Aplica los conceptos
de programación orientada a objetos vistos en este ejercicio.
"""
class Concesionaria:
    def __init__(self):
        self.autos = []
        self.usuarios = []
    
    def agregarAuto(self, vehiculos):
        self.autos.append(vehiculos)
        print(f'El auto {vehiculos.marca}, modelo {vehiculos.modelo} ha sido agregado')

    def autosTotales(self):
        print('Autos disponibles:')
        i = 0
        for vehiculos in self.autos:
            i += 1
            if vehiculos.disponible:
                print(f'{i} Auto {vehiculos.marca}, modelo {vehiculos.modelo}, precio {vehiculos.precio}')

    def agregarUsuario(self, usuario):
        self.usuarios.append(usuario)
        print(f'El usuario {usuario.nombre}, con {usuario.id_usuario} ha sido agregado')     

        
class Vehiculos:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.disponible = True

    def venta(self):
        if self.disponible:
            self.disponible = False
            print(f'El auto {self.marca}, modelo {self.modelo} ha sido vendido')
        else:
            print(f'No hay modedelos disponibles del {self.marca} {self.modelo}')


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario

    def disponibilidad(self, vehiculos):
        if vehiculos.disponible:
            print(f'El auto {vehiculos.marca} {vehiculos.modelo} tiene un precio de {vehiculos.precio}')
        else:
            print(f'No hay disponibilidad del auto {vehiculos.marca} {vehiculos.modelo}')

    def compra(self, vehiculos):
        if vehiculos.disponible:
            vehiculos.venta()
            print(f'Compraste el auto por un valor de {vehiculos.precio}')
        else:
            print(f'No hay disponibilidad del auto {vehiculos.marca} {vehiculos.modelo}')

#creo auto

auto1 = Vehiculos('Toyota', 'Yaris', 7000)
auto2 = Vehiculos('Fiat', 'Palio', 5000)
auto3 = Vehiculos('Toyota', 'Hightlux', 10000)
auto4 = Vehiculos('Ferrari', 'GT200', 200000)

#creo usuario

usuario1 = Usuario('Leandro', 'id: 01020313')
usuario2 = Usuario('Maximiliano', 'id: 01020350')
usuario3 = Usuario('Manuel', 'id: 01020323')

#Creo consecionaria

concesionaria = Concesionaria()
concesionaria.agregarAuto(auto1)
concesionaria.agregarAuto(auto2)
concesionaria.agregarAuto(auto3)
concesionaria.agregarAuto(auto4)

concesionaria.agregarUsuario(usuario1)
concesionaria.agregarUsuario(usuario2)
concesionaria.agregarUsuario(usuario3)

#Mostrar autos
concesionaria.autosTotales()
print('')

#Consultar disponibilidad
usuario1.disponibilidad(auto3)
print('')

#Realizar compra
usuario1.compra(auto3)
print('')

#Consultar disponibilidad
usuario2.disponibilidad(auto3)
print('')

#Mostrar autos
concesionaria.autosTotales()
print('')

