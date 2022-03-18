'''
Crie um programa que tenha uma TUPLA com VARIAS PALAVRAS
(não usar acentos). Depois disso, você deve mostrar, para
cada palavra, quais são suas VOGAIS.
'''

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos = ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
