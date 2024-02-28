import math
import time
a = 0
b = 0
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def producto(a,b):
    return a*b
def division(a,b):
    if b !=0:
        return a/b
    else:
        print("Porfavor introduce un valor valido para b que no sea 0")
def potencia(a,b):
    return a**b
def raiz_cuadrada(a):
    return math.sqrt(a)
def seno(a):
    return math.sin(a)
def coseno(a):
    return math.cos(a)
def tangente(a):
    return math.tan(a)
def arseno(a):
    return math.asin(a)
def arcoseno(a):
    return math.acos(a)
def arctangente(a):
    return math.atan(a)
def factorial(a):
    return math.factorial(a)

def calculadora():
    print("Calculadora cientifica: \nEscoge una de las siguientes opciones:")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicación")
    print("4.Division")
    print("5.Potencia")
    print("6.Raiz Cuadrada")
    print("7.Seno")
    print("8.Coseno")
    print("9.Tangente")
    print("10.Arcseno")
    print("11.Arccoseno")
    print("12.Arctangente")
    print("13.Factorial")
    print("14.Salir")

    while True:
        opcion = input("Introduce una opcion del (1-13): ")
        if opcion in ['1', '2', '3', '4', '5']:
            num1 = int(input("Ingrese el primero número: "))
            num2 = int(input("Ingrese el segundo número: "))
        elif opcion in ['6', '7', '8', '9', '10', '11', '12', '13']:
            num1 = int(input("Ingrese el número: "))
        
        if opcion == '1':
            print("Resultado:", suma(num1, num2))
        elif opcion == '2':
            print("Resultado:", resta(num1, num2))
        elif opcion == '3':
            print("Resultado:", producto(num1, num2))
        elif opcion == '4':
            print("Resultado:", division(num1, num2))
        elif opcion == '5':
            print("Resultado:", potencia(num1, num2))
        elif opcion == '6':
            print("Resultado:", raiz_cuadrada(num1))
        elif opcion == '7':
            print("Resultado:", seno(num1))
        elif opcion == '8':
            print("Resultado:", coseno(num1))
        elif opcion == '9':
            print("Resultado:", tangente(num1))
        elif opcion == '10':
            print("Resultado:", arseno(num1))
        elif opcion == '11':
            print("Resultado:", arcoseno(num1))
        elif opcion == '12':
            print("Resultado:", arctangente(num1))
        elif opcion == '13':
            print("Resultado:", factorial(num1))
        elif opcion == '14':
            break
        else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

calculadora()
