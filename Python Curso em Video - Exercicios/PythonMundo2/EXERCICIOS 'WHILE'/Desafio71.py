
print('----- BANCO DO KRL -----')
notas_50 = notas_20 = notas_10 = notas_1 = saque =  0
while True:    
    saque = int(input('Informe o valor do saque: '))
    notas_50 = saque // 50 
    notas_20 = saque %50 // 20       
    notas_10 = saque %20 // 10
    notas_1 = saque %10 // 1   
    break
print(f'Notas de 50: {notas_50}\nNotas de 20: {notas_20}\nNotas de 10: {notas_10}\nNotas de 1: {notas_1}')

#código nao esta rodando pra valores acima de 700