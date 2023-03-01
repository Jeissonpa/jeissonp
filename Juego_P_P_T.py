#Importal libreria
import random
#opciones
op = ("Piedra", "Papel","Tijera")
#Entradas
usuario = input("Digite la opcion Piedra, Papel o Tijera: ")
cpu = random.choice(op)

#Imprimir informacion
print(f"La opcion que digito el usuario es: {usuario}")
print(f"La opcion de CPU es: {cpu}")

#Proceso
if usuario == "Piedra" and cpu == "Piedra":
    print("Empate")
elif usuario == "Tijera" and cpu == "Tijera":
    print("Empate")
elif usuario == "Papel" and cpu == "Papel":
    print("Empate")
elif usuario == "Piedra" and cpu == "Papel":
    print("Gana CPU!!")
elif usuario == "Piedra" and cpu == "Tijera":
    print("Gana usuario!!")
elif usuario == "Papel" and cpu == "Piedra":
    print("Gana usuario!!")
elif usuario == "Papel" and cpu == "Tijera":
    print("Gana CPU!!")
elif usuario == "Tijera" and cpu == "Piedra":
    print("Gana CPU!!")
elif usuario == "Tijera" and cpu == "Papel":
    print("Gana usuario!!")
else:
    print("error")