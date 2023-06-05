"""
Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
"""

metros = float(input('Digite o valor em metros : '))

centimetros = metros * 100

milimetros = metros * 1000

print('convertendo {} metros em {} centimetros e em milimetros {}'.format(metros, centimetros, milimetros))