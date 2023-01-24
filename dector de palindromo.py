# Programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase: ')).strip().upper() # tira espaços, coloca maiusculo.
palavras = frase.split()
junto = ''.join(palavras) # junta as palavras
inverso = ''
for letra in range(len(junto)  -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('É uma frase  PALÍNDROMO!')
else:
    print('Não é uma frase PALÍNDROMO!')
