'''
Crie um programa que leia a IDADE e o SEXO de VARIAS PESSOAS.
A cada pessoa cadastrada, o programa deverá perguntar se o
USUÁRIO quer ou não continuar. No final, mostre:
a) - Quantas pessoas tem mais de 18 ANOS.
b) - Quantos HOMENS foram cadastrados.
c) - Quantas MULHERES tem menos de 20 ANOS.
'''
tot18 = totHomens = totMulheres20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totHomens += 1
    if sexo == 'F' and idade < 20:
        totMulheres20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totHomens} homens cadastrados')
print(f'E temos {totMulheres20} mulheres com menos de 20 anos')
