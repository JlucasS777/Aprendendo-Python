# print()
# exten = ('zero','um','dois', 'tres' ,'quatro', 'cinco', 'seis', 'sete', 'oito' ,'nove' ,'dez','onze' ,'doze' ,'treze' ,'quartoze', 'quinze' ,'dezesseis' ,'dezessete' ,'dezoito' ,'dezenove' ,'vinte')
#
# print()
#
# while True:
#     num = int(input('Digite um numero entre (0 e 20) :'))
#
#     if num >= 0 and num <= 20:
#
#         print(f'O número que você digitou escrito por extenso é igual a : {exten[num]}')
#         break
#     else :
#
#         print('Digite um valor valido!!\n')

# Exercicio 02:
# from random import randint
# n = (randint (1,100),randint (1,100),randint (1,100),randint (1,100),randint (1,100))
# print('Os valores sorteados foram ',end ='')
# for numeros in n :
#     print(f'{numeros}',end='-')
# print(f'\nO maior numero foi {max(n)}')
# print(f'O menor numero foi {min(n)}')
n1=(int(input("Digite o primeiro número :")),
int(input("Digite o segundo número :")),
int(input("Digite o terceiro número :")),
int(input("Digite o quarto número :")))

print(f'\nOs números digitados foram {n1}')
print(f'\nO número 9 aparece {n1.count(9)} vezes\n')
if 3 not in n1:
    print(" O valor 3 não foi encontrado em nenhuma posição")
else:
    print(f'\nO valor 3 aparece na posição  {n1.index(3)+1} ')
c=0

for passada in n1 :
      if passada % 2 == 0:
        c+=1
print(f'\nTemos um total de {c} números pares ')

