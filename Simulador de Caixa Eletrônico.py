# Programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$2.

print('{:^40}'.format('Banco do Brasil'))
print(' ' * 20)
valor = int(input('Quantos deseja sacar? '))
total = valor
cédula = 50
totalcédula = 0
while True:
    if total >= cédula:
        total -= cédula
        totalcédula += 1
    else:
        if totalcédula > 0:
            print(f'São {totalcédula} cédulas de R${cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 2
        totalcédula = 0
        if total == 0:
            break
print('Finalizado a Operação!')



