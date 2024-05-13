import random

CONDITIONS = 'Find the greatest common divisor of given numbers.'


def gcd(num1, num2):
    while num2 > 0:
        num1, num2 = num2, num1 % num2
    return num1


def get_game():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = str(gcd(num1, num2))
    return question, correct_answer
