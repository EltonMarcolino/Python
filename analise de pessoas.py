# Programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulher20 = 0
for p in range(1, 5):
    print('  {}ª PESSOA  '.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff'and idade < 20:
        totalmulher20 += 1
médiaidade = somaidade / 4
print('A média de Idade do grupo é de {} anos'.format(médiaidade))
print('O Homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('O total de mulheres menores de 20 anos é {}.'.format(totalmulher20))

