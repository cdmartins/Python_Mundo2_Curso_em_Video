n = int(input("Digite um valor para saber seu fatorial: "))
fat = 1
i = 2
while i <= n:
        fat = fat*i
        i = i + 1
print('O fatorial de {}! é: {}'.format(n,fat))

#from math import factorial