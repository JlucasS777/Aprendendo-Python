#1- Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
'''def funcao1():
    return 'Olá Mundo!'

def funcao2(funcao):
    return funcao()
executando = funcao2(funcao1)
print(executando)'''

# Exercício 2

def mestre(funcao,*args,**kwargs) :
    return funcao(*args,**kwargs)

def fala_oi (nome):
    return f'Oi {nome}'

def saudacao (nome, saudacao):
    return f'{saudacao} {nome}'
executando = mestre(fala_oi,'Lucas')
executando2 = mestre(saudacao,'Lucas',saudacao = 'Bom dia!')
print(executando)
print(executando2)