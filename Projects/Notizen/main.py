import keyboard
import  os
import subprocess

# Creating an empty String that it can be accessed even out of the Function
user_input = " "
subprocess.run(['ls -I main.py | cut -f1 -d"." /home/bela/Coding/Python/Python_Projects_Kali/Notizen'])


# The main Function where the whole Program is started
def main():
    user_input = input("Welchen Befehl wollen sie ausführen? (1 = bearbeiten, 2 = erstellen, 3 = leeren, 4 = ausgeben, 5 = löschen)\n")
    if user_input == "1":
        print("Vorhandene Notizen")
        subprocess.run(['ls' , '-I main.py | cut -f1 -d"."'])
        bearbeiten(input("Welche Notiz wollen sie bearbeiten?:\n"),0)
    elif user_input == "2":
        erstellen(input("Welche Notiz wollen sie erstellen?:\n"))
    elif user_input == "3":
        leeren(input("Welche Notiz wollen sie leeren?:\n"))
    elif user_input == "4":
        ausgeben(input("Welche Notiz wollen sie ausgeben?:\n"))
    elif user_input == "5":
        loeschen(input("Welche Notiz wollen sie löschen?:\n"))
    elif user_input == "exit":
        exit()
    else:
        print("Falsche Eingabe!")
        main()


def bearbeiten(notiz,count):
    try:
        file = open(notiz + ".txt" ,"a")
        if count == 0:
            print("Was wollen sie hinzufügen?")
            inp = input()
            while inp != "quit":
                file.write(inp + "\n")
                bearbeiten(notiz,1)
            file.close()
        else:
            inp = input()
            while inp != "quit":
                file.write(inp + "\n")
                bearbeiten(notiz,1)
            file.close()
        main()
    except FileNotFoundError:
        file = open(notiz + ".txt","w")
        bearbeiten(notiz,0)
        file.close()

def erstellen(notiz):
    file = open(notiz + ".txt","w")
    file.close()
    change = input("Wollen sie diese bearbeiten?\n")
    if change == "Ja":
        bearbeiten(notiz,0)
    else:
        main()


def leeren(notiz):
    try:
        file = open(notiz + ".txt","w")
        file.flush()
        main()
    except FileNotFoundError:
        print("Diese Notiz ist nicht vorhanden!")
        main()
def loeschen(notiz):
    notiz = notiz + ".txt"
    rm = "rm" + notiz + ".txt"
    try:
        subprocess.run(rm)
    except FileNotFoundError:
        print("Die Datei ist nicht Vorhanden!")
def ausgeben(notiz):
    try:
        file = open(notiz + ".txt","r").read()
        print("Das sind ihre bisherigen Notizen in der (Ober)Notiz:" , notiz)
        print("\n"+ file)
        main()
    except FileNotFoundError:
        print("Diese Notiz ist nicht vorhanden!")
        hinzu = input("Wollen sie diese Hinzufügen?\n")
        if hinzu == "1":
            file = open(notiz, "w")
            file.close()
        else:
            main()




#main()