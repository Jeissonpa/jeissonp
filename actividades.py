#Libreria
import math

##Adquiriri informacion 
#Entradas
a = int(input("Digite el numero 1: "))
print(f"El numero a es: {a}")
b = int(input("Digite el numero 2: "))
print(f"El numero a es: {b}")
#Proceso
c = a + b
d = a - b
e = a * b
f = a / b
g = a ** b
h = math.sqrt(a)
#5 operaciones mas
i = math.sinh(a)
j = math.cosh(a)
k = math.comb(a, b)
l = math.log(a)
m = math.ceil(a)


#Salida
print(f"El resultado de la suma es : {c}")
print(f"El resultado de la resta es : {d}")
print(f"El resultado de la multiplicación es : {e}")
print(f"El resultado de la suma división : {f}")
print(f"El resultado de la potencia : {g}")
print(f"El resultado de la raiz de a es : {h}")
print(f"El resultado del la funcion seno es : {i}")
print(f"El resultado de la funcion coseno es : {j}")
print(f"El resultado combinado es : {k}")
print(f"El resultado del logaritmo es : {l}")
print(f"El resultado del redondeo es : {m}")



"""
# Funciones hiperbólicas
print(math.sinh(2))  # 3.6268604078470186
print(math.cosh(2))  # 3.7621956910836314
print(math.tanh(2))  # 0.9640275800758169

# Funciones de números aleatorios
print(math.random())  # 0.5815792928786963
print(math.randint(1, 10))  # 8

# Funciones de combinatoria y factoriales
print(math.comb(5, 2))  # 10
print(math.factorial(5))  # 120

# Funciones exponenciales y logarítmicas
print(math.exp(2))  # 7.3890560989306495
print(math.log(10))  # 2.302585092994046
print(math.log10(100))  # 2.0

# Redondeo y truncamiento
print(math.ceil(4.2))  # 5
print(math.floor(4.8))  # 4
print(math.trunc(-4.8))  # -4
print(round(4.5))  # 4 (round es una función incorporada en Python)
"""





"""
#Ejercicio
R= (4+8*2)/4-(3**2)+math.sqrt(4)
print (R)
"""