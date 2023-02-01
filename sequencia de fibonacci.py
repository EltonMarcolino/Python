# Programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

print('-' * 20)
print('Sequência de Fibonacci')
print('-' * 20)
numero = int(input('Quantos termos você deseja mostrar? '))
termo1 = 0
termo2 = 1
print('-' * 20)
print('{} - {} '.format(termo1, termo2), end='')
contador = 3
while contador <= numero:
    termo3 = termo1 + termo2
    print('- {}'.format(termo3), end=' ')
    termo1 = termo2
    termo2 = termo3
    contador += 1
print('FIM!')


