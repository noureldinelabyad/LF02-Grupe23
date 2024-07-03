import config
from Units import Unit


def calculate_amount_by_distance(distance, unit):
    if unit.lower() == Unit.KILOMETER.value:
        amount = distance * config.KILOMETER_RATE
    else:
        amount = distance * config.KILOMETER_RATE / 1000
    return amount


def calculate_amount_by_time(time, unit):
    if unit.lower() == Unit.HOURS.value:
        amount = time * config.MINUTE_RATE * 60
    else:
        amount = time * config.MINUTE_RATE
    return amount


def apply_discount(amount, code):
    return amount * (1 - config.DISCOUNTS.get(code, 0))
