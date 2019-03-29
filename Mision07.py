#Autor: Katia Hernández Barrera
#Programa que ejecuta la opcion que el usuario elija, todas las opciones usan ciclos while

def dividir (b,a):
    cociente = 0
    while b >= a:
        b = b - a
        cociente += 1
    print("Cociente = ", cociente)
    print("Residuo =  ", b)


def encontrarMayor():
    n = int(input("Teclea un número [-1 para salir]:"))
    mayor = -1
    while n != -1:
        n = int(input("Teclea un número [-1 para salir]:"))
        if n > mayor:
            mayor = n
    print("El numero mayor es", mayor)



def main():
    print("Mision 07: ciclos while")
    print("Autor: Katia Hernández Barrera")
    print("Matrícula: A01375906")
    print("1. Calcular divisiones")
    print("2. Encontrar el mayor")
    print("3. Salir")
    opcion = int(input("selecciona una opcion"))

    while opcion >= 1 and opcion <= 3:
        if opcion == 1:
            print("                         ")
            a = int(input("Teclea un divisor"))
            b = int(input("Teclea un dividendo"))
            dividir(a, b)
        elif opcion == 2:
            print ("                          ")
            encontrarMayor()

        elif opcion > 3:
            print("ERROR, inserte un número entre 1 y 3")

        elif opcion == 3:
            print("¡Hasta luego!")
            break

        print("                       ")
        print("Mision 07: ciclos while")
        print("Autor: Katia Hernández Barrera")
        print("Matrícula: A01375906")
        print("1. Calcular divisiones")
        print("2. Encontrar el mayor")
        print("3. Salir")
        opcion = int(input("selecciona una opcion"))




main()