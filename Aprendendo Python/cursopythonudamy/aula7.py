nome='João Lucas'
anon=1989
anoatu=2021
idade=anoatu-anon
altura=1.89
e_maior= idade>18
print(nome, type(nome))
print(type(20))
print("Meu nome é :",nome)
print("Minha idade é  :",idade,"anos")
print("Minha altura  é ' :",altura,"cm")
print('É maior:',e_maior)
peso=92
imc=peso/altura**2
print(f'{nome} tem {idade} anos e seu IMC é {imc:.2f}')#Só vai exibir duas casas decimais por isso o .2f sendo o "f" ponto flutuante
print("'já sei!'")