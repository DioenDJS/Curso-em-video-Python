"""
Crie um programa que leia duas notas de um aluno e calcule sua media mostrando uma mensagem no final
de acordo com a media atingida:

- Media abaixo de 5.0: Reprovado
- Media entre 5.0 e 6.9: Recuperação
- Média 7.0 ou superior: Aprovado
"""

notaUm = float(input("Digite a primeira nota : "))
notaDois = float(input("Digite a segunda nota : "))

status = ""
media = (notaUm + notaDois) / 2

if media < 5.0:
    status = "Reprovado"
elif media >= 5.0 and media <= 6.9:
    status = "em Recuperação"
elif media >= 7.0:
    status = "Aprovado"

print("Sua media foi {:.1f} e você esta {} !".format(media, status))