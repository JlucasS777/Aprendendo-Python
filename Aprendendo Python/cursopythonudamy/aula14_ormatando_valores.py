"""
Formatando valores com modificadores
:s- Texto (strings)
:d- Inteiros (in)
:f- Números de ponto flutuante (float)
:.-(NÚMEROS)f-Quantidade de casas decimais (float) :.2f
:(CARACTERE)(> OU < OU ^)(QUANTIDADE)(TIPO - s,d ou f)

> - esquerda
< - Direita
^ - Centro
"""
nu1 = 1
print(f"{nu1:.10f}")
nome = 'Lucas'
print((50-len(nome)) /2)
print(f'{nome:#^50}')
teste = 'verificar'
teste_formatado = '{t:&<11}'.format(t=teste) #11 fica menos a quantidade de caracteres da palavra verificadar
print(teste_formatado)
frase1 = 'Vamos passear na floresta enquanto seu lobo chamado Mikael não vem'
print(frase1.lower())
print(frase1.upper())
print(frase1.title())
