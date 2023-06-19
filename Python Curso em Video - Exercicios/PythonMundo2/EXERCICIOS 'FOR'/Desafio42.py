
l1 = float (input('Primeiro lado: '))
l2 = float (input('Segundo lado: '))
l3 = float (input('Terceiro lado: '))

if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1 +l2):
    print('É um triangulo ', end='')
    if l1 == l2 == l3:
        print('equilatero')    
    elif l1 != l2 != l3 != l1:
        print('escaleno')
    else: print('isósceles')
else:
    print('Não é um triangulo')