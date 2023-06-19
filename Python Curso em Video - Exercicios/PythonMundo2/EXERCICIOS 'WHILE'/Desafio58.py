import random
import time 
computador_num = random.randint(1,10)
print('Vou pensar em um número de 1 a 10...')
time.sleep(0.5)
print('Tente adivinhar')
time.sleep(0.5)
jogador_num = int(input('\nE ai? Qual seu palpite?  '))
cont = 1
while jogador_num != computador_num:
    if jogador_num < computador_num:
        print('\nMais...')
    else: print('\nMenos...')
    time.sleep(0.5)
    jogador_num = int(input('\nVamos lá, mais uma chance:  '))
    cont += 1
print('Eu pensei no número {}. Parabéns você acertou!!!\nEm {} tentativas.'.format(computador_num,cont))

