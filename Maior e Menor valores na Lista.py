# Programa que leia  numéros e guarde-os em uma lista. No final, mostre qual foi o maior e o menor número digitado e as suas respectivas posições na lista.

listanumero = []
maiornumero = 0
menornumero = 0
for contador in range(0, 10):
    listanumero.append(int(input('Digite um número: ')))
    if contador ==0:
        maiornumero = menornumero = listanumero[contador]
    else:
        if listanumero[contador] > maiornumero:
            maiornumero = listanumero[contador]
        if listanumero[contador] < menornumero:
            menornumero = listanumero[contador]

print(' ' * 25)
print(f'Os números que Você digitou são {listanumero}')
print(f'Maior número digitado é {maiornumero} nas posições', end=' ')
for i , numero in enumerate(listanumero): # mostrar a posição do maior número.
    if numero == maiornumero:
        print(f'{i},', end='')
print(f'Menor número digitado é {menornumero} na posições', end=' ')
for i, numero in enumerate(listanumero):
    if numero == menornumero:
        print(f'{i} ', end='')
print() # Esse print serve para quebra de linha.








