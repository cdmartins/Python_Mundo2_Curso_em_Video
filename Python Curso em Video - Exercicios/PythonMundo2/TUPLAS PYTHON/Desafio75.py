tupla_valores = ()
tupla_pares = ()

for c in range(1,5):
    n = int(input(f'Digite o {c}º valor: '))
    #Adicionar valores a tupla
    tupla_valores += (n,)
    if n%2 == 0:
        #Adicionar os valores pares na tupla:
        tupla_pares += (n,)
            

#Tirar os parenteses da tupla:
pares_sem_parentes = '  '.join(str(elemento) for elemento in tupla_pares)

#Saídas: 1º Valores digitados. 2º Quantas vezes apareceu o valor 9. 3º Em que posição apareceu o valor 3 (mesmo se não for digitado). 4º Quais os valores pares digitados
print(f'Você digitou os valores {tupla_valores}')
print(f'O valor 9 apareceu {tupla_valores.count(9)} vezes.')
print(f'O valor 3 apareceu na {tupla_valores.index(3)+1}º posição') if 3 in tupla_valores else print(f'O valor 3 não foi digitado')
print(f'Os valores pares digitados foram: {pares_sem_parentes}')