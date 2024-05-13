import random

CONDITIONS = 'What number is missing in the progression?'


def generate_progression():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    progression = [str(start + step * i) for i in range(10)]
    hidden_index = random.randint(0, 9)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    return progression, str(correct_answer)


def get_game():
    question, correct_answer = generate_progression()
    question_str = ' '.join(question)
    return question_str, correct_answer
