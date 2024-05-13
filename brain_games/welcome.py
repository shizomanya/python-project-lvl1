import prompt

GAMES_COUNT = 3


def welcome(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.CONDITIONS)

    for _ in range(GAMES_COUNT):
        question, correct_answer = game.get_game()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"{user_answer} is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
