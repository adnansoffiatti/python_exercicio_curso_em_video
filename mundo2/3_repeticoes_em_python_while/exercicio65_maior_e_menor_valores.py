'''
Crie um programa que leia VARIOS NUMEROS inteiros pelo teclado.
No final da execução, mostre a MÉDIA ENTRE TODOS os valores e qual
foi o MAIOR e o MENOR valores lidos. O programa dee perguntar ao
usuário se ele quer ou não CONTINUAR a digitar valores.
'''

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
