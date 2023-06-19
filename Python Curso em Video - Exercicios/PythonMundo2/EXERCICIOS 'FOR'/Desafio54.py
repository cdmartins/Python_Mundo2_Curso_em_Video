from datetime import date
maior_idade = 0
menor_idade = 0
ano_atual = date.today().year

for c in range(1,8):
    ano_nasc = int (input('{}º Ano de nascimento: '.format(c)))
    idade = ano_atual - ano_nasc
    if idade < 21:
        menor_idade += 1
    elif idade >= 21:
        maior_idade += 1
print('Maior idade: Acima de 21 anos.\n{} pessoas já atingiram a maior idade.\n{} pessoas ainda não atingiram a maior idade.'.format(maior_idade,menor_idade))