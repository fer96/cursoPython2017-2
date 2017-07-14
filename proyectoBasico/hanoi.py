#Torres de Hanoi
#para n cantidad de discos

#Hecho por: De La Rosa Salas Fernando

#Consideracion: en la forma "gráfica" las torre no se mantienen en
#el mismo lugar, tienen una rotación

#Funcion para mostrar de forma gráfica
def dibujo(numNiveles,disco,torreInicial,torreFinal,torreAuxiliar):
    if disco in torreInicial:
        #borra el inicio
        #del torreFinal[1]

        #borra el primer elemento cero de la torre final
        torreFinal.remove(0)
        
        #agrega al final
        torreFinal.append(disco)
        #borra disco en torre inicial
        torreInicial[torreInicial.index(disco)]=0
    else:
        pass
    for i in range(numNiveles,-1,-1):
        if i==0:
            print("\t-------------------")
        else:
            pass
        print("\t",torreInicial[i],"\t",torreAuxiliar[i],"\t",torreFinal[i])

#funcion que resuelve
def hanoi(niveles,disco,torreInicial,torreFinal,torreAuxiliar,a,c,b):
    if disco==1:
        print("Mueve el disco: 1 de la torre:",a,"a la torre: ",c)
        dibujo(niveles,disco,torreInicial,torreFinal,torreAuxiliar)
    else:
        hanoi(niveles,disco-1,torreInicial,torreAuxiliar,torreFinal,a,b,c)
        print("Mueve el disco: ",disco,"de la torre:",a,"a la torre: ",c)
        dibujo(niveles,disco,torreInicial,torreFinal,torreAuxiliar)
        hanoi(niveles,disco-1,torreAuxiliar,torreFinal,torreInicial,b,c,a)
    
#programa principal
numNiveles=int(input("Ingresa el número de discos de la torre: "))

#listas que sirve para "dibujar" el procedimiento
a=list(range(1,numNiveles+1,1))
b,c=[],[]
#inicializando en 0 para que todas tengan la misma longitud
for i in a:
    b.append(0)
    c.append(0)
a.reverse()
#Agregando un identificador a las torres
a.insert(0,'A')
b.insert(0,'B')
c.insert(0,'C')


hanoi(numNiveles,numNiveles,a,c,b,'A','C','B')
