#POO de una biblioteca

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True#Este boole es para decir si esta disponible o no

    def borrow(self):#Prestar libro
        if self.available:#Si esta disponible
            self.available = False#Volverlo false
            print(f'El libro {self.title} ha sido prestado')#Y decir que se presto
        else:#Si esta en False porque se presto entonces se dice que no esta disponible
            print(f'El libro {self.title} no esta disponible')
    
    def return_book(self):#devolver libro
        self.available = True#se cambia a true para poder prestarse de vuelta
        print(f'El libro { self.title} ha sido devuelto')

class User:#clase de usuario
    def __init__(self, name, user_id):
        self.name = name#nombre
        self.user_id = user_id#su id 
        self.borrowed_books = []#una lista con los libros que tomo prestados
    
    def borrow_book(self, book):#pedir prestado el libro
        if book.available:#vemos que esta disponible
            book.borrow()#libro se presta ejecuntando el methodo prestar de libro
            self.borrowed_books.append(book)#agrego el libro a libros que tiene el usuario
        else:
            print(f'El libro {book.title} No esta dispnible')

    def return_book(self, book):#devolver libro
        if book in self.borrowed_books:#si el libro esta dentro de los que me prestaron.
            book.return_book()#Estamos diciendo que se retorne de book, por eso es book., y cambiara a true el libro
            self.borrowed_books.remove(book)#Digo que en los libros que me estoy prestando, remueva este libro
        else:
            print(f'El libro {book.title} No esta en la lista de presados')

class Library:#Bibiloteca
    def __init__(self):
        self.books = []#lista de los libros
        self.users = []#lista de los usuarios
    
    def add_book(self, book):#agregar libro a la biblioteca
        self.books.append(book)#agrego un libro a la biblioteca, notece que digo books por lo tanto estoy llamando a la lista que cree que es el unico que es book en prural
        print(f'El libro {book.title} ha sido agregado')

    def register_user(self, user):#registo usuario en la biblioteca
        self.users.append(user)#aca lo agrego a la lista de usuario
        print(f'El usuario { user.name} ha sido registrado')
    
    def show_available_books(self):#aca muestro los libros disponibles
        print('Libros disponibles:')
        for book in self.books:#aca digo que para cada libro que este en mis propios libros agregados
            if book.available:#y si el libro esta disponible
                print(f'{book.title} por {book.author}')#entonces imprime su titulo y autor

#ahora, todo esto son clases, ahora tengo que creear los objetos
#primero debo ver que si creeo un libro, que variables le puse para saber que le paso
    #como puse title, author, tengo que pasarle el titulo y luego el autor porque sino
    #guardara en titulo algo que no va
#Crear los libros
book1 = Book('El principito', 'Antoine de Saint-Exupéry')#agrego libros
book2 = Book('1984', 'George Orwell')

#Crear usuario
user1 = User('Leandro',  '001')#agrego un usuario y su id

#Crear Biblioteca
library = Library()#creo una libreria
library.add_book(book1)#le agrego libros
library.add_book(book2)
library.register_user(user1)#le agrego el usuario

#Mostrar libros
library.show_available_books()

#Realizar prestamo
user1.borrow_book(book1)

#Mostrar libros
library.show_available_books()

#Devolver libro
user1.return_book(book1)

#Mostrar libros
library.show_available_books()