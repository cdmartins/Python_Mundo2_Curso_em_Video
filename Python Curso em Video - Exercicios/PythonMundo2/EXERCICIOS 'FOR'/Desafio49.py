n = int (input('Digite um numero: '))
print('A TABOADA DE {} É: '.format(n))
for c in range(1,11):
    print('{} x {} = {}'.format(n,c,n*c))
