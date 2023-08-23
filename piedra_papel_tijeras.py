import random as selec


def juego_piedra_papel_tijeras ():
    print('________Piedra, papel y tijeras_________')
    print('     Gana el mejor de tres intentos     ')
    print('')
    
    opciones = ['','piedra','papel','tijeras']
    win_player = []
    win_ia = []
    
    while len(win_ia) < 3 and len(win_player) < 3:
        player = input('Elige entre 1: piedra, 2: papel o 3: tijeras: ')
        ia = opciones[selec.randint(1,3)]
        
        # validacion
        if player == '1' or player == '2' or player == '3':
            player = opciones[int(player)]
        else:
            print('Ingrese un valor valido')
            continue
        # empate
        if ia == player:
            print(f'elegiste: {player}, la IA: {ia}')
            print('Empate')
            print('')
            continue
        # gana ia
        elif (player == 'piedra' and ia == 'papel') or (player == 'papel' and ia == 'tijeras') or (player == 'tijeras' and ia == 'piedra'):
            win_ia.append('*')
            print(f'elegiste: {player}, la IA: {ia}')
            print('Gana la IA')
            print('')       
        # gana el player
        else:
            win_player.append('*')
            print(f'elegiste: {player}, la IA: {ia}')
            print('Gana el jugador')
            print('')
        # Contador
        print(f'Contador ----- IA: {len(win_ia)}')
        print(f'Contador ----- Jugador: {len(win_player)}')
        print('')
    # Mostrar ganador
    if len(win_ia) == 3:
        print('')            
        print('----- El juego lo gano la IA -----')
        print('')
    else:
        print('')
        print('----- El juego lo gano el jugador -----')
        print('')
        
    jugar_de_nuevo()

def jugar_de_nuevo ():
    print('')
    res = input('Presione Enter para salir, escriba cualquier letra para jugar de nuevo')
    print('')
    
    if res == '':
        print('Hasta la proxima')
        print('')
    else:
        juego_piedra_papel_tijeras()
        

juego_piedra_papel_tijeras()