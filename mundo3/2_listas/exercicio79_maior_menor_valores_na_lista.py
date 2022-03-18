'''
Crie um programa onde o usuário possa digitar vários VALORES
NÚMERICOS e cadastre-os em uma LISTA. Caso o número já exista
lá dentro, ele NÃO SERÁ ADICIONADO. No final, serão exibidos
todos os VALORES ÚNICOS digitados, em ORDEM CRESCENTE.
'''

numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros}')
