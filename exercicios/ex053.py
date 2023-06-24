"""
Crie um programa que leia uma frase qualquer e diga se ela é
um palindromo desconsiderando os espaços

EX: APOS A SOPA
"""

# frase = str(input("Digite a frase : ")).strip()
frase = "APOS A SOPA "

separando = frase.split()
fraseJunta = "".join(separando)

fraseinvertida = fraseJunta[::-1]

msg = "é um palindromo" if fraseinvertida == fraseJunta else "não palindromo"

print(f"A frase {frase} {msg}")