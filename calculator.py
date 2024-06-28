def calculate_amount_by_distance(distance, unit):
    if unit == "km":
        amount = distance * 0.5  # example rate per km
    else:
        amount = distance * 0.0005  # example rate per meter
    return amount

def calculate_amount_by_time(time, unit):
    if unit == "hours":
        amount = time * 20  # example rate per hour
    else:
        amount = time * 0.3333  # example rate per minute
    return amount

def apply_discount(amount, code):
    discounts = {"Tec5": 0.05, "Tec15": 0.15, "TecFirstTry": 0.50}
    return amount * (1 - discounts.get(code, 0))

def main():
    while True:
        print("Choose calculation type: 1) Distance 2) Time")
        choice = input()

        if choice == '1':
            distance = float(input("Enter distance: "))
            unit = input("Enter unit (km/meters): ").strip().lower()
            amount = calculate_amount_by_distance(distance, unit)
        elif choice == '2':
            time = float(input("Enter time: "))
            unit = input("Enter unit (hours/minutes): ").strip().lower()
            amount = calculate_amount_by_time(time, unit)
        else:
            print("Invalid choice. Exiting.")
            break

        discount_code = input("Enter discount code (optional): ").strip()
        amount = apply_discount(amount, discount_code)

        print(f"Calculated amount: {amount:.2f}")

        again = input("Do you want to calculate again? (yes/no): ").strip().lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    main()
