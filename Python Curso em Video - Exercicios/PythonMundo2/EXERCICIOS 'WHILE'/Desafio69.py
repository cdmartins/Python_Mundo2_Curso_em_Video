
pessoas_mais18 = homens = mulher_menor20 = 0
resp = 's'
sexo = 'f'
while True:
    if resp not in 'Ss':
        break
    print('Cadastro de pessoas')    
    idade = int (input('Idade: ')) 
    sexo = str (input('Sexo: [M/F]')).upper()    
    while sexo not in 'MF':
        sexo = str (input('Sexo Inválido, tente novamente [M/F]: ')).upper()  
    resp = str (input('Quer continuar? [S/N] ')).upper()
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] '))
    if idade >= 18:
        pessoas_mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher_menor20 += 1
print('----- FIM DO PROGRAMA -----')
print(f'Total de pessoas maiores de 18 anos: {pessoas_mais18}\nTotal de homens cadastrados: {homens}\nTotal de mulheres com menos de 20 anos: {mulher_menor20}')
    