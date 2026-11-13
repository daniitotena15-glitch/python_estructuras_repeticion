
print ("Este programa calcula el factorial de un numero N (cualquiera)")
print ()
num= float (input("Por favor ingrese el numero al cual desea conocer el factorial: "))

if num<0:
    print ()
    print (f"El numero ingresado {num} , No cuenta con factorial, intente nuevamente")
    print()
    print(f"Recuerda que los numeros Negativos no cuentan con factorial")
    print()
else:
    fac=1
    num_Infe= 1
    while num_Infe<= num:
        fac *= num_Infe
        num_Infe+=1
    print()
    print(f"El factorial del numero ingresado : {num}, es {fac}")
    print ()