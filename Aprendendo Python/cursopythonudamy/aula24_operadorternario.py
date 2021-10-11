# Operador Ternário

'''login_user = False
if login_user  : # isso é o mesmo que if login_user == True:
    msg = 'Usuário logado'

else:
    msg = 'Usuário precisa logar'
print(msg)
print(i)'''
''' O código acima é o mesmo que :
'''
# login_user = False
# msg ='Usuário logado.'if login_user else ' Usuário precisa logar'
# print(msg)]
print('Seja bem-vindo ao programa sua idade , agora você vai saber se é adulto ou não \n '
'Para sair do program escolha uma idade maior que 120\n')
while True:

    idade = input('Qual a sua idade :')
    if not idade.isnumeric():
        print( 'Você precisa digitar apenas números')
    else:
        idade=int(idade)
        if idade > 120 :
            print('Fim do programa')
            break
        if idade < 120 :
            usario = 'Você é maior de idade'if idade >= 18 else 'Usuario menor de idade, vá brincar de durmir '
            print(usario)