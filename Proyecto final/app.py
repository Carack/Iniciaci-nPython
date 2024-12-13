#Autor: Juan Andrés Lorenzo García
#Fecha fin: 26/08/2024

#Se importan las clases y las funciones de los archivos clses.py y funciones.py
from clases import Cliente, SistemaClientes
from funciones import pintamenu, obtener_datos_cliente

#Función principal del programa   
def main(): 
    #Creación de la instancia de SistemaClientes
    sistema_gestion = SistemaClientes()
    #Código principal
    try: #Control de interrupción de teclado
        #Ejecución principal
        while True:
            pintamenu()
            opcion = input ("Selecciona una opción: ")

            if opcion == '1':
                #Método para Agregar cliente
                nuevo_cliente = obtener_datos_cliente()
                sistema_gestion.agregar_cliente(nuevo_cliente)
            elif opcion == '2':
                #Método para Eliminar cliente
                nombre = input("Ingrese el nombre del cliente a eliminar: ")
                sistema_gestion.eliminar_cliente(nombre)
            elif opcion == '3':
                #Método para buscar clientes
                nombre = input("Ingrese el nombre del cliente a buscar: ")
                cliente=sistema_gestion.buscar_cliente(nombre)
                if cliente:
                    print(f"Cliente encontrado: {cliente}")
                else:
                    print(f"Cliente no encontrado. ")
            elif opcion == '4':
                #Método para listar todos los clientes
                sistema_gestion.listar_clientes()
            elif opcion == '5':
                #Salir del programa
                print("Saliendo del sistema de gestión de clientes. ")
                break
            else:
                #Para la introducción de cualquier valor no contemplado
                print("Opción no válida. Por favor, inténtelo de nuevo introduciendo un valor entre 1 y 5. ")
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario. ")

#Ejrcución principal del programa
if __name__ == "__main__":
    main()

