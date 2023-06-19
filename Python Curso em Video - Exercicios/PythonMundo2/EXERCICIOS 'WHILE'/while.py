import random 

# while Apple false:
#     if chão == True: passo
#     if buraco == True: Pule
#     if moeda == True: pega
# pegaMaça

# for c in range(1,3):
#     n = random.randint(1,50)
#     print('Digite um valor: ')
#     print(n)
# print('fim')

# n = 1
# pares = impar = 0
# while n != 0:
#     n = int(input ('Digite um valor: '))
#     if n != 0:
#         if n %2 == 0:
#             pares += 1
#         else: impar += 1
# print('Acabou', pares, impar)


# import random
# computador_num = random.randint(1,10)
# jogador_num = int(input('Vou pensar em um número... Tente adivinhar\n(~~~~Dica: entre 1 a 10~~~~)\nE ai? Qual seu palpite?  '))
# cont = 1

# while jogador_num != computador_num:
#     jogador_num = int(input('Eu pensei no número {}, você chutou {} e ERROUU!!!\nVamos lá tente novamente: '.format(computador_num,jogador_num)))
#     computador_num = random.randint(1,10)
#     cont += 1

    

# print('Eu pensei no número {}, e voce chutou {}!!! Parabéns você acertou!!!\nTentativas: {}'.format(computador_num,jogador_num,cont))
#comando BREAK, parar o while infinito
saque = int(input('Informe o valor do saque: '))
notas_50 = saque // 50 
notas_20 = saque %50 // 20   
notas_10 = saque %20 // 10
notas_1 = saque %10 // 1   
print(notas_50, notas_20, notas_10, notas_1)