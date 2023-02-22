# Tabela de preços com tupla
print(f'{"TABELA DE PREÇOS":^35}')#colocar no centro o titulo
print('' * 20)
tabela = ('Readset', 289.89,
          'Teclado', 280.50,
          'Mouse', 149.99,
          'Monitor', 899.99,
          'Placa de vidéo', 5000,
          'Mesa', 3800,
          'Cadeira', 1889.99,
          'Mousepad', 89.90)
for posição in range(0, len(tabela)):
    if posição % 2 == 0:
       print(f'{tabela[posição]:.<30}', end='')
    else:
        print(f'R${tabela[posição]:>5.2f}')




