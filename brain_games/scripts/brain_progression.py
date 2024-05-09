#!/usr/bin/env python3
from random import randint
import prompt


def generate_progression():
    start = randint(1, 50)
    step = randint(1, 10)
    progression = [str(start + step * i) for i in range(10)]
    hidden_index = randint(0, 9)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    return progression, str(correct_answer)


def main():
    print('brain-progression')
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("What number is missing in the progression?")

    for _ in range(3):
        progression, correct_answer = generate_progression()
        print("Question:", ' '.join(progression))
        user_answer = prompt.string("Your answer: ")

        if user_answer != correct_answer:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(user_answer, correct_answer))
            print("Let's try again, {}!".format(name))
            return
        print('Correct!')

    print(f"Congratulations, {name}!")


if __name__ == 'main':
    main()
