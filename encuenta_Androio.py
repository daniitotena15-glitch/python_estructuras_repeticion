
print("Este programa calcula que plataforma es mas utilizada por n cantidad de estudiantes")
print()

canti_Estu = int(input("Por favor ingrese la cantidad de estudiantes que se desean encuestar: "))

conta_Estu = 0
android = 0
ios = 0

while conta_Estu < canti_Estu:

    opc = int(input(
        "Por favor ingrese la opcion que quiera.\n"
        "Recuerda que para Android es = 1 y para iOS es = 2: "
    ))

    if opc != 1 and opc != 2:

        print()
        print("La opcion ingresada NO es valida, intente nuevamente")
        print()

    else:

        if opc == 1:

            print("La opcion elegida fue Android")
            print()

            android += 1

        else:

            if opc == 2:

                print("La opcion elegida fue iOS")
                print()

                ios += 1

            else:

                print("Intente nuevamente")

    conta_Estu += 1


print()
print(f"Cantidad de votos Android: {android}")
print(f"Cantidad de votos iOS: {ios}")
print()

if android > ios:

    print("La plataforma mas utilizada es Android")

elif ios > android:

    print("La plataforma mas utilizada es iOS")

else:

    print("Las plataformas cuentan con un empate")
