import sys

import config
from calculation import calculate_discount, calculate_amount_by_distance, calculate_amount_by_time
from Units import Unit
from messages import Message


def main():
    while True:
        choice = get_value(
            message=Message.STARTING_CHOICE.value,
            error_message=Message.ERROR_TYPING.value,
            validate=lambda user_input: user_input.lower() in [Unit.DISTANCE.value, Unit.TIME.value]
        ).lower()

        match choice:
            case Unit.DISTANCE.value:
                distance = get_value(
                    message=Message.DISTANCE.value,
                    error_message=Message.ERROR_NUMERIC.value,
                    validate=lambda user_input: str.isnumeric(user_input)
                )
                unit = get_value(
                    message=Message.DISTANCE_CHOICE.value,
                    error_message=Message.ERROR_TYPING.value,
                    validate=lambda user_input: user_input.lower() in [Unit.KILOMETERS.value, Unit.METERS.value]
                )
                amount = calculate_amount_by_distance(float(distance), unit)
            case Unit.TIME.value:
                time = get_value(
                    message=Message.TIME.value,
                    error_message=Message.ERROR_NUMERIC.value,
                    validate=lambda user_input: str.isnumeric(user_input)
                )
                unit = get_value(
                    message=Message.TIME_CHOICE.value,
                    error_message=Message.ERROR_TYPING.value,
                    validate=lambda user_input: user_input.lower() in [Unit.HOURS.value, Unit.MINUTES.value]
                )
                amount = calculate_amount_by_time(float(time), unit)

        discount_code = get_value(
            message=Message.CODE_CHOICE.value,
            error_message=Message.ERROR_CODE.value,
            validate=lambda user_input: not user_input or user_input in config.DISCOUNTS.keys()
        )
        amount = calculate_discount(amount, discount_code)

        print(Message.TOTAL.value.format(amount))

        again = input(Message.ENDING_CHOICE.value).strip().lower()
        if again != Unit.YES.value:
            sys.exit()


def get_value(message, error_message, validate):
    while True:
        user_input = input(message)
        if validate(user_input):
            return user_input
        else:
            print(error_message)
            continue


if __name__ == "__main__":
    main()
