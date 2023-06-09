import re

email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

def validation(mail):
    if re.match(email, mail):
        print("El correo es valido.")
    else:
        print("El correo es invalido.")
     

validation("test@mail.com")
