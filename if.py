precio = 501
#Estructura IF
if precio >= 500:
    print("Esta muy caro!!!")
#Estructura IF -ELSE
if precio >= 500:
    print("Esta muy caro!!!")
else:
    print("Lo compro!!!")
#Estructura IF - ANIDADAS
if precio <= 500:
    print("Esta muy caro!!!")
elif precio == 501:
    print(precio + 100)
else:
    print("Lo compro!!!")

#Ejemplo IF
numero = int(input("Digite un numeto del 1 al 5: "))
#Estructura IF - ANIDADAS
if numero == 1:
    print(f"El numero que digito es el uno")
elif numero == 2:
    print(f"El numero que digito es el dos")
elif numero == 3:
    print(f"El numero que digito es el tres")
elif numero == 4:
    print(f"El numero que digito es el cuatro")
elif numero == 5:
    print(f"El numero que digito es el cinco")
else:
    print("Error!!!")