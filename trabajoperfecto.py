N= int(input ('ingrese N= '))
K= int(input ('ingrese K= '))

def calculadivisoresdeN(N:int) -> list:   
    divisoresN=list()
    for j in range(1,N+1): 
        if (N % j)==0: 
            divisoresN.append(int(j))
    print(divisoresN)
    return divisoresN
divisores = calculadivisoresdeN(N)

suma=0
for i in divisores:
    suma=i+suma
print(suma)

def esMulti(suma):
    if suma==(K*N):
        print('es multi')
    else:
        print('NO es multi')
esMulti(suma) 