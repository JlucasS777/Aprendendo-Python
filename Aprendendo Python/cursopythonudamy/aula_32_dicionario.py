# Dicionário
# d1={'chave1':'valor da chave'}
# print(type(d1))

'''d1 = {
    'str':'valor',
    123:'outro valor',
    (1,2,3,4) : 'Tupla',
}
# apagar chaves - deld1['str']
# d1['str'] ='Agora ela existe'
# print(len(d1)) vai me informar quantos pares eu tenho no meu dicionário
if d1.get('str') is not None:
    print(d1.get('str'))
print(123)
print(len(d1))'''
# d1 = {
#     'chave1':'valor',
#     'chave2':'outro valor',
#     'chave3' : 'Tupla',
# }
# for k in d1.items():# .values acessa o valor sem isso mostra o nome das chaves já items() mostra a chave e o valor
#     print(k[0],k[1])

''' criando dicionário dentro de dicionário :'''

# clientes = {
#     'cliente1' :{
#         'nome':'Lucas',
#         'sobreme' :'Alcântara',
#     },
#     'Cliente2':{
#         'nome':'Lasla',
#         'sobrenome': 'Brito',
#     },
#     'Cliente3':{
#         'nome':'Alteza',
#         'sobrenome': 'Real',
#     },
#
# }
# for principal_clientes,secundario_cliente in clientes.items():
#     print(f'Exibindo{principal_clientes}')
#     for dados_k, dados_v in secundario_cliente.items():
#         print(f'\t{dados_k}={dados_v}')

d1= {1:'a',2:'b',3:'c','d':['Lasla','Jailton']}
v= d1.copy()# Utilizar a função copy para só haver alteração nessa lista
v[1]='João Lucas Santos '
print(v['d'][0])
print(d1)
print(v)
# usando a função .update() podemos juntar dois dicionários 