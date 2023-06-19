
resp = 'S'
soma = 0
c = 0
while resp == 'S':
    n = int(input('Digite um número: '))
    soma += n
    c+= 1
    media = soma / c
    if c == 1:
        maior = menor = n        
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N]')).upper()
print('Soma dos números digitados: {}\nMédia: {:.1f}\nMaior número: {}\nMenor número: {}'.format(soma, media,maior,menor))