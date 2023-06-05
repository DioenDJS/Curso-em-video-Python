"""
Operações Aritméticas
"""
n1 = int(input('Digite o primeiro valor : '))
n2 = int(input('Digite o segundo valor : '))

a = n1 + n2  # Adição
s = n1 - n2  # Subtração
m = n1 * n2  # Mutiplicação
d = n1 / n2  # Divisão
p = n1 ** n2  # Potência
di = n1 // n2  # Divisão Inteira
rd = n1 % n2  # Resto da Divisão

print('Soma : {}, subtração : {}, multiplicação : {}!'.format(a, s, m))
print('Divisão : {}, potência : {}, divisão inteiro : {}!'.format(d, p, di), end=' ') #OBS: o end=' ' no final evita de quebrar a linha
print('Resto da Divisão : {}!'.format(rd))

# formatando casas decimal da divisão
print('Divisão com o valor com \nduas casas decimal : {:.2}'.format(d))
