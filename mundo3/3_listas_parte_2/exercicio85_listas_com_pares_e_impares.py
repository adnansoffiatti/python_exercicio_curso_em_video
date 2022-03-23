'''
Crie um programa onde o usuário possa digitar SETE
VALORES NUMÉRICOS e cadastre-os em uma LISTA ÚNICA
que mantenha separados os valores PARES e IMPARES.
No final, mostre os valores pares e impares em
ordem CRESCENTE.
'''

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}°. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')
