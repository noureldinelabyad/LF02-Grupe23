import sys

import calculation
from Units import Unit
import errors


def main():
    while True:
        print("Möchtest du deine Fahrt per zurückgelegter Strecke oder Zeit berechnen?")
        choice = input().lower()

        match choice:
            case Unit.STRECKE.value:
                distance = float(input("Zurückgelegte Strecke eingeben:\n"))
                unit = input("Kilometer oder Meter?\n").strip().lower()
                amount = calculation.calculate_amount_by_distance(distance, unit)
            case Unit.ZEIT.value:
                time = float(input("Gefahrene Dauer eingeben:\n"))
                unit = input("Stunden oder Minuten?\n").strip().lower()
                amount = calculation.calculate_amount_by_time(time, unit)
            case _:
                print("Falsche Angabe. Programm wird neugestaret.")
                continue

        if amount == errors.wrong_unit:
            print("Fehlerhafte Eingabe. Bitte überprüfen.")
            continue

        discount_code = input("Rabattcode eingeben (optional):\n").strip()
        amount = calculation.apply_discount(amount, discount_code)

        if amount == errors.wrong_discount:
            print("Fehlerhafte Eingabe. Bitte überprüfen.")
            continue

        print(f"Berechneter Betrag: {amount:.2f}€")

        again = input("Möchtest du eine neue Strecke berechnen lassen? (Ja/Nein): ").strip().lower()
        if again == "nein":
            sys.exit()


if __name__ == "__main__":
    main()
