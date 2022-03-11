'''
Faça um programa que calcule a SOMA
entre todos os NUMEROS IMPARES que são
MULTIPLOS DE TRES e que se encontram no
intervalo de 1 até 500
'''

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
