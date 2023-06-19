valor_casa = float (input('Valor da casa R$'))
salario = float (input('Salário do comprador R$'))
anos = int (input('Quantos anos para pagar: '))
prestacao = valor_casa / (anos * 12)
if prestacao < salario*0.3:
    print(f'Você pagará R${prestacao:.2f} mensal por {anos} anos.\nEmprestimo APROVADO')
else: 
    print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos} anos, a prestação será de R${prestacao:.2f}.\n Emprestivo NEGADO')
