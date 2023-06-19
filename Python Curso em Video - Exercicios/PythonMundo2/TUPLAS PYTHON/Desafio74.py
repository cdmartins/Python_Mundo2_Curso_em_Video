from random import randint
lista = ()
for c in range(5):
    n = randint(1,67)
    lista += (n,)
lista_sem_parenteses = ', '.join(str(elemento) for elemento in lista)
print(f'Os valores sorteados foram: {lista_sem_parenteses}')
print(f'O maior valor dessa lista é {max(lista)}\nO menor valor é {min(lista)}')

