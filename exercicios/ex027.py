"""
Faça um programa que leia o nome completo de uma pessoa, mostrando
em seguida o primeiro e o ultimo nome separadamente.

Ex: Ana Maria de Souza
primeiro=Ana
ultimo=Souza
"""

nomeCompleto = input("Digite o nome completo : ")

nomeSeparado = nomeCompleto.split()

primeiro = nomeSeparado[0]
ultimo = nomeSeparado[len(nomeSeparado) - 1]

print("Nome: {} \nprimeiro = {} \nultimo = {}".format(nomeCompleto, primeiro, ultimo))

