#Se importan las clases del archivo clases.py
from clases import *

#Definiciión de la función que muestra el menú por pantalla
def pintamenu():
    print("\n")
    print("================================")
    print(" Sistema de Gestión de Clientes ")
    print("================================")
    print("1. Agregar un cliente")
    print("2. Eliminar un cliente")
    print("3. Buscar un cliente")
    print("4. Listar todos los clientes")
    print("5. Salir")
    print("================================")

#Definición de la función para recoger los datos del cliente
def obtener_datos_cliente():
    while True:
        nombre = (input("Ingrese el nombre del cliente: "))
        if nombre.isalpha() and nombre.strip(): #Solo debe contener letras y no estar vacío
            break
        else:
            print("Por favor, ingrese un nombre válido que contenga solo letras. ")
    while True:
        email = (input("Ingrese el email del cliente: "))
        if '@' in email and '.' in email: #Debe contener al menos @ y .
            break
        else:
            print("Por favor, ingrese un email válido. ")
    while True:
        telefono = (input("Ingrese el teléfono del cliente: "))
        if telefono.isdigit() and telefono.strip(): #Debe estar compuesto solo por números
            telefono = int(telefono)
            break
        else:
            print("Por favor, ingrese un número de teléfono válido que contenga solo dígitos. ")
    return Cliente(nombre, email, telefono)

    

