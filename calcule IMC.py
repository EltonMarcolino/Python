# Calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

peso = float(input('Qual seu peso? (kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / (altura ** 2)    # pega o peso e divide por altura quadrado.
print('Seu IMC é de {:.1f}'.format(imc))
if  imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif imc >= 18.5 and imc < 25:
    print('PARABÉNS você está na faixa de peso. ')
elif imc >= 25 and imc <= 30:
    print('Você está SOBREPESO. ')
elif imc >= 30 and imc <= 40:
    print('Você está OBESO.')
elif imc > 40:
    print('Você está com OBESIDADE MÓRBIDA, cuidado!')



