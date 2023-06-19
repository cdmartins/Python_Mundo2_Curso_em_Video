preco_produto = float (input('Preço do produto  '))
forma_pagamento = str (input('Forma de pagamento\n[1] Dinheiro/Cheque AVISTA\n[2] Cartão 1x\n[3] Cartão 2x\n[4] Cartão 3x+\n'))
juros = 0
desconto = 0
if forma_pagamento == '1':
    desconto = preco_produto * 0.1
    novo_preco = preco_produto - desconto
elif forma_pagamento == '2':
    desconto = preco_produto * 0.05
    novo_preco = preco_produto - desconto
elif forma_pagamento == '3':
    novo_preco = preco_produto
elif forma_pagamento == '4':
    parcelas  = int (input('Quantas parcelas? '))
    juros = preco_produto * 0.2
    novo_preco = preco_produto + juros
    valor_parcelas = novo_preco / parcelas
    print('{} Parcelas de {:.2f}'.format(parcelas,valor_parcelas))

print('Valor do produto: R${}\nPreço à pagar: R${}\nDesconto de {:.2f}\nJuros de {:.2f}'.format(preco_produto,novo_preco,desconto, juros))
