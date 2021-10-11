'''pessoas = {'nome':'Lucas','sexo':'masculino','idade':32}
print(f"O Servo {pessoas['nome']} tem {pessoas['idade']} de idade ")
print(pessoas.values())
print(pessoas.items())
pessoas ['nome'] = 'João Lucas'# Esse comando substituio o nome Lucas por João Lucas
pessoas ['peso'] = 90.5# adicionei ao meu dicionário o peso
for k,v in pessoas.items():
    print(f'{k} = {v}')
#del pessoas['sexo'] - esse comando apagar o sexo do dicionário'''

#Dicionario dentro de uma lista
'''estado = dict() # também posso declarar dicionário dessa forma
brasil = list()#também posso declarar lista dessa forma
for c in range (1,3):
    estado['uf'] = str(input('Unidade Federativa :'))
    estado['sigla'] = str(input('Sigla do estado :'))
    brasil.append(estado.copy())# tem que usar a função copy para dar certo
print(brasil)
for e in brasil :
    for k, v in e.items():
        print(f" O campo {k} tem valor {v}.")'''
#Desafio 90
alunos ={}
continuar=0
for f  in range(3):
    notas = float(input(f'Qual a sua nota {f+1}: '))
alunos['media']=notas
while True:

    alunos['nome']=str(input('Qual o seu nome:'))


    if alunos['media'] >= 7:
        alunos['situação']='aprovado'
    else:
        alunos['situação'] = 'Reprovado'
    continuar=int(input("Quer continuar 1 para sim e 2 para não digite:"))

    if continuar == 2:
        break


print(alunos)
for f  in range(3):
    notas = float(input(f'Qual a sua nota {f+1}: '))