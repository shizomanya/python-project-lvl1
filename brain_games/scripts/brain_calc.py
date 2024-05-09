#!/usr/bin/env python3
import random
import prompt


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])

    question = f"{num1} {operation} {num2}"
    correct_answer = str(eval(question))

    return question, correct_answer


def main():
    print("brain-calc")
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

    for _ in range(3):
        number, correct_answer = generate_question()
        print('Question: {}'.format(number))
        user_answer = prompt.string("Your answer: ")

        if user_answer != correct_answer:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(user_answer, correct_answer))
            print("Let's try again, {}!".format(name))
            return
        print('Correct!')

    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
