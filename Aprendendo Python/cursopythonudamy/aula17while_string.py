# É sempre bom no laço while ter uma variável de controle(contador=0)
#parta ctrol / para comentar multiplas linhas

frase = 'O rato roeu a roupa do rei de Roma'# tem valor iterável (percorrer cada elemento da sua string
tamanho_frase = len(frase)
contador= 0
nova_string =''
print(len(frase))
input_do_usuario = input("Qual letra deseja colocar como maiúscula:")
while contador < tamanho_frase:
    #print(frase[contador],contador)
    letra=frase[contador]
    if letra == input_do_usuario:
        nova_string+=input_do_usuario.upper()
    else:
        nova_string +=letra
    print(nova_string)
    contador+=1