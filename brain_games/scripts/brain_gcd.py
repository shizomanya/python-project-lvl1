import random
import math
from brain_games.cli import welcome_user

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

def play_game():
    print('Find the greatest common divisor of given numbers.')
    name = welcome_user()
    count = 0
    correct_answers = 0

    while count < 3:
        num1, num2 = generate_question()
        print('Question:', num1, num2)
        user_answer = int(input('Your answer: '))
        correct_answer = gcd(num1, num2)

        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
        
        count += 1
    
    if correct_answers == 3:
        print(f'Congratulations, {name}!')

if __name__ == '__main__':
    play_game()
