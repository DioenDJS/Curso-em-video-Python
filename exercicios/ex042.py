"""
Rafaça o Desafio 035 dos triangulos acrescentando o recurso de mostrar que tipo de triangulo sera formado:

- Equilátero: todos os lados iguais
- Isosceles:dois os lados iguais
- Escaleno: todos os lados diferentes
"""

ladoUm = int(input("Digite o lado 1 : "))
ladoDois = int(input("Digite o lado 2 : "))
ladoTres = int(input("Digite o lado 3 : "))

resultado = ""
if(ladoUm + ladoDois > ladoTres) and ladoDois + ladoTres > ladoUm and ladoTres + ladoUm > ladoDois:
    resultado = "Não é um triagulo"
elif ladoUm == ladoDois and ladoDois == ladoTres and ladoTres == ladoUm:
    resultado = "è um triangulo Equilátero"
elif (ladoUm == ladoDois and ladoUm != ladoTres) or (ladoDois == ladoTres and ladoDois != ladoUm) or (ladoTres == ladoUm and ladoTres != ladoDois):
    resultado = "è um triangulo Isosceles"
elif ladoUm != ladoDois and ladoDois != ladoTres and ladoTres != ladoUm:
    resultado = "è um triangulo  ladoTres"

print()