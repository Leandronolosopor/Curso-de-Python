jugador1 = input('Jugador 1, elija piedra, papel o tijera: ')
jugador2 = input('Jugador 2, elija piedra, papel o tijera: ')

if jugador1 == 'piedra':
    if jugador2 == 'piedra':
        print('Empate, ambos elijieron piedra')
    elif jugador2 == 'papel':
        print('Gana el jugador 2')
    elif jugador2 == 'tijera':
        print('Gana el jugador 1')
    else:
        print('El jugador 2 escribio mal su eleccion')

elif jugador1 == 'papel':
    if jugador2 == 'piedra':
        print('Gana el jugador 1')
    elif jugador2 == 'papel':
        print('Empate, ambos elijieron papel')
    elif jugador2 == 'tijera':
        print('Gana el jugador 2')
    else:
        print('El jugador 2 escribio mal su eleccion')

elif jugador1 == 'tijera':
    if jugador2 == 'piedra':
        print('Gana el jugador 2')
    elif jugador2 == 'papel':
        print('Gana el jugador 1')
    elif jugador2 == 'tijera':
        print('Empate, ambos elijieron tijera')
    else:
        print('El jugador 2 escribio mal su eleccion')
else:
    print('El jugador 1 escribio mal su eleccion')