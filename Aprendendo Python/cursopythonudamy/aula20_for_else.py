#for /else em python

# variavel = ['João','Lucas','Alcantara', 'Moreira', 'Santos']
# for lista in variavel :
#     print(lista,end=' ')
variavel = ['João','Lucas','Alcantara', 'Moreira', 'Santos']

for lista in variavel :
    if lista.lower().startswith('L'):#essa função é para ver se começa com a letra entre parentese- podesse usar lower
       pass
    print(lista)

else:
     print('Não começa com L',lista)

