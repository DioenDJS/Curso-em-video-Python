"""
Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
"""

num = int(input('Digite um numero : '))

for i in range(11):
  if i < 10:
    print('{} x {:2} = {}'.format(num, i, (i * num)))
  else:
    print('{} x {} = {}'.format(num, i, (i * num)))


