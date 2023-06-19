import random
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
resp = 0
while resp != 5:
    print('[1] - Somar\n[2] - Multiplicar\n[3] - Maior\n[4] - Novos números\n[5] - Encerrar programa')
    resp = int (input('O que deseja fazer: '))
    if resp == 1:
        soma = n1 + n2
        print('{} + {} = {}\n'.format(n1,n2,soma))
    elif resp == 2:
        mult = n1*n2
        print('{} * {} = {}\n'.format(n1,n2,mult))
    elif resp == 3:
        if n1 > n2:
            print('Entre {} e {}, o maior é {}\n'.format(n1,n2,n1))
        else: print(('Entre {} e {}, o maior é \n{}'.format(n1,n2,n2)))
    elif resp == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif resp == 5:
        print("Finalizando...")
    else:
        print('>>>> Opção inválida')
    print('=-='*10)
print('Fim do programa.')


