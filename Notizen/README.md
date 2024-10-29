
# Notizen-Manager

Dieses Python-Skript ist ein Notizen-Manager, der unter Windows und Unix-Systemen (über WSL) funktioniert. Es ermöglicht es, Notizen zu erstellen, anzuzeigen, zu bearbeiten, zu leeren und zu löschen. Die Benutzeroberfläche unterstützt eine Menüauswahl mit Tastatur und eine einfache Navigation.

## Funktionen

- **Notiz erstellen**: Erstellt eine neue leere Notiz.
- **Notiz bearbeiten**: Ermöglicht das Hinzufügen von Text zu einer bestehenden Notiz.
- **Notiz leeren**: Löscht den Inhalt einer Notiz.
- **Notiz anzeigen**: Zeigt den Inhalt einer Notiz an.
- **Notiz löschen**: Entfernt eine Notiz-Datei.
- **Menü- und Navigation**: Auswahl der Optionen im Menü mit den Pfeiltasten und Enter zur Bestätigung.

## Voraussetzungen

- **Python 3** muss installiert sein.
- Unter Windows wird **WSL (Windows Subsystem for Linux)** benötigt, um das Skript auszuführen.

## Installation

1. Klone dieses Repository:
   ```bash
   git clone https://github.com/B314-N03/Python_Projects/
   ```
2. Wechsle in das Verzeichnis:
   ```bash
   cd Python_Projects/Notizen
   ```

## Nutzung

Führe das Skript mit folgendem Befehl aus:
```bash
python main.py
```

Das Menü wird angezeigt und ermöglicht die Auswahl der Befehle, um mit den Notizen zu arbeiten. Verwende die Pfeiltasten, um durch die Optionen zu navigieren, und drücke **Enter**, um eine Option auszuwählen.

### Menüoptionen:

1. **Notiz bearbeiten**: Zeigt eine Liste der Notizen an und ermöglicht das Bearbeiten einer ausgewählten Notiz.
2. **Notiz erstellen**: Erstellt eine neue Notiz und bietet die Möglichkeit, sie direkt zu bearbeiten.
3. **Notiz leeren**: Löscht den Inhalt einer ausgewählten Notiz.
4. **Notiz anzeigen**: Zeigt den Inhalt einer ausgewählten Notiz an.
5. **Notiz löschen**: Entfernt die ausgewählte Notiz vollständig.
6. **Exit**: Beendet das Programm.

## Besonderheiten für Unix und Windows

### Unix (WSL)
Das Skript unterstützt Tab-Vervollständigung und terminalbasierte Tasteneingaben.

### Windows
Einige Funktionen, wie die Cursor-Ausblendung und die Nutzung von WSL, sind speziell für die Windows-Umgebung implementiert.

## Fehlerbehebung

Falls das Skript nicht ausgeführt wird:
- Stelle sicher, dass Python 3 installiert ist.
- Für Windows-Benutzer: Stelle sicher, dass **WSL aktiviert** und eingerichtet ist.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Siehe die [LICENSE](LICENSE)-Datei für weitere Details.
