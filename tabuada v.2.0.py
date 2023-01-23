# Mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

numero = int(input('Digite um número: '))
for n in range(1, 11):
    print('{} x {:2} = {}'.format(numero, n, numero*n))