"""
Crie um programa que leia o nome completo de uma pessoa e mostre:

> O nome com todas as letras maiúsculas

> O nome com todas minúsculas

> Quantas letras ao todo(sem considerar espaços)

> quantas letras tem o primeito nome
"""

nomeCompleto = str(input("Digite seu nome completo : "))

nomeCompletoSeparados = nomeCompleto.split()
nomeCompletoSemEspaço = "".join(nomeCompletoSeparados)
quantasLetrasTemNoNome = len(nomeCompletoSemEspaço)

print('O nome em letras Maiúsculas : {}'.format(nomeCompleto.upper()))
print('O nome em letras Minúsculas : {}'.format(nomeCompleto.lower()))
print('Total de letras no nome : {}'.format(quantasLetrasTemNoNome))
print('Primeiro nome : {}'.format(len(nomeCompletoSeparados[0])))


