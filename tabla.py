
print("Este programa genera una tabal segun el numero que ingreses al sistema")
print ()

canti_Num = int (input("Por favor ingrese la cantidad de numeros: "))

print("N\tN²\tN³")

for num in range(1, canti_Num + 1):
      print(f"{num}\t{num**2}\t{num**3}")







'''for num in range(1, canti_Num + 1):
      print(f"{num}, {num**2}, {num**3}")'''

''' tener en cuenta que estos simbolos sirven para:
\n	Salto de línea
\t	Tabulación
\"	Comilla doble
\'	Comilla simple
\\	Barra invertida'''