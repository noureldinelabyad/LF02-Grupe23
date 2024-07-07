import sys

from calculation import calculate_discount, calculate_amount_by_distance, calculate_amount_by_time
from Units import Unit
from messages import Message
import errors


def main():
    while True:
        choice = get_value(
            message=Message.STARTING_CHOICE.value,
            error_message=Message.ERROR_TYPING.value,
            validate=lambda user_input: user_input not in [Unit.DISTANCE.value, Unit.TIME.value]
        )

        match choice:
            case Unit.DISTANCE.value:
                distance = get_value(
                    message=Message.DISTANCE.value,
                    error_message=Message.ERROR_NUMERIC.value,
                    validate=lambda user_input: not str.isnumeric(user_input)
                )
                unit = get_value(
                    message=Message.DISTANCE_CHOICE.value,
                    error_message=Message.ERROR_TYPING.value,
                    validate=lambda user_input: user_input not in [Unit.KILOMETERS.value, Unit.METERS.value]
                )
                amount = calculate_amount_by_distance(float(distance), unit.strip().lower())
            case Unit.TIME.value:
                time = get_value(
                    message=Message.TIME.value,
                    error_message=Message.ERROR_NUMERIC.value,
                    validate=lambda user_input: not str.isnumeric(user_input)
                )
                unit = get_value(
                    message=Message.TIME_CHOICE.value,
                    error_message=Message.ERROR_TYPING.value,
                    validate=lambda user_input: user_input not in [Unit.HOURS.value, Unit.MINUTES.value]
                )
                amount = calculate_amount_by_time(float(time), unit)

        discount_code = input(Message.CODE_CHOICE.value).strip()
        amount = calculate_discount(amount, discount_code)

        if amount == errors.wrong_discount:
            print(Message.ERROR_TYPING.value)
            continue

        print(Message.TOTAL.value.format(amount))

        again = input(Message.ENDING_CHOICE.value).strip().lower()
        if again != Unit.YES.value:
            sys.exit()


def get_value(message, error_message, validate):
    while True:
        user_input = input(message).lower()
        if validate(user_input):
            print(error_message)
            continue
        return user_input


if __name__ == "__main__":
    main()
