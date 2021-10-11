"""
For in em python
Iterando strings com for
Função range recebe três argumentos (star = a,stop, step=1)
"""
# texto = 'Python'
# for letra in texto:
#     print( letra )
'''texto = 'Python'
for n,letra in enumerate(texto) :
    print(n,letra) '''

# print("Escolha um número e veja a sua tabuada ")
# mult = int(input("Digite um numero :"))
# for n in range(1, 11):
#     print( f"{mult} X {n} = {mult * n}")
         # continue - pua o próximo laço
         # break - termina o laço 
texto = 'python'
novo_string =''
for letra in texto:
    if letra=='t'  :
        novo_string =novo_string +letra.upper()
    elif letra =='p':
          novo_string +=letra.upper()
    else:
        novo_string += letra

print(novo_string)