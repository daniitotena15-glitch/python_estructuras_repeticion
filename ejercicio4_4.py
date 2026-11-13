
print ("Este programa clacula si un numero N, pertenece al grupo de numero marcisistas o de Armstrong")
print ()
num = int(input("Por favor ingrese el numero que desea calcular: "))
num_ori=num
cop_Num=num
conta_Cifras= 0

if num >=0:
    while cop_Num>0:
        cop_Num = cop_Num//10
        conta_Cifras +=1
    suma= 0
    cop_Num=num
    while cop_Num>0:
        cifra= cop_Num %10
        suma +=cifra**conta_Cifras
        cop_Num= cop_Num//10
        print ()
        print (f"El numero ingresado es: {num}")
        print()
        print (f"Cantidad de cifras: {conta_Cifras}")
        print ()
        print (f"Suma calculda: {suma}")
        print ()

        if suma==num_ori:
            print (f"El numero {num_ori} Es un numero Armstrong")
        else:
            print (f"El numero {num_ori} NO es un numero Armstrong")
            print ()
else:
    print ()
    print(f"El numero ingresado NO es valido para realizar el calculo por favor intente nuevamente")