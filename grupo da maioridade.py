# Programa que leia o ano de nascimento de dez pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year # pegar ano atual
totalmaior = 0
totalmenor = 0
for pessoa in range(1, 11):
    nasc = int(input('Qual ano a {}ª pessoa nasceu? '.format(pessoa)))
    idade = atual - nasc
    if idade >= 18:
       totalmaior += 1
    else:
       totalmenor += 1
print('No total teve {} pessoas maiores de idade.'.format(totalmaior))
print('No total teve {} pessoas menores de idade.'.format(totalmenor))


