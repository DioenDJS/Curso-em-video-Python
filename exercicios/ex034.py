"""
Escreva um programa que pergunta o salário de um funcionário e calcule o valor do seu aumento
Para salãrios superiores a R$1.250.00, calcule um aumento de 10%
Para os inferiores ou iguais , o aumento é de 15%
"""

salario = float(input("Digite o salario : "))

novoSalario = 0

if salario > 1250:
    novoSalario = salario * 10 / 100 + salario
else:
    novoSalario = salario * 15 / 100 + salario

print("O seu novo salario e {:.2f} ".format(novoSalario))
