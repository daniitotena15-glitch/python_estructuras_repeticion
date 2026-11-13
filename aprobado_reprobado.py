
print ("Este programa calcula cuantos estudiantes ingresados al sistema reprueba o aprueban el curso")
print ()
can_Estu = int (input("Por favor ingrese la cantidad de estudiantes que desea ingresar al sistema: "))
num_Conta = 0
apro = 0
repro =0
promedio = 0
while num_Conta<can_Estu :
    nota_Estu= float(input("Por favor ingrese la nota del estudiante: "))
    print ()
    promedio+=nota_Estu
    print ()
    if nota_Estu >= 3.0:
        apro += 1
    else:
        repro +=1
   
    num_Conta +=1

promedio_Grp = promedio/can_Estu
print (f"La Cantidad de estudiantes que aprobaron son: {apro}")
print()
print (f"La cantidad de estudiantes que reprobaron son: {repro}")
print()
print (f"El promedio total de estudiantes ingresados al sistema fue de : {promedio_Grp:.2f}")
print ()



