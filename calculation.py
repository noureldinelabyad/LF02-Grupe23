import config
from Units import Unit


def calculate_amount_by_distance(distance, unit):
    match unit.lower():
        case Unit.KILOMETER.value:
            return distance * config.KILOMETER_RATE
        case Unit.METERS.value:
            return distance * config.KILOMETER_RATE / 1000
        case _:
            print("Fehlerhafte Eingabe! Bitte Kilometer oder Meter angeben.")


def calculate_amount_by_time(time, unit):
    match unit.lower():
        case Unit.HOURS.value:
            return time * config.MINUTE_RATE * 60
        case Unit.MINUTES.value:
            return time * config.MINUTE_RATE
        case _:
            print("Fehlerhafte Eingabe! Bitte Minuten oder Stunden angeben.")


def apply_discount(amount, code):
    discount_amount = config.DISCOUNTS.get(code)
    if discount_amount is None:
        print("Rabattcode Fehlerhaft!")
        return amount
    else:
        return amount * (1 - discount_amount)
