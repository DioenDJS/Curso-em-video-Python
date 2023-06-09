"""
Faça um algoritmo que leia a temperatura em Celsius e mostre em Fahrenheit.
"""

celsius = float(input('Informe a temperatura em ºC : '))

fahrenheit = celsius * 1.8 + 32  # outra forma (9 * celsius) / 5) + 32

print('A temperatura de {}ºC corresponde a {}ºF!'.format(celsius, fahrenheit))
