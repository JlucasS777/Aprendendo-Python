def aumento(n=0,t=0,formato=False):
    res=n+(n*t)/(100)
    return res if not formato is False else dinheiro(res)


def diminue(n=0,t=0,formato=False):
    res= n - (n * t) / (100)
    return res if not formato is False else dinheiro(res)

def dobra(n=0,formato=False):
    res=n * 2
    return res if not formato is False else dinheiro(res)

def metade(n=0,formato=False):
    res = n / 2
    return res if not formato is False else dinheiro(res)


def dinheiro (dindin=0,simbolo='R$'):
    return f'{simbolo}{dindin:>8.2f}'.replace('.',',')

