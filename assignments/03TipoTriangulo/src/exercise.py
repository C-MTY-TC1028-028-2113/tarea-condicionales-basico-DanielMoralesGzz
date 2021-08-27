def main():
    lado1 = int(input("Ingresa la medida del lado 1: "))
    lado2 = int(input("Ingresa la medida del lado 2: "))
    lado3 = int(input("Ingresa la medida del lado 3: "))
    lados=[lado1,lado2,lado3]
    s_lados=sorted(lados)
    #Escribe aquí tu código...
    if(s_lados[0]+s_lados[1]>s_lados[2]):
        if(s_lados[1]==s_lados[2] and s_lados[1]==s_lados[0]):
            print('ES UN TRIANGULO EQUILATERO')
        elif(s_lados[1]==s_lados[2] and s_lados[1]!=s_lados[0]):
            print('ES UN TRIANGULO ISOSCELES')
        elif(s_lados[1]==s_lados[0] and s_lados[1]!=s_lados[2]):
            print('ES UN TRIANGULO ISOSCELES')
        else:
            print('ES UN TRIANGULO ESCALENO')
    else:
        print('NO ES TRIANGULO')

if __name__=='__main__':
    main()
