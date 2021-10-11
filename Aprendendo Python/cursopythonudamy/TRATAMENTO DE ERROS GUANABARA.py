# try:
#     a= int(input('Numerador:'))
#     b= int(input('Denominador: '))
#     r = a/b
# except Exception as erro:
#     print(f'O erro encontrado foi {erro.__cause__}')
#
# else:
#     print(f'O resultado é {r}')
#
# finally:
#     print("Volte sempre, muito obrigado ")
def leiaInt(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError,TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue

        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n1=float(input(msg))
        except (ValueError,TypeError):
            print('Erro: Por favor digite um valor válido')
            continue
        except:
            print('Erro , tente novamente')
            return 0
        else:
            return n1




num=leiaInt ('Digite um valor inteiro :')
num2=leiafloat('Digite um número qualquer ')
print(f'O valor digitado foi {num} e {num2}')


