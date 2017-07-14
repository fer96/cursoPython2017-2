#Torres de Hanoi
#para n cantidad de discos

#funcion principal
def hanoi(n,torreInicial,torreFinal,torreAuxiliar):
    if n==1:
        print("Mueve el disco: 1 de la torre: ",torreInicial,"a la torre: ",torreFinal)
    else:
        hanoi(n-1,torreInicial,torreAuxiliar,torreFinal)
        print("Mueve el disco: ",n,"de la torre: ",torreInicial,"a la torre: ",torreFinal)
        hanoi(n-1,torreAuxiliar,torreFinal,torreInicial)

#programa principal
numDiscos=int(input("Ingresa el número de discos de la torre: "))
hanoi(numDiscos,'A','C','B')
