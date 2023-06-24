"""
Faça um  programa que calcule a soma entre todos os numeros impares que são multiplos de tres e que
se encontram no intervalo de 1 até 500.
"""

for multiplo in range(1, 500):
     if multiplo % 3 == 0:
          print(f"o numero {multiplo} é multiplo de 3 ")