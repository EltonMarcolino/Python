# mostrar que tipo de triângulo será formado:

print('-=-'*20)
print('Analisando o triangulo')
print('-=-'*20)
r1 = float(input('Qaual o tamanho da primeira reta? '))
r2 = float(input('Qual o tamanho da segunda reta? '))
r3 = float(input('Qual o tamanho da terceira reta? '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Suas retas podem formar um triângulo!', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO! ')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO! ')
    else:
        print('ISÓSCELES! ')
else:
    print('Suas retas não podem formar um triângulo!')
