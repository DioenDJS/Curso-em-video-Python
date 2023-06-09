"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
"""

largura = float(input('Digite a largura da parede : '))
altura = float(input('Digite a altura da parede : '))

area = largura * altura

litros = area / 2

print('A parede de {} largura por {} de altura tem uma area de {}m² e vai precisar de {} litros de tinta '.format(largura, altura, area, litros))

