"""
Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
"""

metros = float(input('Digite o valor em metros : '))

centimetros = metros * 100

milimetros = metros * 1000

print('convertendo {} metros em {:.0f} centimetros e em milimetros {:.0f}'.format(metros, centimetros, milimetros))