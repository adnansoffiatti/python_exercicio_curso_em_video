'''
Crie uma TUPLA preenchida com os 20 PRIMEIROS colocados da
Tabela do CAMPEONATO BRASILEIRO DE FUTEBOL, na ordem de colocação.
Depois mostre:
a) Os 5 PRIMEIROS
b) Os ÚLTIMOS 4 colocados
c) Times em ORDEM ALFABÉTICA
d) em que POSIÇÃO está o time da CHAPECOENSE
'''

times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza',
         'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
         'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo',
         'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia',
         'Sport Recife', 'Chapecoense')
print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}° posição')
