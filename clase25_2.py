#Ahora vamos  a ver la herencia
#vamos a decir que esta concecionaria tambien vende bicis y alquila autos, y vende camiones
class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True
    #las classes que hereden heredan todos lso methodos
    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f'El vehiculo {self.brand}. Ha sido vendido')
        else:
            print(f'El vehiculo {self.brand}. No esta disponible')
    
    def check_Available(self):
        return self.is_available#retornamos el estado de disponible o no disponible
    
    def get_price(self):#cuando queremos devolver el valor de un parametro usamos el methodo "get"
        return self.price
    
    def star_engine(self):
        raise NotImplementedError('Este metodo debe ser implementado por la subclase')
        #Raise define una exepcion, que hace que cuando se ejecute algo en el codigo lo detenga
    
    def stop_engine(self):
        raise NotImplementedError('Este metodo debe ser implementado por la subclase')
    
#ahora si haremos herencia de una clase que hereda de una super clase
class Car(Vehicle):#cuando creamos una herencia es necesario ponerle metodos
    #y aca solo estaremos modificando los metodos de la clase padre 
    def star_engine(self):
        if not self.is_available:
            return f'El motor del coche {self.brand} esta en marcha'
        else:
            return f'El coche {self.brand} no esta disponible'
        
    def stop_engine(self):
        if self.is_available:
            return f'El motor del coche {self.brand} se ha detenido'
        else:
            return f'El coche {self.brand} no esta disponible'

class Bike(Vehicle):
    def star_engine(self):
        if not self.is_available:
            return f'La bicicleta {self.brand} esta en marcha'
        else:
            return f'La bicicleta{self.brand} no esta disponible'
        
    def stop_engine(self):
        if self.is_available:
            return f'La bicicleta {self.brand} se ha detenido'
        else:
            return f'La bicicleta {self.brand} no esta disponible'

class Truck(Vehicle):
    def star_engine(self):
        if not self.is_available:
            return f'El motor del camion {self.brand} esta en marcha'
        else:
            return f'El camion {self.brand} no esta disponible'
        
    def stop_engine(self):
        if self.is_available:
            return f'El motor del camion {self.brand} se ha detenido'
        else:
            return f'El camion {self.brand} no esta disponible'

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = [] #Lista de autos que tiene el consumidor

    def buy_vehicle(self, vehicle: Vehicle):#Aca estoy diciendo que estoy recibiendo el objeto de la clase vehicle
        if vehicle.check_Available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f'Lo siento, {vehicle.brand} no esta disponible')
    
    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_Available():
            availablity = 'Disponible'#aca defino la variable
        else:
            availablity = 'No disponible'
        print(f'El {vehicle.brand} esta {availablity} y cuesta {vehicle.get_price()}')#y si no la pongo que aca la llama entonces me mostrara como erro

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []
    
    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f'El {vehicle.brand} ha sido añadido al inventario')

    def add_customers(self, customer: Customer):
        self.customers.append(customer)
        print(f'El {customer.name} ha sido añadido')

    def show_available_vehicle(self):
        print('Vahiculos disponibles en la tienda')
        for vehicle in self.inventory:
            if vehicle.check_Available():
                print(f'- {vehicle.brand} por {vehicle.get_price()}')

#Ahora veremos el polimorfismo
car1 = Car('Toyota', 'Corola', 20000)
bike1 = Bike('Yamaha', 'MT-07', 7000)
truck1 = Truck('Volvo', 'FH16', 80000)

customer1 = Customer('Carlos')

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

#Mostrar vehiculos disponibles
dealership.show_available_vehicle()

#Cliente consultar un vehiculo
customer1.inquire_vehicle(car1)

#Cliente comprar un vehiculo
customer1.buy_vehicle(car1)

#Mostrar vehiculos disponibles
dealership.show_available_vehicle()

#Los 4 pilares de el poo es la encapsulacion
    #Creo variables de instancia y que son privadas del objeto
    #Abstraccion
        #es que a esas variables solo podemos acceder mediante los precios
    #Herencia
        #Es cuando una como Car hereda de la clase padre Vehicle sus atributos
    #Polimorfismo
        #Es que podemos tener muchas formas pero un compartamiento diferente
        #ejemplo el auto tiene el motor en marcha si no esta disponible
        #pero la bici si no esta disponible no es que tiene su motor en macha