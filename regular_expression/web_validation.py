import re

url_regex = r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'

def validar_web(url):
    if re.match(url_regex, url):
        print("Url valida.")
    else:
        print("La Url no es valida.")

validar_web("https://www.google.com")
