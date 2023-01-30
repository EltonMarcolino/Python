# Programa que leia dois valores e mostre um menu na tela

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5: # diferente é o ponto de exclamação
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair da Programa ''')
    opção = int(input('Qual sua opção? '))
    if opção == 1:
       soma = n1 + n2
       print('A soma entre {} + {} igual {}'.format(n1, n2, soma))
    elif opção == 2:
       multiplicar = n1 * n2
       print('{} x {} igual {}'.format(n1, n2, multiplicar))
    elif opção == 3:
       if n1 > n2:
           maior = n1
       else:
           maior = n2
       print('Entre {} e {} maior é {}'.format(n1, n2, maior))
    elif opção == 4:
       print('Informe os valores novamente! ')
       n1 = int(input('Primeiro valor: '))
       n2 = int(input('Segundo valor: '))
    elif opção == 5:
       print('Finalizado!')
    else:
        print('Opção invalido. Tente outro!')
    print('=-=' * 10)
    sleep(1)
print('Você escolheu a opção sair. Obrigado!')