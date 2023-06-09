def show_menu():
    print('')
    print('[1] - Importar palabras clave')
    print('[2] - Mostrar palabras clave')
    print('[0] - Salir')

def charge_keywords():
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

def show_keywords(keywords):
    counter = 0
    for kw in keywords:
        print(kw)
        counter += 1
        if counter == 20:
            counter = 0
            input('Pulsa una tecla para continuar...')

def run():

    keywords = []
    
    while True:
        show_menu()
        option = int(input('Introduce una opcion: '))
        if option == 0:
            break
        elif option == 1:
            keywords = charge_keywords()
        elif option == 2:
            show_keywords(keywords)
        else:
            print('Opcion incorrecta')

if __name__ == '__main__':
    run()
