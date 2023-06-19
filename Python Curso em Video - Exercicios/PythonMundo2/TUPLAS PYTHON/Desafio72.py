#Entrada: Tupla com numeros escritos por extenso do 0 ao 20
escritos = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez",
            "Onze", "Doze", "Treze", "Catorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")


#Saida: Mostrar por extenso o numero digitado pelo usuario. Repetir o processo quantas vezes ele desejar. Só aceitar numeros entre 0 e 20
while True:
    n = int (input('Digite um numero inteiro de 0 a 20: '))
    if n < 0 or n <= 20:
        print(f'Você digitou o numero {escritos[n]}.')       
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if 'S' not in resp:
            break
