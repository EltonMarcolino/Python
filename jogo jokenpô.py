# programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep # Dá um tempo, para aparecer!
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Escolha:
[ 0 ] PAPEL
[ 1 ] TEROURA
[ 2 ] PEDRA''')
jogador = int(input('Qual você escolhe: PAPEL, TESOURA, PEDRA? '))
print('JO')
sleep(1)
print('ken')
sleep(1)
print('POO..')
print('-' * 11)
print('Computador ESCOLHEU {}'.format(itens[computador]))
print('Você ESCOLHEU {}'.format(itens[jogador]))
print('-' * 11)
if computador == 0: # jogou Papel
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1: # jogou Tesoura
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ VENCEU')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2: # jogou Pedra
    if jogador == 0:
        print('VOCÊ VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')










