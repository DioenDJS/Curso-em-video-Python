"""
Faça um programa que leia o peso de cinco pessoas No final mostre qual
foi o maior e o menor peso lidos
"""

maiorPeso = menorPeso = 0


for person in range(1, 6):
    peso = float(input(f"Digite o peso da pessoa {person}º :"))
    if peso > maiorPeso:
        maiorPeso = peso
    if peso < menorPeso:
        menorPeso = peso

print(f'Menor peso {menorPeso}, e o maior peso {maiorPeso}')