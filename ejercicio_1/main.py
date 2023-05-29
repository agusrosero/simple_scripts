def muestra_menu():
    print('')
    print('[1] - Importar palabras clave')
    print('[2] - Mostrar palabras clave')
    print('[0] - Salir')

def carga_keywords():
    keywords = []
    try:
        # lea un fichero llamado keywords.txt
        with open('/media/agusdev/d037ce5d-76ba-4a6a-b255-e0bbf02cc6ab/home/agus-dev/Documentos/SmallProjects/ejercicio_1/keywords.txt', 'r') as f:
            for kw in f:
                kw = kw.replace('\n', '')
                keywords.append(kw)
    except FileNotFoundError:
        print('No se ha encontrado el fichero keywords.txt')
    return keywords

def mostrar_keywords(keywords):
    contador = 0
    for kw in keywords:
        print(kw)
        contador += 1
        if contador == 20:
            contador = 0
            input('Pulsa una tecla para continuar...')

def run():

    keywords = []
    
    while True:
        muestra_menu()
        opcion = int(input('Introduce una opcion: '))
        if opcion == 0:
            break
        elif opcion == 1:
            keywords = carga_keywords()
        elif opcion == 2:
            mostrar_keywords(keywords)
        else:
            print('Opcion incorrecta')

if __name__ == '__main__':
    run()