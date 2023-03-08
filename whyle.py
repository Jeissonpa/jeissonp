#variable 
contador = 0
#estructura
"""
while contador <=4:
    print(f"contador = {contador}")
    contador += 1
print("Salio de while")

contador = 0
#ejemplo
while contador < 20:
    contador += 1
    if contador <15:
        continue
    print(contador)
"""
texto = "Estoy en clase de algoritmos en unisangil"
#buscar
print("clases" in texto  )
print(texto.title())#Titulo
print(texto.upper())#Mayusculas
print(texto.lower())#Minusculas
print(texto.count('a'))#Cuenta cuantas letra hay en el texto
#break y continue