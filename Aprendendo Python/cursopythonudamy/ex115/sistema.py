from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep
arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
  criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoa cadastrada','Cadastrar nova Pessoa','Sair do Programa'])
    if resposta == 1:
        #opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('Novo Cadastro')
        nome= str(input('Nome:'))
        idade = leiaInt('idade: 1')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        cabeçalho('\033[36mSaindo do sistema... Até logo!\033[m')
        break
    else:
        print("\033[31mErro! Digite uma opção valida!\033[m")
        sleep(2)
