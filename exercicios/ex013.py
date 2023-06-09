"""
Faça um algoritmo que leia o saário de um  funcionário e mostre seu novo salário, com 15% de aumento.
"""

salario = float(input('Digite o salário do funcionário : '))

aumento = (salario * 15) / 100

novoSalario = salario + aumento

print('O salario do funcionario de {:.2f}R$ sofreu um aumento de 15% {:.2f}R$ ficando em : {:.2f}R$'.format(salario, aumento, novoSalario))
