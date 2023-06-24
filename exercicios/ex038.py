"""
Escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""

numUm = int(input("Digite o primeiro valor : "))
numDois = int(input("Digite o segundo valor : "))

if numUm == numDois:
    print("Não existe valor maior, os dois são iguais")
elif numUm > numDois:
    print("O primeiro valor é maior : {}".format(numUm))
else:
    print("O segundo valor é maior : {}".format(numDois))