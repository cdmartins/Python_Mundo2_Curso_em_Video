for c in range(1,6):    
    peso = float (input('Digite o {}º peso: '.format(c)))
    if c == 1:
        maior = peso
        menor= peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O MAIOR peso é: {:.1f}kg\nO MENOR peso é: {:.1f}kg'.format(maior,menor))