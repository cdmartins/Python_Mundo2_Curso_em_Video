import random 
cont = 0
jogador_vence = True
print('Vamos jogar par ou Impar?'.upper())
jogador_num = int (input('Digite um número: '))

while True:      
    computador = random.randint(0,10)
    jogador_escolha = str(input('Par ou Ímpar? [P/I]: ')).upper()
    soma = jogador_num + computador
    par_ou_impar = 'Par' if soma %2 == 0 else 'Impar'
    print(f'Você escolheu {jogador_num} e o computador {computador}. Deu {soma}, {par_ou_impar}!')
    if (soma %2 == 0 and jogador_escolha in 'Pp') or (soma %2 != 0 and jogador_escolha in 'Ii'):
            print(f'Você VENCEU!\nVamos jogar novamente...')
            cont += 1                
            jogador_num = int (input('Digite um valor '))
    else: 
        print('VOCE PERDEU')
        break
   

print(f'GAME OVER! Você venceu {cont} vezes.')