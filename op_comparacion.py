precio = 500
"""""
#o comparacion
print(precio > 500) #F
print(precio >= 500) #V
print(precio < 500) #F
print(precio <= 500) #V
print(precio == 500) #V
print(precio != 500) #F
"""""
#compuertas logicas
print("----------AND--------------")
#AND
print(False and False) #0
print(False and True) #0
print(True and False) #0
print(True and True) #1
print("------------NAND------------")
#NAND
print(not(False and False)) #1
print(not(False and True)) #1
print(not(True and False)) #1
print(not(True and True)) #0
print("------------OR------------")
#OR
print(False and False) #0
print(False and True) #0
print(True and False) #0
print(True and True) #1
print("-----------NOR-------------")
#NOR
print(not(False and False)) #1
print(not(False and True)) #0
print(not(True and False)) #0
print(not(True and True)) #0
#NOT
print("-----------NOT-------------")
print(not(False)) #1
print(not(True)) #0