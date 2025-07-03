class BankAccount:#Cuenta bancaria
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True #Esto no es necesario tenerlo como parametro, asi que se puede poner aca
            #Hara que la cuentra siempre este activa
    
    def deposit(self, amount):#deposito de dinero
        if self.is_active:#Estamos diciendo que si la cuenta esta activa, osea esta True
            self.balance += amount#entonces le sume al balance el monto depositado
            print(f'Se ha depositado {amount}. Saldo actual {self.balance}')
        else:
            print('No se puede depositar. Cuenta inactiva')
    
    def withdraw(self, amount):#Retiro de dinero
        if self.is_active:#Si la cuenta esta activa
            if amount <= self.balance:#Y el monto es menor o igual al balance
                self.balance -= amount#el nuevo balance sera el balance menos el monto
                print(f'Se ha retirado el {amount}. Saldo actual {self.balance}')
    
    def deactivate_account(self):#Desactivacion de cuenta
        self.is_active = False
        print(f'La cuenta se ha desactivada')
    
    def activate_account(self):#Activacion de cuenta
        self.is_active = True
        print(f'La cuenta se ha activada')

account1 = BankAccount('Ana', 500)
account2 = BankAccount('Luis', 1000)

#Llamada a los metodos
account1.deposit(200)#deposito
account2.deposit(100)#tambien deposito
account1.deactivate_account()#desactivo la cuenta 1
account1.deposit(50)#Intento depositarle a la cuenta 1, pero como esta desactivada me dira que no es posible
"""Se ha depositado 200. Saldo actual 700
        Se ha depositado 100. Saldo actual 1100
        La cuenta se ha desactivada
        No se puede depositar. Cuenta inactiva
        """
account1.activate_account()
account1.deposit(50)# y ahora nos dejara porque la estamos activando.