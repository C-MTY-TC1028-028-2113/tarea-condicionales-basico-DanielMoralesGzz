def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))
    ind=peso/(altura**2)
    if(peso<=0 or altura<=0):
        print('Revisa tus datos, alguno de ellos es erróneo.')
    elif (ind<20):
        print('PESO BAJO')
    elif(ind<25):
        print('NORMAL')
    elif(ind<30):
        print('SOBREPESO')
    elif(ind<40):
        print('OBESIDAD')
    else:
        print('OBESIDAD MORBIDA')

if __name__=='__main__':
    main()