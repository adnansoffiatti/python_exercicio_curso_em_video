'''
Refaça o DESAFIO 51, lendo o PRIMEIRO
TERMO e a RAZÃO de uma PA, mostrando
os 10 PRIMEIROS TERMOS da progressão
usando a estrutura WHILE
'''
print('Gerador de PA')
print('-=-' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + razao
    cont += 1
print('FIM')
