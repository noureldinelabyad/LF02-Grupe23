from enum import Enum


class Message(Enum):
    STARTING_CHOICE = "Möchtest du deine Fahrt per zurückgelegter Strecke oder Zeit berechnen?\n"
    DISTANCE = "Zurückgelegte Strecke eingeben:\n"
    DISTANCE_CHOICE = "Kilometer oder Meter?\n"
    TIME = "Gefahrene Dauer eingeben:\n"
    TIME_CHOICE = "Stunden oder Minuten?\n"
    CODE_CHOICE = "Rabattcode eingeben (optional):\n"
    TOTAL = "Berechneter Betrag: {:.2f}€"
    ENDING_CHOICE = "Möchtest du eine neue Strecke berechnen lassen? (Ja/Nein): "
    ERROR_NUMERIC = "Fehler! Bitte geben Sie nur Ziffern an.\n"
    ERROR_TYPING = "Fehlerhafte Eingabe. Bitte überprüfen."
    ERROR_CODE = "Fehlerhafte Eingabe. Bitte den Code überprüfen."

