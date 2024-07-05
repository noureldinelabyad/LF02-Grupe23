import sys
from calculation import calculate_discount, calculate_amount_by_distance, calculate_amount_by_time
from Units import Unit
import errors
from error_messages import error_messages

def get_valid_input(prompt, error_key, valid_func):
    while True:
        user_input = input(prompt).strip()
        if valid_func(user_input):
            return user_input
        print(error_messages[error_key])

def main():
    while True:
        choice = get_valid_input(
            "Möchtest du deine Fahrt per zurückgelegter Strecke oder Zeit berechnen?\n",
            'invalid_choice',
            lambda x: x in [Unit.STRECKE.value, Unit.ZEIT.value]
        ).lower()

        if choice == Unit.STRECKE.value:
            distance = get_valid_input(
                "Zurückgelegte Strecke eingeben (nur Ziffern):\n",
                'invalid_numeric',
                str.isnumeric
            )
            unit = get_valid_input(
                "Kilometer oder Meter?\n",
                'invalid_unit_distance',
                lambda x: x in ["kilometer", "meter"]
            )
            amount = calculate_amount_by_distance(float(distance), unit)

        elif choice == Unit.ZEIT.value:
            time = get_valid_input(
                "Gefahrene Dauer eingeben (nur Ziffern):\n",
                'invalid_numeric',
                str.isnumeric
            )
            unit = get_valid_input(
                "Stunden oder Minuten?\n",
                'invalid_unit_time',
                lambda x: x in ["stunden", "minuten"]
            )
            amount = calculate_amount_by_time(float(time), unit)

        if amount == errors.wrong_unit:
            print(error_messages['wrong_unit'])
            continue

        while True:
            discount_code = input("Rabattcode eingeben (optional):\n").strip()
            amount_with_discount = calculate_discount(amount, discount_code)
            if amount_with_discount == errors.wrong_discount:
                print(error_messages['wrong_discount'])
            else:
                amount = amount_with_discount
                break

        print(f"Berechneter Betrag: {amount:.2f}€")

        while True:
            again = get_valid_input(
                "Möchtest du eine neue Strecke berechnen lassen? (Ja/Nein): ",
                'wrong_answer',
                lambda x: x.lower() in ["ja", "nein"]
            ).lower()

            if again == "nein":
                sys.exit()
            else:
             break

if __name__ == "__main__":
    main()
