import prompt


def welcome_user():
    print('brain-games')
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
