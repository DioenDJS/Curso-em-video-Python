import math
"""
Faça um programa que leia um ângulo qualquer e mostre na
tela o valor do seno cosseno e tangente desse ângulo
"""

grau = float(input("Digite o ângulo : "))

cosseno = math.cos(math.radians(grau))
seno = math.sin(math.radians(grau))
tangente = math.tan(math.radians(grau))

print("O ângulo de {:.0f}º graus tem o seno {:.2f} o cosseno {:.2f} e a tangencia {:.2f}".format(grau, seno, cosseno, tangente))

