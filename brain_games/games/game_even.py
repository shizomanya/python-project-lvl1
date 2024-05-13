import random

CONDITIONS = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_game():
    number = random.randint(1, 100)
    return number, 'yes' if is_even(number) else 'no'
