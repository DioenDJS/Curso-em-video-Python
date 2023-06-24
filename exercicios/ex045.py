from random import choice
"""
Crie um programa que faça o computador jogar jokenpo com vccê
"""

suaJogada = str(input("digite sua jogada : "))

lista = ["pedra", "papel", "tesoura"]
suaJogadaMaquina = choice(lista)
vence = ""
jogo = suaJogada + " X " + suaJogadaMaquina
print(jogo)
if jogo == "pedra X papel" or jogo == "papel X pedra":
    vence = "papel"
elif jogo == "pedra X tesoura" or jogo == "tesoura X pedra":
    vence = "pedra"
elif jogo == "tesoura X papel" or jogo == "papel X tesoura":
    vence = "tesoura"
elif jogo == "tesoura X tesoura" or jogo == "papel X papel" or jogo == "pedra X pedra":
    vence = "Empate"

if vence != "Empate":
    vencedor = "Você venceu" if suaJogada == vence else "Você perdeu"
else:
    vencedor = "Ninguem venceu"

print("{} o jogo {} ".format(vencedor, vence))
