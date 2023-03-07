import math
while True:
    print("Ingrese la operacion que desea realizar")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia")
    print("6. Raiz")
    print("7. Seno")
    print("8. Coseno")
    print("9. Numero Combinado")
    print("10. Logaritmo")
    print("11. Redondeo")
    print("12. Salir")
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        print("Ha seleccionado Suma")
        a = int(input("Digite el numero 1: "))
        print(f"El numero a es: {a}")
        b = int(input("Digite el numero 2: "))
        print(f"El numero a es: {b}")
        c = a + b
        print(f"El resultado de la suma es : {c}")

    elif opcion == 2:
        print("Ha seleccionado Resta")
        a = int(input("Digite el numero 1: "))
        print(f"El numero a es: {a}")
        b = int(input("Digite el numero 2: "))
        print(f"El numero a es: {b}")
        c = a - b
        print(f"El resultado de la resta es : {c}")

    elif opcion == 3:
        print("Ha seleccionado Multiplicacion")
        a = int(input("Digite el numero 1: "))
        print(f"El numero a es: {a}")
        b = int(input("Digite el numero 2: "))
        print(f"El numero a es: {b}")
        c = a * b
        print(f"El resultado de la Multiplicacion es : {c}")

    elif opcion == 4:
        print("Ha seleccionado Division")
        a = int(input("Digite el numero 1: "))
        print(f"El numero a es: {a}")
        b = int(input("Digite el numero 2: "))
        print(f"El numero a es: {b}")
        c = a / b 
        print(f"El resultado de la division es : {c}")

    elif opcion == 5:
        print("Ha seleccionado Potencia")
        a = int(input("Digite el numero 1: "))
        print(f"El numero a es: {a}")
        b = int(input("Digite el numero 2: "))
        print(f"El numero a es: {b}")
        c = a ** b
        print(f"El resultado de la Potencia es : {c}")

    elif opcion == 6:
        print("Ha seleccionado Raiz")
        a = int(input("Digite el numero a sacar raiz: "))
        print(f"El numero a es: {a}")
        c =  math.sqrt(a)
        print(f"El resultado de la Raiz es : {c}")

    elif opcion == 7:
        print("Ha seleccionado Seno")
        a = int(input("Digite el numero a sacar el Seno: "))
        print(f"El numero a es: {a}")
        c =  math.sinh(a)
        print(f"El Seno de {a} es : {c}")

    elif opcion == 8:
        print("Ha seleccionado Coseno")
        a = int(input("Digite el numero a sacar el coseno: "))
        print(f"El numero a es: {a}")
        #proceso
        c =  math.cosh(a)
        print(f"El Coseno de {a} es : {c}")

    elif opcion == 9:
        print("Ha seleccionado Numero Combinado")
        a = int(input("Digite el numero 1: "))
        print(f"El numero a es: {a}")
        b = int(input("Digite el numero 2: "))
        print(f"El numero a es: {b}")
        c = math.comb(a, b)
        print(f"El Numero Combinado es : {c}")

    elif opcion == 10:
        print("Ha seleccionado Logaritmo") 
        a = int(input("Digite el numero a sacar Logaritmo: "))
        print(f"El numero a es: {a}")

        c = math.log(a)
        print(f"El Logaritmo del numero {a} es : {c}") 

    elif opcion == 11:
        print("Ha seleccionado Redondeo")
        a = float(input("Digite el numero a redondear: "))
        print(f"El numero a es: {a}")
        c = math.ceil(a)
        print(f"El numero {a} redondeado es : {c}") 

    elif opcion == 12:
        print("Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
