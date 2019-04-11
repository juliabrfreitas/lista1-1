x=float(input("insira aqui a coord x da localização"))
y=float(input("insira aqui a coord y da localização"))
d=float(input("insira aqui a distância"))
acumulador=[]
lista=[] #por aqui os 10 a 20 pontos

def Ponto(lista):
    for i in range(len(lista)):
        ponto=lista[i]
        dist=((ponto[0]-x)**2+(ponto[1]-y)**2)**0.5
        if dist<=d:
            acumulador.append(ponto)
    if len(acumulador)!=0:
        print ("Os pontos que estão dentro são:", acumulador]
    else:
        print ("não há nenhum ponto dentro")


Ponto()
