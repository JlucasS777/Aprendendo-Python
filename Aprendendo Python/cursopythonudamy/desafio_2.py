print('Com o laço for :')
b =0
for a in  range (0,9):
    b= 10 -a
    print(a,b)
#forma mais fácil :
print("Forma no professor:")
for p,r in enumerate(range(10,1,-1)):
    print(p,r)


print("Mesmo assunto com o laço while:")
a=-1
b=11
while b>= 1 and a <=7 :
    a+=1
    b-=1
    print(a,b)