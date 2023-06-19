peso = float (input('Peso (Kg): '))
altura = float (input('Altura (m): '))
imc = peso / (altura**2)
print('IMC: {:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else: print ('Obesidade morbida')