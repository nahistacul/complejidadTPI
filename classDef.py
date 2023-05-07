class Numero():
    def __init__(self,valor=0,divisores=[]):
        self.valor=valor;
        self.divisores=divisores;
    
    def setDivisores(self, valores:list):
        self.divisores=valores

    def calcularDivisores(self) -> list:   
        divisoresN=list();
        for j in range(1,self.valor+1): 
            if (self.valor % j)==0: 
                divisoresN.append(int(j))
        return divisoresN;
    

class Multiperfecto(Numero):
    def sumarDivisores(self) -> float:
        suma=0
        for i in self.divisores:
            suma=i+suma
        return suma;



        


