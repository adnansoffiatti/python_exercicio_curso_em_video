# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
# quantos dólares ela pode comprar

# Condisere R$ 5,06 = 1,00 dólar
real = float(input('Quanto dinheiro você tem na carteira? '))
dolar = 5.06
conversao = real / dolar
print('Com R${} você pode comprar US$ {:.2f}.'.format(real, conversao))
