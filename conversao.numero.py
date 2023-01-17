 # programa  que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um numero: '))
print('''Escolha uma das bases para conversão:'
 [ 1 ] converter para BINÁRIO
 [ 2 ] converter para OCTAL 
 [ 3 ] converter para HEXADECIMAL ''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print('{} convertido para OCTA é igual a {}'.format(numero, oct (numero)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção invalida, tente novamente.')

