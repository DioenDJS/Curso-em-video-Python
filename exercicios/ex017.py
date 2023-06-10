import math
from math import pow, sqrt
"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um Triângulo
retângulo, calcule e mostre o comprimento da hipotenusa.

                  _____________________________________
    hipotenusa = V   catetoOposto² + catetoAdjacente²  |
    
"""

catetoOposto = float(input('Digite o valor do cateto oposto  : '))
catetoAdjacente = float(input('Digite o valor do cateto adjacente  : '))

# hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)

#         ou

# hipotenusa = pow(catetoOposto, 2) + pow(catetoAdjacente, 2)

# hipotenusa = sqrt(hipotenusa)

hipotenusa = math.hypot(catetoOposto, catetoAdjacente)

print("O valor da hipotenusa do cateto oposto {} e do cateto adjacente {} é : {:.2f}".format(catetoOposto, catetoAdjacente, hipotenusa))
