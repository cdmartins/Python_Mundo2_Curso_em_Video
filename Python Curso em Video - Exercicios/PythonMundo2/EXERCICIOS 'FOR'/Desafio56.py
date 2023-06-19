soma_idades = 0 
maior_idade_homem = 0 
mulheres_menor_idade = 0

for c in range(1,5):
    nome = str (input('Nome: '))
    idade = int (input('Idade: '))
    sexo = str (input('Sexo [F] - Feminino [M] - Masculino: '))
    soma_idades += idade
    media = soma_idades / 4
    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_do_mais_velho = nome
    if sexo == 'F' and idade < 21:
        mulheres_menor_idade += 1
print('A média de idade do grupo é de {:.1f} anos.\nO homem mais velho é {} com {} anos.\nMulheres com menos de 21 anos: {}'.format(media,nome_do_mais_velho,maior_idade_homem, mulheres_menor_idade))