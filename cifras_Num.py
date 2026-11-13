
print ("Este programa calcula si un numero entero pertenece al sistema decimal (0-9), si se cumple dicha condicion se informa cuantas cifras posse y la sumatoria de estas")
print ()
num= int (input("Por favor ingrese el numero a calcular: "))
if num>0:
    copia_Num= num
    contador_Cifra=0
    suma_Cifras = 0
    while copia_Num>0:
        cif= copia_Num%10
        copia_Num = copia_Num//10
        suma_Cifras += cif
        contador_Cifra += 1
    print ()
    print (f"La cantidad de cifras es de : {contador_Cifra}")
    print ()
    print (f"son: {contador_Cifra}")
    print ()
    print (f"La sumatoria es : {suma_Cifras}")
    print ()
else:
    print ("El numero ingresado NO es nu numero positivo, por favor intentalo nuevamente")
    print ()
