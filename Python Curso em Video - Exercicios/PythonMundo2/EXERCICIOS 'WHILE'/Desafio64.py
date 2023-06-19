
n = cont = soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        soma += n
    cont += 1
print('A soma de todos os {} números digitados é: {}'.format(cont-1,soma))
