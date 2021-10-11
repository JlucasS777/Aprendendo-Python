'''i = int(input('Onde começar :'))
f = int(input('Onde terminar :'))
t = int(input('Qual o intervalo :'))
for c in range(i,f+t,t):
    print(c)'''

# import time
# for c in range(10,-1,-1):#Esse programa faz uma contagem regressiva.
#     time.sleep(1)
#     print(c)
# print("Feliz 5 mil anos de Novo mundo!!!")

"""print("Veja todos os números pares de 1 a 50")
for c in range(1,52,2):
    print(c)"""

# print("Escolha um número e veja a
# mult = int(input("Digite um numer
# for n in range(1, 11):
#     print( f"{mult} X {n} = {mult
         # continue - pua o próximo
         # break - termina o laço
'''soma = 0
for a in range (6):# desafio 50 de Guanabara
    a = int(input(f"Digite o número inteiro com nome {a} :"))

    if a % 2 == 0:
        soma+=a
print(f"A soma dos valores pares é {soma}")'''

# soma = 0
# soma1 = 0
# for a in range (3):# desafio 54 de Guanabara
#     a = int(input(f" Candidato {a} , favor digite seu ano de nascimento :"))
#     if a <= 2003:
#         soma+=1
#     else:
#         soma1+=1
# print(f"No geral {soma1} pessoas  ainda não atigiram a maior idade e {soma} já atigiram a maior idade ")

'''==========================================================='''

cont = 0
maior = 0
menor = 0
for a in range(1,3) :
    cont+=1
    peso = float(input(f"Qual o seu peso candidato {a} : "))
    if cont == 1:
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior = peso
        if peso<menor:
            menor=peso
print(f"O maior valor foi {maior} e o menor foi {menor}")