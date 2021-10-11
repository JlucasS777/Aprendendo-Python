"""Listas em python
fatiamento
append(adiciona um elemento no final da lista), insert(insere algo no índice escolhido) , pop(remove o último elemento da lista),
 del (apaga elemento podendo utilizar intervalos) ,clear, extend, +
 min, max (min e max mostram o maior e menor valor da sua lista)
range"""
#         0  1    2   3   4    5 - ESSES SÃO OS ÍNDECES DA LISTA ABAIXO
# lista = ['A','B','C','D','E',10.5]
# lista[5] = " fiz a mudança do índice 5 para uma string"
#
# print(lista[5])
# #Fatiamento de lista
# print (lista[1:6:2])
l1 = [1,2,3]
l2 = [4,5,6]
l3= l1+l2
l2.append("b")
print(l1)
print(l2)
print(l3)

"""
Criando lista com a função range
"""
# l2 = list(range(0,11))
# print (l2)
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for valor in lista :
    print(valor)
"""" jogo da forca """
#!/usr/bin/env python

"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra) #Adiciona a letra digitada na lista

    if letra in secreto:
        print(f'UHUULLL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFFzzz: a letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop() # Apaga a letra errada digitada da lista

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()
