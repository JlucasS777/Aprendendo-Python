# temp = []
# princ = []
# maior = menor = 0
# while True:
#     temp.append(str(input('Nome:')))
#     temp.append(float(input('Peso:')))
#     if len(princ) == 0:
#         maior = menor = temp[1]
#     else:
#         if temp[1]>maior:
#             mai= temp[1]
#         if temp[1]<menor:
#             menor=temp[1]
#     princ.append(temp[:])
#     temp.clear()
#     resp = str(input('Quer continuar?[s/n]'))
#     if resp in 'Nn':
#         break
# print(30*'+=')
# print(f'Ao todo você cadastrou {len(princ)} pessoas ')
# print(f' O maior peso foi de {maior} kg. Peso de ',end='')
# for p in princ:
#     if p[1]== maior:
#         print(f'{p[0]}',end='')
# print()
# print(f' O menor peso foi de {menor} ',end='')
# for p in princ:
#     if p[1]== menor:
#         print(f'{p[0]}')
#
# print()
'''
Exercício 85

'''
# listag =[]
# par=[]
# impar=[]
# for  c in range(1,8):
#     listag.append(int(input(f"Digite um número pela  {c}ªº: ")))
# for  v in listag:
#     if v % 2== 0:
#         par.append(v)
#     else:
#         impar.append(v)
# listag.clear()
# listag.append(par)
# listag.append(impar)
#
# par.sort()
# print(f'Os pares são {par}')
# impar.sort()
# print(f'Os impares são {impar}')
# listag.sort()
# print(listag)
### Resolução Guanabara
# num = [ [], [] ]
# valor = 0
# for c in range (1,8):
#     valor= int(input(f'Digite o {c}º. valor: '))
#     if valor %2 == 0:
#         num[0].append(valor)
#     else:
#         num[1].append(valor)
# num[0].sort()
# num[1].sort()
# print(f'Os valores pares digitados foram:{num[0]}')
# print(f'Os valores pares digitados foram:{num[1]}')
# print(f'A lista total foi {num}')
################
# matriz = [[0,0,0],[0,0,0],[0,0,0]]
# spar = mai = scol = 0
# for l in range (0,3):
#     for c in range(0,3):
#         matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
# print('-='*30)
# for l in range(0,3):
#     for c in range(0,3):
#         print(f'[{matriz[l][c]:^3}]',end='')
#         if matriz[l][c] % 2 ==0:
#             spar+=matriz[l][c]
#     print()
# print('-='*30)
# print(f'A soma dos valores pares é {spar}')
# for l in range(0,3):
#     scol+=matriz[l][2]
# print(f'A soma dos valores da terceira coluna é  {scol}')
# for c in range(0,3):
#     if c == 0:
#         mai = matriz[1][c]
#     elif matriz [1][c]> mai:
#         mai = matriz [1][c]
# print(f'O maior valor da segunda linha é {mai} .')
###
# from random import randint
# from time import sleep
# lista = list()
# cont = 0
# jogos = list()
# quant = int(input("Quantas listas você quer sortear :"))
# tot = 1
# while tot<=quant:
#     cont=0
#     while True:
#         num = randint(1,60)
#         if num not in lista:
#             lista.append(num)
#             cont+=1
#         if cont >=6:
#             break
#     lista.sort()
#     jogos.append(lista[:])
#     lista.clear()
#     tot+=1
# print(f'Os números sorteados foram :')
# print()
# for i,l in enumerate(jogos):
#     print(f'jogo{i+1}:{l}')
#     sleep(1)
#forma BRUTAL :
# from random import sample
# from time import sleep
# jogos=list()
# n=int(input('Quantos jogos?: '))
# for c in range(n):
#   a=sorted(sample(range(1, 61), 6))
#   jogos.append(a[:])
#   print(f'Jogo {c+1}: {a}')
#   sleep(0.5)
