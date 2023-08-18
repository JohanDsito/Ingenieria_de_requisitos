#Boleto de tren
#Valery Rosero y Johan Delgado
#15/08/2023

import msvcrt

key = input("Presione 'w' para continuar: ")
while key != 'w':
    key = msvcrt.getwch()
input("Bienvenido a la estación Antioquia.")

input("            Menú\n Por favor, seleccione su destino (ingrese el número de su destino).\n 1. LA ESTRELLA.\n 2. CARACOL.\n 3. EL LIMÓN.\n 4. LA SIERRA.\n 5. ESTACIÓN GRECIA.\n 6. SAN JOSÉ DEL NUS.\n 7. CISNEROS.\n 8. PUERTO NARE.\n 9. CICLORRUTA DE SURAMÉRICA.")

destino = int(input("Ingrese su destino: "))

if destino == 1:
    tarjetaCredito = int(input("Ingrese aquí su tarjeta de crédito: "))
    if int(tarjetaCredito) < 19:
        print("Error, tiene más de 19 carácteres.")
    else:
        clave = int(input("Introduzca su clave: "))
        documento = int(input("Para finalizar, ingrese su número de identificación: "))
        print("Boleto de tren\n Destino: La estrella.\n ID 23449.\n Disfrute su viaje.")
if destino == 2:
    tarjetaCredito = int(input("Ingrese aquí su tarjeta de crédito: "))
    if int(tarjetaCredito) < 19:
        print("Error, tiene más de 19 carácteres.")
    else:
        clave = int(input("Introduzca su clave: "))
        documento = int(input("Para finalizar, ingrese su número de identificación: "))
        print("Boleto de tren\n Destino: Caracol.\n ID 23239.\n Disfrute su viaje.")
if destino == 3:
    tarjetaCredito = int(input("Ingrese aquí su tarjeta de crédito: "))
    if int(tarjetaCredito) < 19:
        print("Error, tiene más de 19 carácteres.")
    else:
        clave = int(input("Introduzca su clave: "))
        documento = int(input("Para finalizar, ingrese su número de identificación: "))
        print("Boleto de tren\n Destino: El Limón.\n ID 12239.\n Disfrute su viaje.")
if destino == 4:
    tarjetaCredito = int(input("Ingrese aquí su tarjeta de crédito: "))
    if int(tarjetaCredito) < 19:
        print("Error, tiene más de 19 carácteres.")
    else:
        clave = int(input("Introduzca su clave: "))
        documento = int(input("Para finalizar, ingrese su número de identificación: "))
        print("Boleto de tren\n Destino: La cierra.\n ID 23539.\n Disfrute su viaje.")       
if destino == 5:
    tarjetaCredito = int(input("Ingrese aquí su tarjeta de crédito: "))
    if int(tarjetaCredito) < 19:
        print("Error, tiene más de 19 carácteres.")
    else:
        clave = int(input("Introduzca su clave: "))
        documento = int(input("Para finalizar, ingrese su número de identificación: "))
        print("Boleto de tren\n Destino: Caracol.\n ID 23207.\n Disfrute su viaje.")
if destino == 6:
    tarjetaCredito = int(input("Ingrese aquí su tarjeta de crédito: "))
    if int(tarjetaCredito) < 19:
        print("Error, tiene más de 19 carácteres.")
    else:
        clave = int(input("Introduzca su clave: "))
        documento = int(input("Para finalizar, ingrese su número de identificación: "))
        print("Boleto de tren\n Destino: Estación Grecia.\n ID 28939.\n Disfrute su viaje.")
if destino == 7:
    tarjetaCredito = int(input("Ingrese aquí su tarjeta de crédito: "))
    if int(tarjetaCredito) < 19:
        print("Error, tiene más de 19 carácteres.")
    else:
        clave = int(input("Introduzca su clave: "))
        documento = int(input("Para finalizar, ingrese su número de identificación: "))
        print("Boleto de tren\n Destino: San José del Nus.\n ID 23109.\n Disfrute su viaje.")
if destino == 8:
    tarjetaCredito = int(input("Ingrese aquí su tarjeta de crédito: "))
    if int(tarjetaCredito) < 19:
        print("Error, tiene más de 19 carácteres.")
    else:
        clave = int(input("Introduzca su clave: "))
        documento = int(input("Para finalizar, ingrese su número de identificación: "))
        print("Boleto de tren\n Destino: Cisneros.\n ID 27389.\n Disfrute su viaje.")
if destino == 9:
    tarjetaCredito = int(input("Ingrese aquí su tarjeta de crédito: "))
    if int(tarjetaCredito) < 19:
        print("Error, tiene más de 19 carácteres.")
    else:
        clave = int(input("Introduzca su clave: "))
        documento = int(input("Para finalizar, ingrese su número de identificación: "))
        print("Boleto de tren\n Destino: Puerto Nare.\n ID 75439.\n Disfrute su viaje.")
