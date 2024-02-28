import time
a = 0
b = 0
seguir = True
while seguir == True:
    print("Hola \n¿Con cuales dos numeros quieres operar?")
    a = int(input("Introduce el primer numero: "))
    b = int(input("Introduce el segundo numero: "))
    print("¿Que operacion quieres hacer? \n1.Sumar \n2.Restar \n3.Multiplicar \n4.Dividir")
    accion = int(input("Introduce el numero de la accion que quieres hacer: "))
    if accion == 1:
        resultado = a + b
        print("Este es el resultado de la operacion: " + str(resultado))
        time.sleep(1)
        print("Quieres realizar alguna operacion mas? \n1.Si \n2.No")
        pregunta = int(input("Introduce el numero de la accion que quieres hacer: "))
        if pregunta == 1:
            seguir = True
        else:
            seguir = False
    elif accion == 2:
        resultado = a - b
        print("Este es el resultado de la operacion: " + str(resultado))
        time.sleep(1)
        print("Quieres realizar alguna operacion mas? \n1.Si \n2.No")
        pregunta = int(input("Introduce el numero de la accion que quieres hacer: "))
        if pregunta == 1:
            seguir = True
        else:
            seguir = False
    elif accion == 3:
        resultado = a*b
        print("Este es el resultado de la operacion: " + str(resultado))
        time.sleep(1)
        print("Quieres realizar alguna operacion mas? \n1.Si \n2.No")
        pregunta = int(input("Introduce el numero de la accion que quieres hacer: "))
        if pregunta == 1:
            seguir = True
        else:
            seguir = False
    elif accion == 4:
        resultado = a/b
        print("Este es el resultado de la operacion: " + str(resultado))
        time.sleep(1)
        print("Quieres realizar alguna operacion mas? \n1.Si \n2.No")
        pregunta = int(input("Introduce el numero de la accion que quieres hacer: "))
        if pregunta == 1:
            seguir = True
        else:
            seguir = False
    else:
        print("Porfavor introduce el numero de una de las operaciones que aparecen")