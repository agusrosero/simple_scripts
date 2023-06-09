import re

url_regex = r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'

def validate_web(url):
    if re.match(url_regex, url):
        print("Url valida.")
    else:
        print("La Url no es valida.")

validate_web("https://www.google.com")
