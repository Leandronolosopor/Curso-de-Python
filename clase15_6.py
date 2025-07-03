#Generar un generadro "def" para pares y otro para impares
def pares(limit):
    a = 0
    while a < limit + 1:
        yield a
        a += 2

for a in pares(10):
    print(a)

def impares(limit2):
    b = 1
    while b < limit2:
        yield b
        b += 2
for b in impares(10):
    print(b)
