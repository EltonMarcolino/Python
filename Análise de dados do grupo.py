# Programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

total18 = 0
totalhomens = 0
totalmulher20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totalhomens += 1
    if sexo == 'F' and idade < 20:
        totalmulher20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
            break
print(f'Total de pessoas maior de 18 anos: {total18}')
print(f'O total de Homens acadastrados:  {totalhomens}')
print(f'Temos  {totalmulher20}  Mulheres menores de 20 anos.')

