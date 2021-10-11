"""
Split, Join, enumerate em Python
*Split - Dividir uma string #str
*Join - Juntar uma lista # Str
% count(variável) server para ver quantas vezes a variavel dentro dos pareteses aparece
* Enumerate - Enumerar elementos da lista # interáveis
* strip() Remove o espaço no inicio e no fim do string
"""
'''string = "O Brasil é o o o o o país do futebal,o Brasil é Penta"
lista1 = string.split(' ')
lista2 = string.split(',')
# print(lista1)
# print(lista2)
palavra =''
contagem = 0
for valor in lista1:
    qtd_vezes = lista1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f' A palavra que aparece mais vezes é {palavra} (`{contagem} x)')'''

'''string = 'Acesse o site jw.org e aprenda sobre Deus'
lista = string.split(' ')
string2 = '.'.join(lista)
print(string2)'''

# string = 'Acesse o site jw.org e aprenda sobre Deus'
# lista = string.split(' ')
# for indice, nome in enumerate(lista):
#     print(indice,nome)

# lista = ['João ','Lucas','Alcãntara','Moreira','dos','Santos']
# n1,n2,n3,n4,n5,n6 = lista
# print(n1,n2,n6)
#
# lista = [
#     ['João ','Lucas','Alcântara'],
#     ['Moreira','dos','Santos'],
#     ['Lasla','do','Rosario','Brito'],
# ]
# print(lista[0][2]) # índice um da lista mãe índice 2 da lista filho
# enumerada = enumerate(lista)
# print(list(enumerada))

lista = [
    ['João ','Lucas','Alcântara'],
    ['Moreira','dos','Santos'],
    ['Lasla','do','Rosario','Brito'],
]
for v1 ,v2 in enumerate(lista,50) :
    print(v1, v2)