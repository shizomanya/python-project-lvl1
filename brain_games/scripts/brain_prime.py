#!/usr/bin/env python3
import prompt
import random

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    print('brain-prime')
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for _ in range(3):
        num = random.randint(2, 100)
        correct_answer = "yes" if is_prime(num) else "no"
        print('Question: {}'.format(num))
        user_answer = prompt.string("Your answer: ")

        if user_answer != correct_answer:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(user_answer, correct_answer))
            print("Let's try again, {}!".format(name))
            return
        print('Correct!')

    print(f'Congratulations, {name}!')

if __name__ == '__main__':
    main()
