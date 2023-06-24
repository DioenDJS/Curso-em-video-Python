"""
Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa,o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou entao
o emprestimo sera negado.
"""

valorCasa = float(input("Digite o valor da casa R$: "))
salario = float(input("Digite o salario do comprador : "))
anos = int(input("Digite em anos vai ser feito o pagamento : "))

valorAPagarParcelas = valorCasa / (anos * 12)

trintaPorcentoDoSalario = salario * 30 / 100

print("30% do salario do comrador é R${} ".format(trintaPorcentoDoSalario))
print("Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}".format(valorCasa, anos, valorAPagarParcelas))
if trintaPorcentoDoSalario < valorAPagarParcelas:
    print("Emprestimo Negado !")
elif trintaPorcentoDoSalario >= valorAPagarParcelas:
    print("Emprestimo Aprovado !")

