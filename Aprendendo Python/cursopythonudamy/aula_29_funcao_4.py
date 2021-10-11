# Variavel local e Global
variavel = 'valor'
def func():
    print(variavel)
func()

def func2():
    global variavel
    variavel = 'Outro valor'
    print(variavel)
func()
func2()
print(variavel)