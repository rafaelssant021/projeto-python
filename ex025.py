print('{:=^40}'.format(' LOJAS SANT '))
valor = float(input('valor da compra: R$'))
print(''' FORMAS DE PAGAMENTO 
[ 1 ] a vista dinheiro/pix
[ 2 ] 2x no cartao
[ 3 ] 3x ou mais no cartao''')
opçao = int(input('qual a opçao? '))
if opçao == 1:
    total = valor - (valor * 10 / 100)
elif opçao == 2:
    total = valor
    parcela = total / 2
    print('sua compra sera parcelada em 2x de R${:.2f}.'.format(parcela))
elif opçao == 3:
    total = valor + (valor * 20 / 100)
    totpar = int(input('quantas parcelas? '))
    parcela = total / totpar
    print('sua compra sera parcelada em {}x de R${:.2f} com juros.'.format(totpar, parcela))
print('sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, total))