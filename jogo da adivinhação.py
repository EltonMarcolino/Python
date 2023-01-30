# O computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
ia = randint(0, 10)
print('Sou a MATRIX...Acabei de pensar num número de 0 a 10. ')
print('Será que você consegue adivinhar o número que pensei? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == ia:
        acertou = True
    else:
        if jogador < ia:
            print('Maior, tente de novo!')
        elif jogador > ia:
            print('Menor, tente de novo!')
print('ADIVINHOU com {} tentativas. Parabéns! '.format(palpites))





