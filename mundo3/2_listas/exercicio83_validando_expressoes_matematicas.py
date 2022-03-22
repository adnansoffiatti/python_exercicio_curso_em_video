'''
Crie um programa onde o usuário digite uma EXPRESSÃO
qualquer que use PARÊNTESES. Seu aplicativo deverá analisar
se a expressão passada está com os parênteses aberto e
fechados na ORDEM CORRETA
'''

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está inválida')