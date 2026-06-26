import os
import sys
import random
import subprocess

# Carpeta donde se almacenan los tickets
CARPETA_TICKETS = "tickets/"


# Función para limpiar la consola
def limpiar_pantalla():
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run([comando], shell=True)


# Función para generar un nuevo ticket
def alta_ticket():

    while True:

        limpiar_pantalla()

        print("===== GENERAR NUEVO TICKET =====\n")

        nombre = input("Nombre: ")
        sector = input("Sector: ")
        asunto = input("Asunto: ")
        problema = input("Problema: ")

        # Genera un número de ticket que no exista
        while True:
            numero_ticket = random.randrange(1000, 9999)
            ruta = CARPETA_TICKETS + str(numero_ticket) + ".txt"

            if not os.path.isfile(ruta):
                break

        archivo = open(ruta, "w")

        archivo.write("Numero de Ticket: " + str(numero_ticket) + "\n")
        archivo.write("Nombre: " + nombre + "\n")
        archivo.write("Sector: " + sector + "\n")
        archivo.write("Asunto: " + asunto + "\n")
        archivo.write("Problema: " + problema + "\n")

        archivo.close()

        print("\n======================================")
        print("         TICKET GENERADO")
        print("======================================")
        print("Número de Ticket:", numero_ticket)
        print("Nombre:", nombre)
        print("Sector:", sector)
        print("Asunto:", asunto)
        print("Problema:", problema)
        print("======================================")

        print("\n¡Recuerde guardar el número de su ticket!")

        while True:

            respuesta = input("\n¿Desea generar otro ticket? (S/N): ").upper()

            if respuesta == "S":
                break

            elif respuesta == "N":
                return

            else:
                print("\nRespuesta inválida. Ingrese S o N.")


# Función para leer un ticket existente
def leer_ticket():

    while True:

        limpiar_pantalla()

        print("======================================")
        print("          LEER TICKET")
        print("======================================\n")

        numero = input("Ingrese el número de Ticket: ")

        ruta = CARPETA_TICKETS + numero + ".txt"

        if os.path.isfile(ruta):

            archivo = open(ruta, "r")

            print("\n======================================")
            print("             TICKET")
            print("======================================\n")
            print(archivo.read())

            archivo.close()

        else:

            print("\nEl ticket no existe.")

        while True:

            respuesta = input("\n¿Desea leer otro ticket? (S/N): ").upper()

            if respuesta == "S":
                break

            elif respuesta == "N":
                return

            else:
                print("\nRespuesta inválida. Ingrese S o N.")


# Función para salir del programa con confirmación
def salir():

    while True:

        limpiar_pantalla()

        respuesta = input("¿Está seguro que desea salir? (S/N): ").upper()

        if respuesta == "S":
            print("\n¡Gracias por utilizar el Sistema de Tickets!")
            sys.exit()

        elif respuesta == "N":
            break

        else:
            print("\nRespuesta inválida. Ingrese S o N.")
            input("\nPresione ENTER para continuar...")
            

# Función que muestra el menú principal
def menu():

    while True:

        limpiar_pantalla()

        print("====================================")
        print("   BIENVENIDO AL SISTEMA DE TICKETS")
        print("====================================\n")

        print("1 - Generar un Nuevo Ticket")
        print("2 - Leer un Ticket")
        print("3 - Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            alta_ticket()

        elif opcion == "2":
            leer_ticket()

        elif opcion == "3":
            salir()

        else:
            print("\nOpción inválida.")
            input("\nPresione ENTER para continuar...")

menu()