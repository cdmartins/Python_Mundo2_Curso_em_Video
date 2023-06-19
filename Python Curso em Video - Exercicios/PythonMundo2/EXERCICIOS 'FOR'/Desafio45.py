from random import randint
from time import sleep

opcao_jogador = int(input("Sua opção: \n[0] Pedra\n[1] Papel\n[2] Tesoura\n"))
print('')
print("JO")
sleep(1)
print("KEN")
sleep(0.5)
print("PO!!")
sleep(1)
print('')
itens = ("Pedra", "Papel", "Tesoura")
opcao_computador = randint(0, 2)
if opcao_jogador <= 2:
    print("-=" * 15)
    print(
        "Computador escolheu: {}\nVocê escolheu: {}".format(
            itens[opcao_computador], itens[opcao_jogador]
        )
    )
    if opcao_jogador == opcao_computador:
        print("====> Empate")
    elif (
        (opcao_jogador == 0 and opcao_computador == 1)
        or (opcao_jogador == 1 and opcao_computador == 2)
        or (opcao_jogador == 2 and opcao_computador == 0)
    ):
        print("====> Computador venceu")
    else:
        print("====> VOCÊ VENCEU!!!")
else:
    print("Opção invalida, tente novamente")
