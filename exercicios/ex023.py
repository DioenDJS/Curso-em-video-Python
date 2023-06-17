"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

Ex:
Digite um número:1834

unidade:4
dezena:3
centena:8
milhar:1
"""
print('Digite um número ate 4 digitos ex: 9999 ')
num = int(input('Digite o número : '))
# numString = str(num)

# Refatorando com a solução do Gustavo Guanabara
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

# unidade = numString[3]
# dezena = numString[2]
# centena = numString[1]
# milhar = numString[0]

print('unidade:{} \ndezena:{} \ncentena:{} \nmilhar:{}'.format(unidade, dezena, centena, milhar))