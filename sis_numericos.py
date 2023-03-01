numero = int (input("Digite el numero a transformar: "))
#conv, decimal a binario
binario = bin(numero)
print(f"binario: {binario}")
#Conv. decimal-hexa
hexadecimal = hex(numero)
print(f"Hexadecimal: {hexadecimal}")
#Conv. decimal-octal
octal = oct(numero)
print(f"Octal: {octal}")