'''
Crie um programa que leia um número Real qualquer pelo teclado e mostre
na tela a sua porção Inteira

Ex: Digite um número: 6.127
O número 6.127 tem a parte Interira 6
'''
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(
    num, trunc(num)))
