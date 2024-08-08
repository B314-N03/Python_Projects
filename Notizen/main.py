import os
import sys
import subprocess

# Function to hide cursor
def hide_cursor():
    if os.name != 'nt':  # Not Windows
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

# Function to show cursor
def show_cursor():
    if os.name != 'nt':  # Not Windows
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

# Function to run WSL script
def run_wsl_script():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    wsl_path = script_directory.replace('C:', '/mnt/c').replace('\\', '/')
    subprocess.run(['wsl', '-u', 'root', 'python3', wsl_path + '/main.py'])
    sys.exit()

# Fallback to WSL
if os.name == 'nt':
    run_wsl_script()

else:
    import readline
    import glob
    import termios
    import tty

    # Tab completion for Unix systems
    def completer(text, state):
        files = glob.glob(text + '*')
        return files[state] if state < len(files) else None

    readline.set_completer(completer)
    readline.parse_and_bind("tab: complete")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_key():
    if os.name == 'nt':  # Windows
        import msvcrt
        return msvcrt.getch().decode('utf-8')
    else:  # Unix (Linux/MacOS) in WSL
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def display_menu(options, current_selection):
    hide_cursor()  # Hide cursor while displaying the menu
    clear_screen()
    print("Welchen Befehl wollen Sie ausführen?")
    for i, option in enumerate(options):
        if i == current_selection:
            print(f"[X] {option}")
        else:
            print(f"[ ] {option}")

def display_edit_overlay():
    print("\nTipps:")
    print("  - Geben Sie 'quit' ein, um das Hinzufügen zu beenden und zu speichern.")
    print("  - Um das Programm zu beenden, geben Sie 'exit' ein.\n")

def befehl_auswahl():
    options = [
        "Notiz bearbeiten",  # 1
        "Notiz erstellen",   # 2
        "Notiz leeren",      # 3
        "Notiz ausgeben",    # 4
        "Notiz löschen",     # 5
        "Exit"               # 6
    ]
    current_selection = 0

    while True:
        display_menu(options, current_selection)
        key = get_key()

        if key == '\x1b':  # ESC sequence for Unix (Linux/MacOS)
            key = get_key()
            if key == '[':
                key = get_key()
                if key == 'A':  # Up arrow
                    current_selection = (current_selection - 1) % len(options)
                elif key == 'B':  # Down arrow
                    current_selection = (current_selection + 1) % len(options)
        elif key in ('H', 'P'):  # Up (H) and Down (P) for Windows
            if key == 'H':  # Up arrow
                current_selection = (current_selection - 1) % len(options)
            elif key == 'P':  # Down arrow
                current_selection = (current_selection + 1) % len(options)
        elif key == '\r':  # Enter key
            clear_screen()
            show_cursor()  # Show cursor after menu selection
            if options[current_selection] == "Exit":
                print("Programm beendet.")
                sys.exit()
            return current_selection + 1  # Rückgabe der ausgewählten Option (1-basiert)

def run_ls():
    result = [f[:-4] for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.txt') and f != 'main.py']
    if result:
        for note in result:
            print(note)
    else:
        print("Keine Notizen gefunden.")

def main():
    while True:
        befehl = befehl_auswahl()

        if befehl == 1:
            run_ls()
            bearbeiten(input_with_completion("Welche Notiz wollen Sie bearbeiten?:\n"), 0)
        elif befehl == 2:
            notiz_name = input("Wie soll die Notiz heißen?:\n")
            erstellen(notiz_name)
        elif befehl == 3:
            run_ls()  
            leeren(input_with_completion("Welche Notiz wollen Sie leeren?:\n"))
        elif befehl == 4:
            run_ls()  
            ausgeben(input_with_completion("Welche Notiz wollen Sie ausgeben?:\n"))
        elif befehl == 5:
            run_ls() 
            loeschen(input_with_completion("Welche Notiz wollen Sie löschen?:\n"))
        elif befehl == 6:
            print("Programm beendet.")
            break
        else:
            print("Falsche Eingabe!")

def input_with_completion(prompt):
    if os.name == 'nt':  # Windows
        print(prompt, end='')
        return input().strip()
    else:  # Unix (Linux/MacOS) in WSL
        return input(prompt).strip()

def bearbeiten(notiz, count):
    try:
        with open(notiz + ".txt", "a") as file:
            if count == 0:
                print("Was wollen Sie hinzufügen?")
                display_edit_overlay()
                inp = input()
                while inp != "quit":
                    if inp.lower() == 'exit':
                        print("Programm beendet.")
                        sys.exit()
                    file.write(inp + "\n")
                    inp = input()
            else:
                inp = input()
                while inp != "quit":
                    if inp.lower() == 'exit':
                        print("Programm beendet.")
                        sys.exit()
                    file.write(inp + "\n")
    except FileNotFoundError:
        with open(notiz + ".txt", "w") as file:
            bearbeiten(notiz, 0)

def erstellen(notiz):
    with open(notiz + ".txt", "w") as file:
        pass
    change = input("Wollen Sie diese bearbeiten? [y/n]:\n")
    if change.lower() == "y":
        bearbeiten(notiz, 0)

def leeren(notiz):
    try:
        with open(notiz + ".txt", "w") as file:
            file.flush()
    except FileNotFoundError:
        print("Diese Notiz ist nicht vorhanden!")

def loeschen(notiz):
    notiz = notiz + ".txt"
    try:
        os.remove(notiz)
    except FileNotFoundError:
        print("Die Datei ist nicht vorhanden!")

def ausgeben(notiz):
    try:
        with open(notiz + ".txt", "r") as file:
            content = file.read()
        print("Das sind Ihre bisherigen Notizen in der (Ober)Notiz:", notiz)
        print("\n" + content)
    except FileNotFoundError:
        print("Diese Notiz ist nicht vorhanden!")
        hinzu = input("Wollen Sie diese hinzufügen? [y/n]:\n")
        if hinzu.lower() == "y":
            with open(notiz + ".txt", "w") as file:
                pass

if __name__ == "__main__":
    main()
