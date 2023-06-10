from math import trunc
"""
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

Ex:
Digite um número:6.127
O número 6.127 tem a parte inteira 6.
"""

numReal = float(input('Digite um número : '))

parteInteira = trunc(numReal)

print("O número {} tem a parte inteira {}.".format(numReal, parteInteira))