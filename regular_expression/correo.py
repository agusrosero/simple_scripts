import re

email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

def validacion(correo):
    if re.match(email, correo):
        print("El correo es valido.")
    else:
        print("El correo es invalido.")
     

validacion("test@mail.com")
