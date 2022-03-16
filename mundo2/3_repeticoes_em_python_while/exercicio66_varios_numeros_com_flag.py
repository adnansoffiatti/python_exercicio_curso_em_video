'''
Crie um programa que leia VARIOS NUMEROS inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que
é a CODIÇÃO DE PARADA. No final, mostre QUANTO NÚMEROS foram
digitados e qual foi a SOMA entre eles (DESCONSIDERANDO O FLAG)
'''

soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}!')
