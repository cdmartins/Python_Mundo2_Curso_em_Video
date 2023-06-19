numero = int (input('Digite um número inteiro: '))
BaseConver = str(input('Escolha a base para conversão:\n[ 1 ] para BINÁRIO\n[ 2 ] para OCTAL\n[ 3 ] para HEXADECIMAL\nSua opção: '))
if BaseConver == '1':
    BaseConver = 'BINÁRIO'
    convertido = bin(numero)[2:] 
    print('O número {} convertido para {} é igual a:  {}'.format(numero,BaseConver,convertido))
elif BaseConver == '2':
    BaseConver = 'OCTAL'
    convertido = oct(numero)[2:] 
    print('O número {} convertido para {} é igual a:  {}'.format(numero,BaseConver,convertido))
elif BaseConver ==  '3':
    BaseConver = 'HEXADECIMAL'
    convertido = hex(numero)[2:] 
    print('O número {} convertido para {} é igual a:  {}'.format(numero,BaseConver,convertido))
else: print('Opção INVALIDA')
