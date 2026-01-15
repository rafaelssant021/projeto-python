from datetime import date
ano = int(input('qual o seu ano de nascimento? '))
atual = date.today().year
idd = atual - ano
print('voce nasceu em {} e tem {} anos.'.format(ano,idd))
if idd <= 9:
    print('sua categoria é MIRIM')
elif idd > 9 and idd <= 14:
    print('sua categoria é INFANTIL')
elif idd > 14 and idd <= 19:
    print('sua categoria é JUNIOR')
elif idd > 19 and idd <= 25:
    print('sua categoria é SENIOR')
elif idd > 25:
    print('sua categoria é MASTER')