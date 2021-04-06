print("Hola, ingresa un numero y te diré si es par o impar ")
numero=float(input("Ingresa el número "))
div=(numero%2)
if div==0:
    print("Tu numero ",numero," es par")
else:
    print("Tu numero",numero," es impar")