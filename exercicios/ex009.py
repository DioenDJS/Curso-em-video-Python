"""
Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
"""

num = int(input('Digite um numero : '))

for i in range(11):
        print('{} x {} = {}'.format(num, i, (i*num)))
