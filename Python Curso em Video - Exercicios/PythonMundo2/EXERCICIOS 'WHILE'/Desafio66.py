n = cont = soma = 0
while True:
    n = int (input('Digite um valor (999 Para finalizar): '))
    if n == 999:
        break
    cont += 1
    soma += n    
print(f'A soma dos {cont} valores foi {soma}!')
