times = ("Flamengo", "Palmeiras", "Atlético-MG", "Fortaleza", "Athletico Paranaense",
    "Bahia", "Fluminense", "Santos", "Corinthians", "Ceará", "Internacional",
    "São Paulo", "Juventude", "Sport Recife", "América-MG", "Atlético-GO", "Grêmio",
    "Chapecoense", "Cuiabá", "América-RN")

print(12*'-=-')
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print(12*'-=-')
print(f'Os últimos 4 colocados da tabela são: {times[-4:]}')
print(12*'-=-')
print(f'Em ordem alfabética temos: {sorted(times)}')
print(12*'-=-')
print(f'E o time da Chapecoente está na {times.index("Chapecoense")+1}º na tabela')