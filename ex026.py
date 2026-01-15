from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
pc = randint(0,2)
print('''suas opções
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
eu = int(input('qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*11)
print('computador jogou {}'.format(itens[pc]))
print('jogador jogou {}'.format(itens[eu]))
print('-='*11)
if pc == 0:
    if eu == 0:
        print('empate')
    elif eu == 1:
        print('jogador vence')
    elif eu == 2:
        print('computador vence')
    else:
        print('jogada invalida!')
elif pc == 1:
    if eu == 0:
        print('computador vence')
    elif eu == 1:
        print('empate')
    elif eu == 2:
        print('jogador vence')
    else:
        print('jogada invalida!')
elif pc == 2:
    if eu == 0:
        print('jogador vence')
    elif eu == 1:
        print('computador vence')
    elif eu == 2:
        print('empate')
    else:
        print('jogada invalida!')