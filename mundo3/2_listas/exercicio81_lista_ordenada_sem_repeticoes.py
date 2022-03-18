'''
Crie um programa que vai ler VÁRIOS NÚMEROS e colocar em uma
LISTA. Depois disso, mostra:
a) QUANTOS números foram digitados.
b) A lista de valores, ordenada de forma DECRESCENTE
c) Se o valor 5 foi digitado e está ou não na LISTA
'''

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
