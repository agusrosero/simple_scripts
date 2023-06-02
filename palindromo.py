palabra = str(input("Ingrese una palabra: "))

es_palindromo = True
inico = 0
fin = len(palabra) - 1

while inico < fin:
    if palabra[inico] != palabra[fin]:
        es_palindromo = False
        break
    inico += 1
    fin -= 1

if es_palindromo:
    print(f"{palabra} es un palindromo")
else:
    print(f"{palabra} no es un palindromo")
