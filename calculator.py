import sys

from calculation import calculate_discount, calculate_amount_by_distance, calculate_amount_by_time
from Units import Unit
import errors


def main():
    while True:
        print("Möchtest du deine Fahrt per zurückgelegter Strecke oder Zeit berechnen?")
        choice = input().lower()

        match choice:
            case Unit.DISTANCE.value:
                distance = input("Zurückgelegte Strecke eingeben:\n")
                if not str.isnumeric(distance):
                    print("Fehler! Bitte geben Sie nur Ziffern an.\n")
                    continue
                unit = input("Kilometer oder Meter?\n").strip().lower()
                amount = calculate_amount_by_distance(float(distance), unit)
            case Unit.TIME.value:
                time = input("Gefahrene Dauer eingeben:\n")
                if not str.isnumeric(time):
                    print("Fehler! Bitte geben Sie nur Ziffern an.\n")
                    continue
                unit = input("Stunden oder Minuten?\n").strip().lower()
                amount = calculate_amount_by_time(float(time), unit)
            case _:
                print("Fehlerhafte Eingabe. Programm wird neugestaret.")
                continue

        if amount == errors.wrong_unit:
            print("Fehlerhafte Eingabe. Programm wird neugestaret.")
            continue

        discount_code = input("Rabattcode eingeben (optional):\n").strip()
        amount = calculate_discount(amount, discount_code)

        if amount == errors.wrong_discount:
            print("Fehlerhafte Eingabe. Bitte überprüfen.")
            continue

        print(f"Berechneter Betrag: {amount:.2f}€")

        again = input("Möchtest du eine neue Strecke berechnen lassen? (Ja/Nein): ").strip().lower()
        if again != "ja":
            sys.exit()


if __name__ == "__main__":
    main()
