print("Hola, este es un programa que convierte letras a número y bicebersa")
print("Menu:")
print("Presiona 1 si deseas convertir un número a sus letras: ")
print("Presiona 2 si deseas convertir letras a su número: ")
menu=int(input("¿Cúal es tu opción?: "))
if menu==1:
    num=int(input("Ingresa un número para convertirlo a letra: "))
    if num==0:
        print("Tu número es: CERO")
    elif num==1:
        print("Tu número es: UNO")
    elif num==2:
        print("Tu numero es: DOS")
    elif num==3:
        print("Tu numero es: TRES")
    elif num==4:
        print("Tu numero es: CUATRO")
    elif num==5:
        print("Tu numero es: CINCO")
    else:
        print("Tu numero es invalido")
elif menu==2:
    letra=input("Ingresa con letra el número que quieres convertir: ")
    letra=letra.lower()#convierto lo que haya tecleado sin importar mayusculas o minusculas y lo convierte a minusculas
    if letra=="cero" or letra=="CERO":
        print("Tu numero es: 0")
    elif letra=="uno" or letra=="UNO":
        print("Tu numero es: 1")
    elif letra=="dos" or letra=="DOS":
        print("Tu numero es: 2")
    elif letra=="tres" or letra=="TRES":
        print("Tu numero es: 3")
    elif letra=="cuatro" or letra=="CUATRO":
        print("Tu numero es: 4")
    elif letra=="cinco" or letra=="CINCO":
        print("Tu numero es: 5")
    else:
        print("Tu numero es invalido")
else:
    print("Tu opcion es invalida")
