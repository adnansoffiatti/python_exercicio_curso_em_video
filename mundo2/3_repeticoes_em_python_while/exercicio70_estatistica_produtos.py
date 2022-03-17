'''
Crie um programa que leia o NOME e o PREÇO de
VARIOS PRODUTOS. O programa deverá perguntar se
o USUÁRIO vai continuar. No final, mostre:
a) Qual é o TOTAL GASTO na compra.
b) Quantos produtos custam MAIS de R$1000.
C) Qual é o NOME do produto mais BARATO
'''
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} custa R${menor:.2f}')
