'''
Escreva um programa que leia um valor em metros,
e o exiba convertido em centímetros e milímetros
'''

n = int(input('Digite um valor em metros: '))

print(f'{n} metros são {n * 1000} quilômetros.')
print(f'{n} metros são {n * 100} hectômetros.')
print(f'{n} metros são {n * 10} decâmetros.')
print()

print(f'{n} metros são {n * 1} metros.')
print(f'{n} metros são {n / 10} decímetros.')
print(f'{n} metros são {n / 100} centímetros.')
print(f'{n} metros são {n / 1000} milímetros.')
