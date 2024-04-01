#!/usr/bin/env python

import random
import prompt

def is_even(number):
    return number % 2 == 0

def get_question():
    number = random.randint(1, 100)
    return number, 'yes' if is_even(number) else 'no'

def main():
    print('brain-even')
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number, correct_answer = get_question()
        print('Question: {}'.format(number))
        user_answer = input('Your answer: ')
        if user_answer != correct_answer:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(user_answer, correct_answer))
            print("Let's try again, {}!".format(name))
            return
        print('Correct!')
    print(f"Congratulations, {name}!")

if __name__ == '__main__':
    main()
    
