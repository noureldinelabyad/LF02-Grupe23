import calculation


def main():
    while True:
        print("Möchtest du per Distanz oder Zeit berechnen?")
        choice = input().lower()

        if choice == 'distanz':
            distance = float(input("Zurückgelegte Distanz eingeben:\n"))
            unit = input("Kilometer oder Meter?\n").strip().lower()
            amount = calculation.calculate_amount_by_distance(distance, unit)
        elif choice == 'zeit':
            time = float(input("Gefahrene Dauer eingeben:\n"))
            unit = input("Stunden oder Minuten?\n").strip().lower()
            amount = calculation.calculate_amount_by_time(time, unit)
        else:
            print("Falsche Angabe. Programm wird beendet.")
            break

        discount_code = input("Rabattcode eingeben (optional):\n").strip()
        amount = calculation.apply_discount(amount, discount_code)

        print(f"Berechneter Betrag: {amount:.2f}€")

        again = input("Möchtest du eine neue Strecke berechnen lassen? (Ja/Nein): ").strip().lower()
        if again == "nein":
            break


if __name__ == "__main__":
    main()
