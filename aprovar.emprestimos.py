# um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor do empréstimo, o salário do solicitador e em quantos anos ele vai pagar.  será negado.

empréstimo = float(input('Qual o valor que você deseja emprestar? R$ '))
salário = float(input('Qual seu salário? R$'))
anos = int(input('Quantos vezes você deseja em pagar? R$ '))
prestação = empréstimo / (anos * 12)
mínimo = salário * 30 / 100
print('Para seu empréstimo de R${:.2f} em {} anos, '.format(empréstimo, anos), end='')
print('O valor da parcela será de R${:.2f}, por mês! '.format(prestação))
if  prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO!')



