from random import randint
computador = randint(0, 10)
print('-=-' *20)
print('vou pensar em um numero de 0 e 10, tente adivinhar...')
print('-=-' *20)
jogador = int(input('em que numero eu pensei?  '))
if jogador == computador:
    print('paraben! vc conseguiu me vencer.')
else:
    print('ganhei! eu pensei no numero {}'.format(computador))