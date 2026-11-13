
print ("Funcion")
print ()
valor_x=int (input("Por favor ingrese el valor maximo para X: "))

def f(x):
        return x**3+ x**2-5

x=0

while x <= valor_x:
    print()
    print (f"Para X = {x} , f(x)= {f(x)}")
    x += 1
    print()
    