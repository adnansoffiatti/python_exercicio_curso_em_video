'''
Crie um programa onde o usuário possa digitar cinco VALORES
NUMÉRICOS e cadastre-os em uma LISTA, JÁ NA POSIÇÃO CORRETA
de inserção (sem usar o SORT()). No final, mostre a LISTA
ORDENADA na tela.
'''

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
