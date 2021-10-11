# teste = list()
# teste.append('Lucas')
# teste.append('32')
# galera = list()
# galera.append(teste[:])
# teste[0]= 'Maria'
# teste[1]=22
# galera.append(teste)
# print(galera)

# familia =[['Lasla',27],['Maurina',54],['Mariana',22],['Roberto',54]]
# for p,i in familia:
#     print(f'Oi você cuje o nome é {p} tem a idade de {i}')
#
conhecidos = list()
dado = list ()
totalmais=totalmenos=0
for c in range(0,3):
    dado.append(str(input('Nome:')))
    dado.append(int(input("Idade: ")))
    conhecidos.append(dado[:])
    dado.clear()
print(conhecidos)
for p in conhecidos:
    if p[1] >=21:
        print(f'{p[0]} é maior de idade')
        totalmais+=1
    else:
        print(f'{p[0]} é menor de idade')
        totalmenos+=1
if totalmenos == 0:
    totalmenos= 'nenhum '
print(f' Temos um total de  {totalmais} maiores de idade e {totalmenos} menores.')