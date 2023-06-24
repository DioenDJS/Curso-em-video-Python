

teste = list()
teste.append('Diovane')
teste.append(32)
galera = list()
galera.append(teste[:])
teste[0] = 'Luis'
teste[1] = 12
galera.append(teste[:])
teste[0] = 'Luiz'
teste[1] = 11
teste.append("M")
galera.append(teste[:])
print(galera)
