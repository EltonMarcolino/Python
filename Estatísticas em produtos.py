# Programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#  qual é o total gasto na compra.
#  qual é o produto mais caro.
#  qual é o nome do produto mais barato.

total = 0
produtomaiscaro = 0
produtomaisbarato = 0
contador = 0
barato = ''
while True:
    produto = str(input('Produto: '))
    preço = float(input('Preço R$: '))
    contador += 1
    total += preço
    if contador == 1:
        produtomaisbarato = preço
        barato = produto
    else:
        if preço < produtomaisbarato:
            produtomaisbarato = preço
            barato = produto
    if contador == 1:
        produtomaiscaro = preço
    else:
        if preço > produtomaiscaro:
            produtomaiscaro = preço
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
print('{:-^30}'.format('Operação finalizado!'))
print(f'Total da compra é R${total:.2f}')
print(f'O produto mais caro é R${produtomaiscaro:.2f} ')
print(f'O produto mais barato é {barato}, que custa R${produtomaisbarato:.2f}')


