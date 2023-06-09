word = str(input("Ingrese una palabra: "))

is_palindrome = True
start = 0
end = len(word) - 1

while start < end:
    if word[start] != word[end]:
        is_palindrome = False
        break
    start += 1
    end -= 1

if is_palindrome:
    print(f"{word} es un palindromo")
else:
    print(f"{word} no es un palindromo")
