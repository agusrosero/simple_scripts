import random

letter = "abcdefghijklmnopqrstuvwxyz"
number = "0123456789"
symbols = "!@#$%^&*()_+-="

all_together = letter + number + symbols

# Genera una contraseña de una cierta cantidad de caracteres de largo.
long = int(input("Ingrese la cantidad de caracteres de la contraseña: "))
password = "".join(random.sample(all_together, long))
print(f"Password generado: {password}")

