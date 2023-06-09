"""
Crie um algoritmo que leia um número e mostre o seu dobro triplo e raiz quadrada.
"""

num = int(input('Digite um número : '))

numDobro = num * 2
numTriplo = num * 3
numRaiz = num ** (1/2)
print('O dobro do valor {} é : {} o triplo é : {} e a raiz quadrada é : {:.3} '.format(num, numDobro, numTriplo, numRaiz))