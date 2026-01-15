nota1 = float(input('primeira nota: '))
nota2 = float(input('segunda nota: '))
nota3 = float(input('terecira nota: '))
media = (nota1 + nota2 + nota3) / 3
print('a sua media foi de {:.1f}'.format(media))
if media >= 6:
    print('parabens voce foi aprovado!')
elif media >=4 and media < 6:
    print('voce ficou de recuperação.')
elif media < 4:
    print('voce foi reprovado.')