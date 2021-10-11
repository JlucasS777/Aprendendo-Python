# Na identação do python utilizar apenas 4 espaços como convenção
print("Olá meu caro seja bem-vindo ao seu programa PYTHON\n")
num_1=int(input("Digite um número interiro :"))
print("Vamos trabalhar com soma agora ")
num_2=int(input("\nDigite outro número interiro :"))
total=num_1+num_2
if total <=5:
    print(f" A soma é {total} e esse total é menor ou igual a 5  ")
elif total <= 10 :
    print(f" A soma é {total} e esse total é menor ou igual a 10  ")
elif total <=50:
    print(f" \nA soma é {total} e esse total é menor ou igual a 50 ")
else:
    print(f" \nA soma é {total} e esse total é maior que 50 ")
print("\n FIM do Programa")

