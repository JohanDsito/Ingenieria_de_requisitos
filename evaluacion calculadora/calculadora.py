# Elaborado por Johan Delgado 

print("*************")
print("CALCULADORA")
print("*************")

class Calculadora:
    def __init__(self):
        self.valor1 = int(input("Ingrese el primer valor con el que desea calcular: "))
        self.valor2 = int(input("Ingrese el segundo valor con el que desaea calcular: "))

    def suma(self):
        return self.valor1 + self.valor2

    def resta(self):
        return self.valor1 - self.valor2

    def multiplicacion(self):
        return self.valor1 * self.valor2

    def division(self):
        if self.valor2 == 0:
            return "como se te ocurre dividir por 0 xd?"
        else:
            return self.valor1 / self.valor2

calculadora2 = Calculadora()
print("-------------")
print("SUMA")
print(calculadora2.suma())
print("-------------")
print("RESTA")
print(calculadora2.resta())
print("-------------")
print("MULTIPLICACION")
print(calculadora2.multiplicacion())
print("-------------")
print("DIVISION")
print(calculadora2.division())
print("-------------")

print("*******************")
print("FIN DEL CALCULO :P")
print("*******************")
