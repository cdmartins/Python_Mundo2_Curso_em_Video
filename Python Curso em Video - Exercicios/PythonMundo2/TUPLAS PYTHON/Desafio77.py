palavras = ('Banana', 'Carro', 'Abacaxi', 'Casa', 'Flor', 'Gato', 'Elefante', 'Laranja', 'Mesa', 'Livro')

for palavra in palavras:
    vogais = ''
    for letra in palavra:
        if letra.lower() in 'aeiou':
            vogais += (letra)
    print(f'Na palavra {palavra.upper()} temos: {vogais.lower()}')


