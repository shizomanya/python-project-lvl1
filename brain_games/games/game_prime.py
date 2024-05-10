#!/usr/bin/env python3
import random

CONDITIONS = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_game():
    num = random.randint(1, 100)
    if is_prime(num):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return num, correct_answer
