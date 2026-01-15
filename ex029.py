from random import randint
pc = randint(0,10)
print('sou seu computador... acabei de pensar em um numero entre 0 e 10.')
print('sera que voce consegue adivinhar qual foi? ')
acertou = False
chutes = 0
while not acertou:
    jogador = int(input('qual é o seu palpite? '))
    chutes += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('mais... tente de novo')
        elif jogador > pc:
            print('menos... tente de novo')
print('acertou com {} tentativas'.format(chutes))