from random import shuffle
"""
O mesmo professor do desafio anterior quer sortear
a ordem de apresentação de trabalhos dos alunos
Faça um programa que leia o nome dos quatro alunos
e mostre a ordem serteada.
"""

aluno1 = input("Digite o nome do aluno um : ")
aluno2 = input("Digite o nome do aluno dois : ")
aluno3 = input("Digite o nome do aluno tres : ")
aluno4 = input("Digite o nome do aluno quatro : ")

alunos = [aluno4, aluno3, aluno2, aluno1]

shuffle(alunos)

print("Ordem de alunos : ", end='')
print(alunos)
