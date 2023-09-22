class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        self.clientes = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_empleados(self):
        print(f"Empleados de la empresa {self.nombre}:")
        for empleado in self.empleados:
            empleado.mostrar_informacion()

    def mostrar_clientes(self):
        print(f"Clientes de la empresa {self.nombre}:")
        for cliente in self.clientes:
            cliente.mostrar_informacion()

class Empleado:
    def __init__(self, nombre, edad, sueldo_bruto):
        self.nombre = nombre
        self.edad = edad
        self.sueldo_bruto = sueldo_bruto

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Sueldo Bruto: {self.sueldo_bruto}")

class Cliente:
    def __init__(self, nombre, edad, telefono):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Teléfono de Contacto: {self.telefono}")

def ingresar_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    edad = int(input("Ingrese la edad del empleado: "))
    sueldo_bruto = float(input("Ingrese el sueldo bruto del empleado: "))
    return Empleado(nombre, edad, sueldo_bruto)

def ingresar_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    edad = int(input("Ingrese la edad del cliente: "))
    telefono = input("Ingrese el teléfono de contacto del cliente: ")
    return Cliente(nombre, edad, telefono)

nombre_empresa = input("hola, porfavor Ingrese el nombre de la empresa: ")
empresa = Empresa(nombre_empresa)

while True:
    opcion = input("¿Desea ingresar un empleado (E) o un cliente (C)? (E/C/fin para terminar): ").strip().lower()
    if opcion == 'e':
        empleado = ingresar_empleado()
        empresa.agregar_empleado(empleado)
    elif opcion == 'c':
        cliente = ingresar_cliente()
        empresa.agregar_cliente(cliente)
    elif opcion == 'fin':
        break
    else:
        print("Opción no válida. Por favor, ingrese 'E' para empleado, 'C' para cliente o 'fin' para terminar.")
empresa.mostrar_empleados()
empresa.mostrar_clientes()
