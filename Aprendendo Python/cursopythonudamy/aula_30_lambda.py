#Função lambda ou anômimas :

# def funcao(arg,arg2):
#     return arg *arg2
# var = funcao(2,2)
# print(var)

'''a= lambda x,y:x*y
print(a(8,5))'''

# Veja a forma de resolver usando função :
# lista = [
#     ['P1',13],
#     ['P2',6],
#     ['P3',7],
#     ['P4',50],
#     ['P5',8],
# ]
# def func (item):
#     return item[1]
# lista.sort(key=func)
# print(lista)

# Veja a forma de resolver usando lambda :
lista = [
    ['P1',13],
    ['P2',6],
    ['P3',7],
    ['P4',50],
    ['P5',8],
]
lista.sort(key=lambda item:item[1],reverse=False)
#ou também pode usar :
print(sorted(lista,key = lambda i :[1],reverse=False))

print(lista)