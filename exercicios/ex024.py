"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
"""

nomeCidade = input('Digite o nome da Cidade : ').strip()

nomeCidadeMaiuscula = nomeCidade.upper()

resulte = nomeCidadeMaiuscula.find('SANTO')

encontrado = 'sim' if resulte == 0 else 'não'

print('A cidade {}, {} começa com a palavra SANTO'.format(nomeCidade, encontrado))