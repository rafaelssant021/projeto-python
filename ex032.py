from random import randint
v = 0
while True:
    player = int(input('diga um valor: '))
    pc = randint(0,10)
    tot = player + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('par ou impar? [P/I] ')).strip().upper()[0]
    print(f'voce jogou {player} e o computador {pc}. total de {tot}')
    if tipo == 'P':
        if tot % 2 == 0:
            print('voce venceu!')
            v += 1
        else:
            print('voce perdeu!')
            break
    elif tipo == 'I':
        if tot % 2 == 1:
            print('voce venceu!')
            v += 1
        else:
            print('voce perdeu!')
            break
    print('vamos jogar novamente...')
print(f'GAME OVER! voce venceu {v} vezes.')