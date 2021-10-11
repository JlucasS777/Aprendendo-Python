#funções (def) em Python - *args(Uso quando eu não sei quantos argumentos serão necessários na minha função )*** Kwargs-
#Aula 16(Parte3)
'''def func (a1,a2,a3,a4,a5,nome = None,a6 = None):
    print(a1,a2,a3,a4,a5,nome, a6)
    return nome, a6
var=func (1,2,3,4,5,nome = 'Luiz',a6='5')
print(var[1],var[0])'''

def func(*args):
    print(arg)
lista = [1,2,3,4,5]
n1,n2,*n = lista # ao usar o *n estou solicitando todos os elementos da lista 
print(n1,n2,n)