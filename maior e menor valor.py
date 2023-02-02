# Programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
resposta = 'S'
soma = média = quantidade = maior = menor = 0
while resposta in 'Ss':
    número = int(input('Digite um número: '))
    soma = soma + número
    quantidade = quantidade + 1
    if quantidade ==1:
        maior = menor = número
    else:
        if número > maior:
            maior = número
        if número < menor:
            menor = número
    resposta = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
média = soma / quantidade
print('Foi digitado {} números, a média é {}'.format(quantidade, média))
print('O maior número é {}, e menor número é {}'.format(maior, menor))


