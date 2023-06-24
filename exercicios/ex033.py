"""
Faça um programa que leia tres números e mostre qual é o maior e qual é o menor.
"""
numUm = int(input("Digire o numero 1 : "))
numDois = int(input("Digire o numero 2 : "))
numTres = int(input("Digire o numero 3 : "))
maior = 0
menor = 0

if numUm > numDois and numUm > numTres:
    maior = numUm
elif numDois > numUm and numDois > numTres:
    maior = numDois
elif numTres > numUm and numTres > numDois:
    maior = numTres

if numUm < numDois and numUm < numTres:
    menor = numUm
elif numDois < numUm and numDois < numTres:
    menor = numDois
elif numTres < numUm and numTres < numDois:
    menor = numTres

print("Entre os numeros {}, {}, {} o maior numero é {} e o menor {} ".format(numUm, numDois, numTres, maior, menor))