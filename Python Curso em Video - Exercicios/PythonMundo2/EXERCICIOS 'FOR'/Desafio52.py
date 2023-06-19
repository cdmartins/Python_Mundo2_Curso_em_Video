n = int (input('Digite um numero inteiro: '))
mult = 0 
for c in range(2, n-1):
    if n % c == 0:
        mult += 1
if mult == 0 and n >= 2:
    print('É um numero primo')
else: print('Não é um numero primo')