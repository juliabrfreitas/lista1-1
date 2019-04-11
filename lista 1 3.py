dim=int(input("insira a dimensão aqui"))

def Vetor(dim):
    v1=[]
    v2=[]
    v3=[]
    for i in range(dim):
        x1=int(input("digite a coordenada do primeiro vetor aqui"))
        v1.append(x1)
    for i in range(dim):
        x2=int(input("digite a coordenada do segundo vetor aqui"))
        v2.append(x2)
    for i in range(dim):
        x3=v1[i]+v2[i]
        v3.append(x3)
    print (v3)


Vetor(dim)
