"""
Elabore um programa que calcule o valor a ser pago por um produto.
considerando o seu preço normal e condição de pagamento:

- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em ate 2x no cartão preço normal:
- Em 3x ou mais no cartão 20% de juros:

"""

valorDaCompra = float(input("Valor da compra : "))

print("="*10 + " Forma de Pagamento " + "="*10 + "\n1 - A vista dinheiro ou cheque \n2 - A vista no cartão \n3 - parcelado")

forma = int(input("escolha a forma de pagamento : "))

preçoFinal = 0
valorDasParcelas = 0
descontoOuAcrescimo = 0
quantidadeParcelas = 0
msg = ""
if forma == 1:
    descontoOuAcrescimo = valorDaCompra * 10 / 100
    preçoFinal = valorDaCompra - descontoOuAcrescimo
    msg = "pagamento feito avista dinheiro ou cheque"
elif forma == 2:
    descontoOuAcrescimo = valorDaCompra * 5 / 100
    preçoFinal = valorDaCompra - descontoOuAcrescimo
    msg = "pagamento feito a vista cartão"
elif forma == 3:
    quantidadeParcelas = int(input("Digite a quantidade de parcelas : "))
    if quantidadeParcelas <= 2:
        preçoFinal = valorDaCompra
        valorDasParcelas = preçoFinal / quantidadeParcelas
        msg = " de {} parcelas de RS{:.2f}".format(quantidadeParcelas, valorDasParcelas)
    elif quantidadeParcelas > 2:
        descontoOuAcrescimo = valorDaCompra * 20 / 100
        preçoFinal = valorDaCompra + descontoOuAcrescimo
        valorDasParcelas = preçoFinal / quantidadeParcelas
        msg = "de {} parcelas de RS{:.2f}".format(quantidadeParcelas, valorDasParcelas)

print("valor final RS{}, {} !".format(preçoFinal, msg))