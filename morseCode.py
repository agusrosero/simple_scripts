morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

def interface():
    print("1. Traducir texto a morse.")
    print("2. Traducir codigo morse a texto.")
    print("3. Salir.")

def text_to_morse(text):
    morse = ""
    for char in text:
        if char.upper() in morse_code:
            morse += morse_code[char.upper()] + " "
    return morse

def morse_to_text(morse):
    text = ""
    inverse_morse = {v: k for k, v in morse_code.items()}
    codes = morse.split(" ")
    for code in codes:
        if code in inverse_morse:
            text += inverse_morse[code]
    return text

def main():
    while True:
        interface()
        choice = input("Ingrese una opcion: ")

        if choice == "1":
            text = input("Ingresa el texto a traducir: ")
            morse = text_to_morse(text)
            print("Texto en codigo morese: ", morse)
        elif choice == "2":
            morse = input("Ingrese el codigo morse a traducir: ")
            text = morse_to_text(morse)
            print("Codigo morse traducido: ", text)
        elif choice == "3":
            break
        else:
            print("Error. Opcion invalida.")


if __name__ == "__main__":
    main()