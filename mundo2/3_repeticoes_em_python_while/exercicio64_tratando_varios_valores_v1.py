'''
Crie um programa que leia VARIOS NUMEROS inteiros pelo
teclado. O programa só vai parar qunado o usuário digitar
o valor 999, que é a CONDIÇÃO DE PARADA . No final, mostre
QUANTOS NÚMEROS foram digitados e qual foi a SOMA entre eles
(DESCONSIDERANDO O FLAG)
'''

num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {} '.format(cont, soma))
