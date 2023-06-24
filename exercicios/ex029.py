"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h.mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite.
"""

km = int(input('Quanto o veiculo passou : '))
kmEssedente = 0
msg = ""

if km > 80:
    kmEssedente = km - 80
    multa = kmEssedente * 7
    msg = "O veiculo essedeu {}km/h acima do 80km/h o valor da multa é {:.2f}R$ ".format(kmEssedente, multa)
else:
    msg = "A velocidade do veiculo é de {}km/h e nao essedeu 80km/h !".format(km)

print(msg)