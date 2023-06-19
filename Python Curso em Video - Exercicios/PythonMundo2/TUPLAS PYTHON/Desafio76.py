
#Entrada: Um tupla com string de produtos seguido de seus respectivos valores
produtos = ( "Maçã", 1.5,"Banana", 0.75,"Laranja", 1.0,"Abacaxi", 2.25, "Melancia", 4.5,"Morango", 2.0,"Uva", 3.75,"Pera", 1.25,"Kiwi", 2.75, "Manga", 2.5)

#Saida: Tabela de preço dos produtos alinhados um em frente ao outro
print('-------> LISTAGEM DE PREÇOS <-------')
for i in range(0, len(produtos), 2):
    produto = produtos[i]
    preco = produtos[i +1]
    print(f'{produto:.<30}R${preco:.2f}')
                    #:<30 Pra alinhar com 30 espaços a direita




