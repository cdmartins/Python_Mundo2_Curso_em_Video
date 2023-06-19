sexo = str(input('Digite seu sexo [F/M]: ')).upper()

#aqui poderia usar tbm o Not in, ficaria assim: while sexo not in 'FfmM'
while sexo != 'F' and sexo != 'M':
    sexo = str (input('Dados invalidos, tente novamente.\nDigite seu sexo [F/M]:  ')).upper()

genero = '> FEMININO <' if sexo == 'F' else '> MASCULINO <'
print('\nSexo {} Cadastrado\nPROGRAMA ENCERRADO'.format(genero))

