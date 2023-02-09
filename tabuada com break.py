# Programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    numero = int(input('Digite um número para tabuada: '))
    if numero < 0:
        break
    print('-' * 20)
    for contagem in range(1, 11):
        print(f'{numero} x {contagem} = {numero*contagem}')
    print('-' * 20)
print('Operação finalizado!')

