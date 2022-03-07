# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele

entrada = input('Digite algo: ')
print(f'Tipo primitivo: {entrada}')

print(f'É númerico? {entrada.isnumeric()}')
print(f'É alfanúmerico? {entrada.isalpha()}')
print(f'É um decimal? {entrada.isdecimal()}')
print(f'Está em caixa baixa? {entrada.islower()}')
print(f'É apenas espaço em branco? {entrada.isspace()}')
print(f'Esta em caixa alta? {entrada.isupper()}')
