print('='*30)
print('     10 TERMOS DE UMA PA')
print('='*30)
a1 = int (input('\nPrimeiro termo: '))
r = int (input ('Razão: '))
pa = a1
print('Os 10 primeiros termos de uma PA de inicio {} com razão {} são:'.format(a1,r))
for c in range(0,10):
    print(pa,end=' ')
    pa += r

