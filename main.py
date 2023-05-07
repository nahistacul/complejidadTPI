from classDef import Numero, Multiperfecto

def esMulti(suma, K, N):
    if suma==(K*N):
        return f'es multi'
    else:
        return f'NO es multi'

if __name__ == "__main__":
    N=Multiperfecto(int(input ('ingrese N= ')))
    K=Numero(int(input ('ingrese K= ')))
    print(N.valor)
    print(K.valor)
    N.setDivisores(N.calcularDivisores())
    suma=N.sumarDivisores()

    N.esMulti(suma,K.valor,N.valor)
    


    