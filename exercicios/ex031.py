"""
Desenvolva um programa que pergunte a distancia de uma viagem em Km
Calcule o preço da passagem cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 para viagens mais longas.
"""

distanciaViagem = int(input("Distancia da viagem : "))

valorPassagem = 0

valorPassagem = distanciaViagem * 0.50

if distanciaViagem > 200:
    valorPassagem = distanciaViagem * 0.45

print("O percurso da viagem vai ser de {}Km com o custo de R$ {:.2f} ".format(distanciaViagem, valorPassagem))