#!/usr/bin/env python3
import random

CONDITIONS = 'What is the result of the expression?'


def get_game():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])

    question = f"{num1} {operation} {num2}"
    correct_answer = str(eval(question))

    return question, correct_answer
