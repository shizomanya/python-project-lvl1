#!/usr/bin/env python3
import random
import prompt


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    print('brain-gcd')
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')

    for _ in range(3):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        correct_answer = gcd(num1, num2)
        print(f'Question: {num1} {num2}')
        user_answer = int(prompt.string('Your answer: '))

        if user_answer != correct_answer:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(user_answer, correct_answer))
            print("Let's try again, {}!".format(name))
            return
        print('Correct!')

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
