from datetime import date
atual = date.today().year
ano_nascimento = int (input('Ano de nascimento: '))
idade = atual - ano_nascimento
if idade < 18:
    anos = 18 - idade
    data_alis = atual + anos
    print('Idade: {}\nFaltam {} anos para você se alistar.\nVocê poderá se alistar em {}'.format(idade,anos,data_alis))
elif idade == 18:
    print('Idade: {}\nJá é hora de se alistar.'.format(idade))
elif idade > 18:
    anos = idade - 18
    data_alis = atual - anos
    print('Idade: {}\nVocê deveria ter se alistado há {} anos.\nAno de alistamento correto: {}'.format(idade,anos,data_alis))