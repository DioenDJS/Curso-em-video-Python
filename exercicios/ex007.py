"""
Desenvolva um programa que leia as duas notas de um aluno, colcule e mostre a sua média.
"""
import math

notaUm = float(input('Digite a primeira nota : '))
notaDois = float(input('Digite a segunda nota : '))

media = (notaUm + notaDois) / 2

print('A média entre {} e {} é : {:.1f}'.format(notaUm, notaDois, media))
