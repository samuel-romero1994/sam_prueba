print("Este es un programa que calcula los días de vacaciones de sus trabajadores")
print("Los días correspondientes se determinan por departamento y por tiempo de antiguedad")
print("Los departamentos se determinan por clave: ")
print("Clave 1: Atención a clientes")
print("Clave 2: Logistica")
print("Clave 3: Gerencia")
nombre=input("Ingrese su nombre ")
clave=int(input("Ingrese la clave correspondiente a su departamento "))

if clave==1:
    antiguedad=float(input(nombre+ " Ingrese en años su antiguedad "))
    if antiguedad>=1 and antiguedad<2:
        print(nombre+" te corresponden 6 días de vacaciones ")
    if antiguedad>=2 and antiguedad<6:
        print(nombre+" te corresponden 14 días de vacaciones ")
    if antiguedad>=7:
        print(nombre+" te corresponden 20 días de vacaciones ")
    if antiguedad<1 and antiguedad>=0:
        print(nombre+" no tienes derecho a vacaciones")

elif clave==2:
    antiguedad=float(input(nombre+ " Ingrese en años su antiguedad "))
    if antiguedad>=1 and antiguedad<2:
        print(nombre+" te corresponden 7 días de vacaciones ")
    if antiguedad>=2 and antiguedad<6:
        print(nombre+" te corresponden 15 días de vacaciones ")
    if antiguedad>=7:
        print(nombre+" te corresponden 22 días de vacaciones ")
    if antiguedad<1 and antiguedad>=0:
        print(nombre+" no tienes derecho a vacaciones")

elif clave==3:
    antiguedad=float(input(nombre+ " Ingrese en años su antiguedad "))
    if antiguedad>=1 and antiguedad<2:
        print(nombre+" te corresponden 10 días de vacaciones ")
    if antiguedad>=2 and antiguedad<6:
        print(nombre+" te corresponden 20 días de vacaciones ")
    if antiguedad>=7:
        print(nombre+" te corresponden 30 días de vacaciones ")
    if antiguedad<1 and antiguedad>=0:
        print(nombre+" no tienes derecho a vacaciones")
else:
    print("La clave no es valida")
