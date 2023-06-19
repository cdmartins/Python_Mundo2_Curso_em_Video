n = int(input('Quantos elementos da Sequencia de Fibonacci você quer visualizar: '))
c = 1
f1 =0
f2 = 1
while c <= n:   
    sequencia = f1 + f2
    print(sequencia, end=' ')
    f2 = f1
    f1 = sequencia
    c += 1
    
