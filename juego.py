#utilizar continue y break generar un contador de rondas y adicional a ello que halla un ganador al que cualquier jugador 
#llege a 3 puntos y este diga el ganador
import random
max_intentos = 3
intentos = 0
 #opciones
op = ("Piedra", "Papel","Tijera")
while intentos < max_intentos:
    print("Ejecutando ronda", intentos+1)
    intentos += 1
 
#estructura while

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
    