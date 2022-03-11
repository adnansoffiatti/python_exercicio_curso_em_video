'''
Refaça o DESAFIO 009, mostrando
a TABUADA de um número que o usuário
escolher, só que agora utilizando um 
LAÇO FOR.
'''
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
