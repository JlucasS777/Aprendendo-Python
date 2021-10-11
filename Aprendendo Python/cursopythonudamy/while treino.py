'''cont=' n '
n=int(input("Digite um número :"))
cont = input("Quer continuar ?[s] ou [n]: ")
while cont =='s' or cont == 'sim':
    n=int(input("Digite um número :"))
    cont = input("Quer continuar ?[s] ou [n]: ")
print("Fim do programa!")'''
import numbers

"""n = 1
par=impar=0
while n != 0:
    n= int(input("Digite um número : "))
    if n != 0:
        if n % 2 == 0:
           par+=1
        else:
            print('impar')
            
print(f"Temos um total de {par} números par e {impar} números ímpares"
      f" Fim do program!!!")"""


# meu Jeito de fazer
numbers = 0
print("Ao digitar 999 o programa finalizará !\n")
contador = numbers
soma = 0
somaneg=1
flag01 = 999
while numbers != 999:

    numbers = int(input("Digite um número : ")) # se colocar fora do while dispença as variaveis somaneg e flag 01
    contador += numbers
    soma+=1
    if numbers == 999:
        break


print(f"A soma de todos os números digitados sem o flag é  {contador-flag01} e você digitou {soma-somaneg} números")

# Jeito Guanabara melhor
numbers = soma = 0
print("Ao digitar 999 o programa finalizará !\n")
contador = numbers

numbers = int(input("Digite um número : "))
while numbers != 999:

    numbers = int(input("Digite um número : ")) # se colocar fora do while dispença as variaveis somaneg e flag 01
    contador += numbers
    soma+=1

print(f"A soma de todos os números digitados sem o flag é  {contador} e você digitou {soma} números")



























