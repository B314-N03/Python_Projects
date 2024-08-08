import random
import string
import pyperclip


def randPassw(length):
    digits = string.digits
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    special = str(['@' '!''#' '*''$' '§''&'])
    passw = ''.join(random.choice(digits + upper + lower + special) for i in range(length))
    print("Random passwort mit der Länge ", length, " ist:   ", passw)
    pyperclip.copy(passw)
    print("Es wurde in die Zwischenablage kopiert!")
    
randPassw(int(input("Welche Länge soll das Passwort haben ? : ")))