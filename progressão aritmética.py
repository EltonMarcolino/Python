# lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} ='.format(termo),end='')
        termo += razão
        contador += 1
    print('PAUSA!')
    mais = int(input('Quantos termos você deseja mostrar mais? '))
print('Progressão realizada com {} termos.'.formT(total))

