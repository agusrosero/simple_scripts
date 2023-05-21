import random

letras = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
simbolos = "!@#$%^&*()_+-="

todo_junto = letras + numeros + simbolos

# Genera una contraseña de una cierta cantidad de caracteres de largo.
largo = int(input("Ingrese la cantidad de caracteres de la contraseña: "))
password = "".join(random.sample(todo_junto, largo))
print(f"Password generado: {password}")
