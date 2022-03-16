'''
Melhore o DESAFIO 061, perguntando para o usuário
se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer
mostrar O TERMOS.
'''
# usou código do 61

print('Gerador de PA')
print('-=-' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
