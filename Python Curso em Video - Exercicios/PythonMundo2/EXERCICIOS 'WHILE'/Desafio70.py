print('----- SUPERMERCADO -----')
resp = 's'
soma = mais_mil = 0
menor_preco = 99999
nome_menor_preco = 's'
while True:   
    if resp == 'N':
        break  
    produto = str(input('Produto: '))
    preco = float(input('Preço: R$ '))
    resp = str (input('Quer continuar? [S/N] ')).upper()
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? Digite > S < para SIM e > N < para NÃO ')).upper()[0]
       
    if preco > 1000:
        mais_mil += 1
    if preco < menor_preco:
        nome_menor_preco = produto
        menor_preco = preco
    soma += preco 
        
print(f'Total da compra foi de R${soma}\nTemos {mais_mil} produtos custando mais do que R$1000,00\nO produto mais barato foi {nome_menor_preco}, custando R${menor_preco}')