from datetime import date
atual = date.today().year
nasc = int(input('ano de nascimento: '))
idd = atual - nasc
print('quem nasceu em {} tem {} anos no ano de {}'. format(nasc, idd, atual))
if idd == 18:
    print('voce deve se alistar imediatamente.')
elif idd < 18:
    saldo = 18 - idd
    print('ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('seu alistamento sera em {}.'.format(ano))
elif idd > 18:
    saldo = idd - 18
    print('voce deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('seu alistamento foi em {}.'.format(ano))
