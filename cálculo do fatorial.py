# Programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

'''from math import factorial
numero = int(input('Digete um número: '))
fatorial = factorial(numero)
print('O fatorial de {} é {}.'.format(numero, fatorial))'''

numero = int(input('Digite um valor: '))
contador = numero
fatorial = 1
print('Calculando {}! = '.format(numero),end='')
while contador > 0:
    print('{} '.format(contador), end='')
    print('x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print('{}'.format(fatorial))



