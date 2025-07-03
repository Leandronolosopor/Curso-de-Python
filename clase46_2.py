#solo estamos haciendo una clase que va tener un contador que se va a ir sumando
class Counter:
    count = 0 

    @classmethod
    def increment(cls):
        cls.count += 1
#class method, define que el methodo que estamos difiniendo a cuntinuacion esta modificando el mothodo
# o clase en especifico

#Para ver que se esta llamando al modificador tenemos que llamar a Counter
Counter.increment()
Counter.increment()
Counter.increment()
print(Counter.count)