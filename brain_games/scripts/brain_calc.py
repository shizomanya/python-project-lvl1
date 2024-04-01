import random
from brain_games.game_engine import run_game

DESCRIPTION = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 100
OPERATIONS = ['+', '-', '*']

def generate_question():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation = random.choice(OPERATIONS)
    
    question = f"{num1} {operation} {num2}"
    correct_answer = str(eval(question))
    
    return question, correct_answer

def run():
    run_game(DESCRIPTION, generate_question)

if __name__ == '__main__':
    run()
