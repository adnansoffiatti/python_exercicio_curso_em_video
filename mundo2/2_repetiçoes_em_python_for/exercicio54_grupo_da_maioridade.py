'''
Crie um programa que leia o ANO DE NASCIMENTO
de SETE PESSOAS. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já
são maiores.
'''

from datetime import date

atual = date.today().year
total_menor = 0
total_maior = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        total_maior += 1
    else:
        total_menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(total_maior))
print('E também tivemos {} pessoas menores de idade'.format(total_menor))
