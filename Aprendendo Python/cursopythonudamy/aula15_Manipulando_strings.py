"""
Mani
Manipulando strings - Aula 6
*String índeces
* Fatiamento de strngs [inicio:fim:passo]
*funções built-in len, abs, type , print, etc...
Essas funções podem ser usadas diretamente em cada tipo.
Você pode conferir tudo isso em:
https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/library/functions.html
Nos documentos oficiais do Python
"""
# positivos [0123456789] Acessando índices
aprendendo = 'aprendIzagem'
print(aprendendo[2])
url = 'www.google.com.br/'
print(url[:-1])
nova_string = aprendendo[6:9]# para o final sempre um número a mais ou seja do 6 iniciando de zero até o 9 só vai pegar o 8 .
print(nova_string)
fatiamento = '0123456789'
print(fatiamento[::2]) # Nesse caso o numero está pulando de 2 em 2
print(fatiamento[0:8])
print(fatiamento[3:-2])

