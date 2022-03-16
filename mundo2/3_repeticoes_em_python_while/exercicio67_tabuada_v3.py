'''
Faça um programa que mostre a TABUADA de VARIOS NUMEROS,
um de cada vez, para cada valor digitado pelo usuario.
O programa será INTERROMPIDO quando o número solicitado
for NEGATIVO
'''

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
