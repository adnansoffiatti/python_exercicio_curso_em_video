'''
Crie um programa que vai ler VÁRIOS NÚMEROS e colocar em uma
LISTA. Depois disso, crie DUAS LISTAS EXTRAS que vão conter
apenas os valores PARES e os valores IMPARES digitado,
respectivamente. Ao final, mostre o conteúdo das TRÊS LISTAS
geradas.
'''

num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
