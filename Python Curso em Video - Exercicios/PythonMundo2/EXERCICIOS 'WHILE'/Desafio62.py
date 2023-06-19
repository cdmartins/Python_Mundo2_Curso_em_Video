print('Digite o primeiro termo e a razão para obter os 10 primeiros termos de uma PA')
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
pa = primeiro_termo
c = 1
total = 0
mais = 11
while mais != 0:
    total += mais
    while c < total: 
        print(pa,end=' ')  
        pa += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
