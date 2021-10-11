#1 Crie uma função que exibe uma saudação com os parânmetros saudação e nome
'''def saudacao(saudacao,nome):

    print(f'{saudacao},{nome}')

saudacao('oi','Lasla')
saudacao('olá','Lucas')
saudacao('Hi','João')'''

#2 - Crie uma função que recebe 3 números com parâmetros e exiba a soma entre eles.
# def soma (n1,n2,n3):
#     print(n1+ n2+n3)
# soma(2,1,3)
# soma(9,8,3)
# soma(4,5,6)

#3Crie uma função que receba 2 numeros . O primeiro é um valor e o segundo um
# percentual.Retorne o valor do primeiro número somado do aumento de percentual do mesmo

# def Sper (nu1,nceto) :
#     return nu1*nceto
# percentoal=Sper(50,0.5)
#
# if percentoal>0:
#
#     print(f"O volor percentual do número somado ao percetual dele é {percentoal+50}")
# else:
#     print('Valor invalido ')
# outra forma :
# def aumento_percentual(valor,percentual):
#     print(valor+(valor*percentual/100))
# aumento_percentual(50,15)
# aumento_percentual(30,100)
# aumento_percentual(100,20)

#Fizz Buzz- Se o parâmetro da função for divisível por 3, retorna fizz, se o parâmetro da função for fivisível por 5, retorna buzz.
# Se o parâmento da função for fivisível por 5 e por 3, retorna FizzBuzz,caso contrário,retorne o número enviado.
# def fb(n):
#     if n % 5 == 0 and n % 3 ==0:
#         return f'Fizbuzz ,{n} é divisivel por 3 e 5'
#     elif n % 3 ==0:
#        return f'fizz ,{n} é divisivel por 3'
#     elif n % 5 ==0:
#         return f'Buzz,{n} é divisével por 5'
#     else:
#         print('erro')
# aleatorio=fb(15)
# print(aleatorio)
#Segunda forma de fazer :
def fb(n):
    if n % 5 == 0 and n % 3 ==0:
        return f'Fizbuzz ,{n} é divisivel por 3 e 5'
    elif n % 3 ==0:
       return f'fizz ,{n} é divisivel por 3'
    elif n % 5 ==0:
        return f'Buzz,{n} é divisével por 5'
    else:
        print('Não é um numero valido')

from random import randint

for i in range (10):
    aleatorio=randint(0,10)
    print(fb(aleatorio))
