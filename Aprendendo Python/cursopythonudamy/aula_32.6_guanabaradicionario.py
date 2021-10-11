# from datetime import datetime
# dados = dict()
# dados['nome']=str(input("Nome: "))
# nasc = int(input('Ano de Nascimento:'))
# dados['idade'] = datetime.now().year-nasc
# dados['ctps'] = int(input("Nº da ctps(digite '0' caso não tenha) :"))
# print(dados)
# if dados['ctps'] != 0:
#     dados['anocont']=int(input('Qual seu ano de contração:'))
#     dados['salario']=int(input('Seu salário:'))
# dados['aposetadoria'] =dados['anocont']+35-(nasc)
# print(dados)
#
galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome']=str(input('Nome: '))
    while True:
        pessoa['sexo']= str(input('sexo  [M/F]: ')).upper()[0]

        if pessoa['sexo'] in 'MF':
            break
        print('Digite um codigo valido ')
    pessoa['idade']=int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        res = str(input("Quer continuar ?[S/N] ")).upper()[0]
        if res in 'SN':
            break
        print('Erro ! Responda apenas S ou N. ')
    if res == 'N':
        break
print(galera)
média = soma /len(galera)
print(f'O Número de pessoas cadastrada é {len(galera)}')
print(f'A media das idades é  {(média):5.2f}')
print(f'As mulheres cadastrads foram ',end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}',end =' ')
print()
print('A lista de pessoas que estão acima da média:')
for p in galera:
    if p['idade'] >= média:
        print('   ',end='')
        for k , v in p.items():
            print(f'{k} = {v};',end =' ')
            print()
print('<<ENCERRADO>>')