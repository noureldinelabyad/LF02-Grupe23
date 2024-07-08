import config
from units import Unit
from exceptions import UnitException, DiscountException


def calculate_amount_by_distance(distance, unit):
    match unit.strip().lower():
        case Unit.KILOMETERS.value:
            return distance * config.KILOMETER_RATE
        case Unit.METERS.value:
            return distance * config.KILOMETER_RATE / 1000
        case _:
            raise UnitException


def calculate_amount_by_time(time, unit):
    match unit.strip().lower():
        case Unit.HOURS.value:
            return time * config.MINUTE_RATE * 60
        case Unit.MINUTES.value:
            return time * config.MINUTE_RATE
        case _:
            raise UnitException


def calculate_discount(amount, code):
    if not code:
        return amount
    discount_amount = config.DISCOUNTS.get(code)
    if discount_amount is None:
        raise DiscountException
    else:
        # Calculates the Amount  * ( 100% - DiscountAmount%) = Total Amount
        return amount * (1 - discount_amount)
