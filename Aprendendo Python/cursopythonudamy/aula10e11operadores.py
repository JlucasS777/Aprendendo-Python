#Operadores relacionais(<><=...) e lógicos(and,or,not in e not in) :

"""nome = 'Joao Lucas'
if 'z' in nome: # Se J tem dentro(in) da variavel nome
    print("Minha mãe me dizia meu filho meu filho tu vai ver coisa ....")
else:
    print('É mentira de DINDINHA')"""
'''Esse programa foi melhorado depois de aprender o laço for'''
print("Para fazer o login , por favor digite seu login e a senha do usuário:\n")
lcerto='Lucaseu'
scerto = '1107Lu'
login=senha=""
while login != scerto or login != lcerto :
    login=input("Digite seu Login: ")

    senha=input("Digite sua Senha: ")

    if senha==scerto and login==lcerto:
        print("Você fez login !")
        break
    else:
            print("Login ou senha incorretos tente novamente:")
print("Fim do programa")



