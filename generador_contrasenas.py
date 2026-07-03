import os
import sys
import secrets
import string
import subprocess

# Diccionario con los tipos de caracteres disponibles
diccionario = {
    "letras": string.ascii_letters,
    "numeros": string.digits,
    "caracteres": string.punctuation
}


# Función para limpiar la consola
def limpiar_pantalla():
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run([comando], shell=True)


# Función para generar una contraseña
def generar_contrasena(caracteres_permitidos):

    limpiar_pantalla()

    print("======================================")
    print("     GENERADOR DE CONTRASEÑAS")
    print("======================================\n")

    while True:

        largo = input("Ingrese la longitud de la contraseña: ")

        if largo.isdigit() and int(largo) > 0:
            largo = int(largo)
            break

        else:
            print("\nDebe ingresar un número mayor que 0.\n")

    password = ""

    for i in range(largo):
        password += secrets.choice(caracteres_permitidos)

    print("\n======================================")
    print("     CONTRASEÑA GENERADA")
    print("======================================")
    print("Contraseña:", password)
    print("======================================")

    input("\nPresione ENTER para continuar...")


# Función para salir del programa con confirmación
def salir():

    while True:

        limpiar_pantalla()

        respuesta = input("¿Está seguro que desea salir? (S/N): ").upper()

        if respuesta == "S":
            print("\n¡Gracias por utilizar el Generador de Contraseñas!")
            sys.exit()

        elif respuesta == "N":
            return

        else:
            print("\nRespuesta inválida. Ingrese S o N.")
            input("\nPresione ENTER para continuar...")


# Función que muestra el menú principal
def menu():

    while True:

        limpiar_pantalla()

        print("======================================")
        print("     GENERADOR DE CONTRASEÑAS")
        print("======================================\n")

        print("1 - Generar contraseña solo de letras")
        print("2 - Generar contraseña solo de números")
        print("3 - Generar contraseña de letras y números")
        print("4 - Generar contraseña de letras, números y caracteres")
        print("0 - Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            generar_contrasena(diccionario["letras"])

        elif opcion == "2":
            generar_contrasena(diccionario["numeros"])

        elif opcion == "3":
            generar_contrasena(
                diccionario["letras"] + diccionario["numeros"]
            )

        elif opcion == "4":
            generar_contrasena(
                diccionario["letras"] +
                diccionario["numeros"] +
                diccionario["caracteres"]
            )

        elif opcion == "0":
            salir()

        else:
            print("\nOpción inválida.")
            input("\nPresione ENTER para continuar...")


menu()