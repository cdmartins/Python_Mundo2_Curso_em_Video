from datetime import date

ano_nascimento = int (input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print('Idade: {}'.format(idade))
print ((idade <= 9)*'Classificação: Mirim' + (idade > 9 and idade <= 14)*'Classificação: Infantil'+(idade > 14 and idade <=19)*'Classificação: Junior'+(idade > 19 and idade <= 20)*'Classificação: Senior'+(idade > 20)*'Classificação: MASTER')
