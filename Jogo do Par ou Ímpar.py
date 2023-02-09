# Jogue par ou ímpar, o jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
vitoria = 0
while True:
    jogador = int(input('Digite um numero: '))
    matrix = randint(0, 10)
    total = jogador + matrix
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e matrix jogou {matrix}. Total de é {total} pontos, ', end= '')
    print('Deu PAR' if total % 2 == 0 else 'deu ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos tentar de novo?')
print(f'GAME OVER. Você venceu {vitoria} vezes. ')