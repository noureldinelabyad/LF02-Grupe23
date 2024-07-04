import config
from Units import Unit
import errors


def calculate_amount_by_distance(distance, unit):
    match unit.lower():
        case Unit.KILOMETER.value:
            return distance * config.KILOMETER_RATE
        case Unit.METERS.value:
            return distance * config.KILOMETER_RATE / 1000
        case _:
            return errors.wrong_unit


def calculate_amount_by_time(time, unit):
    match unit.lower():
        case Unit.HOURS.value:
            return time * config.MINUTE_RATE * 60
        case Unit.MINUTES.value:
            return time * config.MINUTE_RATE
        case _:
            return errors.wrong_unit


def calculate_discount(amount, code):
    if not code:
        return amount
    discount_amount = config.DISCOUNTS.get(code)
    if discount_amount is None:
        return errors.wrong_discount
    else: # Calculates the discount with the price
        return amount * (1 - discount_amount)
