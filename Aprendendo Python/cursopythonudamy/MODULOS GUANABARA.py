from uteis import numeros
from moeda import aumento



# num = int(input('Digite um número :'))
# fat =numeros.fatorial(num)
# print(f'fatorial de {num} é {fat}.')
# print(f'O dobro de {num} é {numeros.dobro(num)}')

n=float(input('Digite um valor: '))
t=float(input('Digite a taxa de aumento ou desconto: '))
print(f'O valor de  {aumento.dinheiro(n)} com uma taxa de aumento de {t}% fica no valor de {aumento.aumento(n,t,True)}')
print(f'O valor de  {aumento.dinheiro(n)} com uma redução de  {t}% fica no valor de {aumento.diminue(n,t,True)}')
print(f'O valor de  {aumento.dinheiro(n)} dobrado fica  {aumento.dobra(n,True)}')
print(f'O valor de  {aumento.dinheiro(n)} pela metade fica  {aumento.metade(n,True)}')