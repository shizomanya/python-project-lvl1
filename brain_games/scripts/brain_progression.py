from random import randint

def generate_progression():
    start = randint(1, 50)
    step = randint(1, 10)
    progression = [str(start + step*i) for i in range(10)]
    hidden_index = randint(0, 9)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    return progression, str(correct_answer)

def brain_progression():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")
    
    for _ in range(3):
        progression, correct_answer = generate_progression()
        print("Question:", ' '.join(progression))
        user_answer = input("Your answer: ")
        
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print("Let's try again, {name}!")
            break
    else:
        print("Congratulations, {name}!")

if __name__ == '__main__':
    brain_progression()
