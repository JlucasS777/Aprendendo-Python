#Adicionando valores a uma lista :
# valores = []
# for cont in range(0,5):
#     valores.append(int(input('Digite um numero para cria sua lista :')))
# print(valores)
# for c, v in enumerate(valores):
#     print(f'Na posição [{c}] tem o valor  {v}...',end='')

#######################----EXERCÍCIOS----##################################
# lista = []
# posicao_maior = []
# posicao_menor = []
# for p in range(0, 5):
#     lista.append(int(input(f'Digite um valor na posição {p}: ')))
#
# for p, v in enumerate(lista):
#     if v == max(lista):
#         posicao_maior.append(p)
#     if v == min(lista):
#         posicao_menor.append(p)
# print(f'Você digitou os valores {lista}')
# print(f'O maior valor da lista é {max(lista)}, nas posições {posicao_maior}')
# print(f'O menor valor da lista é {min(lista)}, nas posições {posicao_menor}')
while True:
    expr = str(input('Digite uma  expressão válida: '))
    pi = expr.count('(')
    pf = expr.count(')')
    if expr.index(')') > expr.index('('):
        if pi == pf:
            print('Expressão válida')
        else:
            print('Expressão é inválida')
            break
    else:
        print('Expressão inválida')