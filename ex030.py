from time import sleep
valor1 = int(input('primeiro valor: '))
valor2 = int(input('segundo valor: '))
opçao = 0
while opçao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa''')
    opçao = int(input('>>>>> qual a sua opção? '))
    if opçao == 1:
        soma = valor1+valor2
        print('a soma de {} e {} é {}'.format(valor1, valor2, soma))
    elif opçao == 2:
        mult = valor1*valor2
        print('a multiplicação de {} e {} é {}'.format(valor1, valor2, mult))
    elif opçao == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('entre {} e {} o maior valor é {}'.format(valor1,valor2,maior))
    elif opçao == 4:
        print('informe os valores de novo: ')
        valor1 = int(input('primeiro valor: '))
        valor1 = int(input('segundo valor: '))
    elif opçao == 5:
        print('finalizando...')
    else:
        print('opçao invalida. tente novamente')
    print('=-=' * 10)
    sleep(2)
print('fim do programa')