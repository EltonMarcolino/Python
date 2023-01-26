# Programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maiorpeso = 0
menorpeso = 0
for p in range(1, 7):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print('O maior peso lido foi de {}kg'.format(maiorpeso))
print('O menor peso lido foi de {}kg'.format(menorpeso))








