# def myname ():
#     print('João Lucas Alcântara Moreira dos Santos ')
# myname()
# def myname (nome='João Lucas',sobrenome = 'Alcântara Moreira dos Santos'):
#     print(nome,sobrenome)
# myname()
# myname('Lasla','Alcântara')


#Aula com guanabara.


# def lin():# chamamos de programa principal
#     print('=#'*30)
#
# lin()
# print(" Lucas ")
# lin()

# def título (txt):
#     print('-'*30)
#     print(txt)
#     print('-' * 30)
#
# título('Obrigado Guanabara')
# def soma(a,b):
#     print(f'A={a} e B={b}')
#     s= a+b
#     print(f'A soma de A+B é {s}')
#
# soma(18,15)
# def soma(*valores):
#     soma= 0
#     for num in valores:
#         soma+=num
#     print(f'Somando os valores {valores} adicionados o resultado é {soma} ')
# soma(16,80,68,70)

#Exercicio 96
# def área(a,b):
#     área= a*b
#     print(f'A área do seu  terreno é {a}m X {b}m é de {área} m²')
#
# print("Controle de Terrenos")
# print("-"*30)
# a=float(input('Largura do terreno (m):'))
# b=float(input('Largura do terreno (m) :'))
# área(a,b)
# área(560,874)

#Exercício 97
# def escreva(txt):
#     tam = len(txt)
#     print('~'* len(txt))
#     print(txt)
#     print('~' * len(txt))
#
#
# while True:
#     txt=str(input('Digite algo ao seu gosto:'))
#     escreva(txt)
#     cont=str(input("Quer continuar [S/N]:"))
#     if cont in "nN":
#         break
# print('=-'*30)
# print('Obrigado por participar do programa ')

# Exercício 98:
# from time import sleep
# def contador(i,f,p):
#     print(f"Contagem de {i} até {f} de {p} em {p} :")
#
#     if i < f:
#         cont = i
#         while cont <= f:
#             print(f'{cont}',end=' ')
#             sleep(0.5)
#             cont += p
#         print('FIM!')
#     elif i<f:
#         cont=i
#         while cont < f:
#             print(f'{cont}', end=' ')
#         sleep(0.5)
#         cont+=p
#
#     else:
#         cont = i
#         while cont>=0:
#             print(f'{cont}',end=' ')
#             sleep(0.5)
#             cont+=p
#         print('FIM!')
# contador(1,10,1)
# print()
# contador(10,0,-2)
# sleep(0.5)
# print("Agora é sua vez de personalizar a contagem:")
# sleep(0.5)
# i=int(input('Digite o inicio :'))
# f=int(input('Digite o fim :'))
# p=int(input('Digite o passo :'))
# while True:
#     if i > f:
#         print('=-'*30)
#         sleep(0.5)
#         print('Tente novamente o inicio não pode ser maior que o fim !!! ')
#         sleep(1.5)
#         print('=-' * 30)
#         i = int(input('Digite o inicio :'))
#         f = int(input('Digite o fim :'))
#         p = int(input('Digite o passo :'))
#     else:
#         break
# if p<0:
#     p+=1
#     print("A contangem só será reduzida até zero{0}")
# if p == 0:
#     p+=1
#     print('O passo foi para 1 (não pode ser zero)')
# sleep(0.5)
# print('=-' * 30)
# contador(i,f,p)
# def contador (i,f,p):
#     '''
#     O programa faz uma contagem e mostra na tela.
#     :param i: Inicio
#     :param f: fim
#     :param p: Passo
#     :return:Sem retorno
#     '''
#     c= i
#     while c <= f:
#         print(f" {c}",end='')
#         c+=p
#     print(" fim!")
# contador(2,10,2)
# help(contador)
# def somar (a=0,b=0,c=0):# quando se define o valor podemos deixar sem um ou outro valor
#     s=a+b+c
#     print(f"A soma vale {s}")
#
# somar(8,15,35)
# somar(8)
# def funcao ():
#     n1 = 4
#     print(f'N1 dentro  vale {n1}')
#
# n1= 2
# funcao()
# print(f'N1 fora vale {n1}')
# def teste(b):
#     global a #dessa forma a substitui os outros valores e se torna global
#     a= 8
#     b+=4
#     c=2
#     print(f'A dentro vale {a}')
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c}')
#
# a = 5
# teste(a)
# print(f'A fora vale {a}')
# def parimpar(n=0):
#     if n%2==0:
#         return True
#     else:
#         return False
# num = int(input('Digite um número: '))
# print(parimpar())

#desafio 101

from datetime import date
# def voto(ano_nascimento):
#     global voto
#     voto=0
#     if voto < 18 and voto < 65:
#         print('Seu voto é obrigatorio')
#     elif voto < 18 :
#         print('Você não tem idade para votar')
#     else:
#         print('Seu voto é facultativo')
#     return voto
#
#
# ano_nascimento=int(input('Qual a sua idade :'))
# print(ano_nascimento)


# def voto(ano):
#     from datetime import date
#     atual=date.today().year
#     idade = atual- ano
#     if idade > 18 and idade < 65:
#          return f'Seu voto é obrigatorio pois sua idade é {idade}'
#     elif idade < 18 :
#          return f'Você não tem idade para votar pois tem {idade}'
#     else:
#         return f'Seu voto é facultativo pois sua idade é {idade}'
#
# ano=int(input('Qual seu ano de nascimento :'))
# print(voto(ano))

#Exercício 103

# def fatorial (n,show =False):
#     '''
#
#     :param n:O número a ser culculado
#     :param show:É opcional mostra ou não a conta
#     :return:O valor de um número
#     '''
#     f=1
#     for c in range (n,0,-1):
#         if show:
#             print(c,end='')
#             if c > 1:
#                 print(" x ",end='')
#             else:
#                 print('= ',end='')
#         f*=c
#     return f
# n=int(input("Digite  um número que eu mostro o seu fatorial :"))
# print(fatorial(n,show=True))
# help(fatorial)

#Exercício 104
# def ficha(nome='desconhecido',gols=0):
#     print(f'O nome do jogador é {nome} e ele fez {gols}')
#
#
#
# print('Ficha do jogador')
# n=str(input("Digite o nome do jogador : "))
# g=input("Digite quantos gols ele fez: ")
# if g.isnumeric():
#     g=int(g)
# else:
#     g = 0
# print(30*'=-')
#
# if n.strip()=='':
#     ficha(gols=g)
# else:
#     ficha(n,g)

#Exercício 105
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n=str(input(msg))
        if n.isnumeric():
            valor=int(n)
            ok=True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\33[m')
        if ok:
            break
    return valor

n = leiaInt('Digite um número:')
print(f'Você acabou de digitar o número {n}')