# Calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros

print('{:^40}'.format(' LOJA DE ROUPAS '))
preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO  
[ 1 ] à vista dinheiro/chque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''') # colocando 3 áspas, posso usar várias linhas
pagamento = int(input('Qual a forma de PAGAMENTO? '))
if pagamento == 1:
    total = preço - (preço * 10 / 100)
elif pagamento == 2:
    total = preço - (preço * 5 / 100)
elif pagamento == 3:
    total = preço
    parcela = total / 2
    print('Sua parcela vai ser 2x de R${:.2f}, SEM JUROS'.format(parcela))
elif pagamento == 4:
    total = preço + (preço * 20 / 100)
    totalparcela = int(input('Quantas parcelas? '))
    parcela = total / totalparcela
    print('Sua compra vai ser parcelada em {}x de R${:.2f}, COM JUROS'.format(totalparcela, parcela))
else:
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} no final, vai custar R${:.2f}.'.format(preço, total))




