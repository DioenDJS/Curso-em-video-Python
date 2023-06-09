"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
Considere:
USS1.00 = R$3.27
"""

valorCarteira = float(input('Digite quando vc tem em dinheiro em sua carteira : '))

quantidade = valorCarteira / 3.27

print('Podera ser comprado USS{:.2f} dolares '.format(quantidade))
