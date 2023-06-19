s = 0
cont = 0
for c in range(1,501):
    if c %2 != 0 and c %3 == 0:
        s += c
        cont += 1
print('\nA soma dos número impares e multiplos de 3 no intervalo de 1 a 500 é igual a {}, com {} valores'. format(s,cont))
