"""
Faça um algoritmo que leia o saário de um  funcionário e mostre seu novo salário, com 15% de aumento.
"""

salario = float(input('Digite o salário do funcionário : '))

aumento = (15 / 100) * salario

novoSalario = salario + aumento

print('O salario do funcionario de {}R$ sofreu um aumento de 15% {}R$ ficando em : {}R$'.format(salario, aumento, novoSalario))
