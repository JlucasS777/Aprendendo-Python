'''while em Python - Aula 7
utilizando para realizar ações enquanto uma condição for verdadeira.'''
"""while True:
    nome = input(" Qual o seu nome ?")
    print(f'Olá {nome}!')"""
'''x = 0
while x <101 : #'cotinue' pula o laço e 'break' finaliza o laço
    print(x)
    x = x+1 # ou x += 1
print("Fim do programa!!!")'''

while True:
    nu1 = input("Digite um número:")
    nu2 = input("Digite outro número:")
    if not nu1.isnumeric() or not  nu2.isnumeric():
        print("Você precisa digitar um número.")
        continue

    nu1=int (nu1)
    nu2=int (nu2)
    if nu1.numerator or nu2.numerator:
        operador=input("Escolha um operador :")
        if operador == '+':
            print(f"{nu1} + {nu2} ={nu1 + nu2}")
        elif operador =='-':
            print(f"{nu1} - {nu2} ={nu1 - nu2}")
        elif operador == '*' :
            print(f"{nu1} x {nu2} ={nu1 * nu2}")
        elif operador =='/':
            print(f"{nu1} / {nu2} ={nu1/nu2}")



