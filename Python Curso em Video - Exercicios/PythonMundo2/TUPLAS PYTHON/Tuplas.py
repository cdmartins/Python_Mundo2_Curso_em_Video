lanche = ('Hamburguer', 'Suco','Pizza', 'Pudim', 'Batata Frita ')
#TUPLAS SÃO IMUTAVEIS

#maneira1:
for c in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[c]}')
print('Comi pra caramba! ')

#maneira2:
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')

#Maneira3:
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba! ')

#Imprimir em ordem alfabetica, método SORTED
print(sorted(lanche))

a = (2,5,4)
b = (5,8,1,2)
c = a + b #União dos conjuntos A e B

#Para contar quantas vezes aparece tal elemento no conjunto, metodo > (onde voce quer procurar) <-- x.COUNT() <
print(c.count(5))

#Para saber qual posição está tal elemento, metodo .index
print(c.index(8))


n = int (input('Digite um numero inteiro de 0 a 20: '))

