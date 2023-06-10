from random import choice
"""
Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
Faça um programa que ajude ele. lendo o nome deles e escrevendo o nome
do escolhido
"""

aluno1 = input("Digite o nome do aluno um : ")
aluno2 = input("Digite o nome do aluno dois : ")
aluno3 = input("Digite o nome do aluno tres : ")
aluno4 = input("Digite o nome do aluno quatro : ")

alunos = [aluno4, aluno3, aluno2, aluno1]

escolhido = choice(alunos)

print("O alunos sorteado : {}".format(escolhido))
