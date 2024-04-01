from random import randint
import prompt

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def brain_prime():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    
    correct_answers = 0
    while correct_answers < 3:
        number = randint(1, 100)
        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ")
        
        if (is_prime(number) and user_answer == "yes") or (not is_prime(number) and user_answer == "no"):
            print("Correct!")
            correct_answers += 1
        else:
            if is_prime(number):
                correct_answer = "yes"
            else:
                correct_answer = "no"
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    
    if correct_answers == 3:
        print(f"Congratulations, {name}!")

if __name__ == '__main__':
    brain_prime()
