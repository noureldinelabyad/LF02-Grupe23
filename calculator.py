import sys

from calculation import calculate_discount, calculate_amount_by_distance, calculate_amount_by_time
from Units import Unit
from messages import Message
import errors


def main():
    while True:
        print(Message.STARTING_CHOICE.value)
        choice = input().lower()

        match choice:
            case Unit.DISTANCE.value:
                distance = input(Message.DISTANCE.value)
                if not str.isnumeric(distance):
                    print(Message.ERROR_NUMERIC.value)
                    continue
                unit = input(Message.DISTANCE_CHOICE.value).strip().lower()
                amount = calculate_amount_by_distance(float(distance), unit)
            case Unit.TIME.value:
                time = input(Message.TIME.value)
                if not str.isnumeric(time):
                    print(Message.ERROR_NUMERIC.value)
                    continue
                unit = input(Message.TIME_CHOICE.value).strip().lower()
                amount = calculate_amount_by_time(float(time), unit)
            case _:
                print(Message.ERROR_TYPING.value)
                continue

        if amount == errors.wrong_unit:
            print(Message.ERROR_TYPING.value)
            continue

        discount_code = input(Message.CODE_CHOICE.value).strip()
        amount = calculate_discount(amount, discount_code)

        if amount == errors.wrong_discount:
            print(Message.ERROR_TYPING.value)
            continue

        print(Message.TOTAL.value.format(amount))

        again = input(Message.ENDING_CHOICE.value).strip().lower()
        if again != Unit.YES.value:
            sys.exit()


if __name__ == "__main__":
    main()
