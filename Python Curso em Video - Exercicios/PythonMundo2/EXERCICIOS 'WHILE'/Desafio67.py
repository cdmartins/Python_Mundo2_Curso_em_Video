n = 0

while True:
    n = int (input('Quer ver a taboada de qual valor? \n(valor negativo para parar) '))
    cont = 0
    if n < 0:
        break
    while cont < 10:
        cont += 1
        print(f'{n} x {cont} = ', n*cont)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre.')
    