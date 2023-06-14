"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.
"""

nome = input('Digite o seu nome completo : ')

resulte = nome.upper().find('SILVA')

verificacao = 'tem' if resulte != -1 else 'não tem'

print('O nome {}, {} a palavra SILVA !'.format(nome, verificacao))
