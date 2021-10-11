'''
Funções (def) em Python- return-aula 27( parte 2 )
'''

def divisao(n1,n2):
    if n2==0:
        return
    return n1 / n2
divide = divisao (8,-1)

if divide:
    print(divide)
else:
    print('conta invalida')