# Declaración Clase Cliente
# Clase que almacenará los datos del cliente con el que queremos trabajar
class Cliente:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} - Email: {self.email}, Tel: {self.telefono}"

# Declaración Clase SistemaClientes
# Clase para operar con la colección de clientes
class SistemaClientes:
    def __init__(self):
        self.lista_clientes = [] #lista para almacenar los objetos Cliente
    
    #Agregar nuevos clientes a la lista
    def agregar_cliente(self, nuevo_cliente):
        self.lista_clientes.append(nuevo_cliente)
        print (f"Cliente '{nuevo_cliente.nombre}' agregado al sistema. ")

    #Eliminar clientes de la lista buscando por nombre
    def eliminar_cliente(self, nombre_cliente):
        #Comprobación de lista no vacía
        if not self.lista_clientes:
            print("No hay clientes en el sistema para eliminar. ")
            return
        #La variable se inicializa antes del bucle para evitar errores en la búsqueda
        cliente_a_eliminar = None
        #Búsqueda del cliente a eliminar
        for cliente in self.lista_clientes:
            if cliente.nombre == nombre_cliente:
                cliente_a_eliminar = cliente
                break
        #Verificación si se encontró al cliente y borrado
        if cliente_a_eliminar is not None:
            self.lista_clientes.remove(cliente_a_eliminar)
            print(f"Cliente '{nombre_cliente}' eliminado del sistema. ")
        else:
            print(f"Cliente '{nombre_cliente}' no encontrado. ")
    
    # Buscar clientes por nombre
    def buscar_cliente(self, nombre_cliente):
        for cliente in self.lista_clientes:
            if cliente.nombre == nombre_cliente:
                return cliente
        return None
    
    # Mostrar la lista de clientes
    def listar_clientes(self):
        if not self.lista_clientes:
            print(f"No hay clientes en el sistema. ")
        else: 
            for cliente in self.lista_clientes:
                print(cliente)

