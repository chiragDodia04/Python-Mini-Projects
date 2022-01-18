from random import randint
EASY_LEVEL = 10
HARD_LEVEL = 5
turns = 0

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Its too HIGH!!")
        return turns - 1
    elif guess < answer:
        print("Its too LOW!!")
        return turns - 1
    else:
        print(f"This is the CORRECT ANSWER!!! {answer}")

def set_difficulty():
    level = input("Choose the difficulty, type 'easy'or 'hard':")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    print("GUESSING GAME")
    print("computer is thinking of a number from 1 to 100.")
    answer = randint(1,100)
    print(f"the correct answer {answer}")
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} life remaining to guess the computer number.")
        guess = int(input("make a guess:"))
        if turns == 0:
            print("YOU LOST!!!!!!!!!!")
            return
        turns = check_answer(guess, answer, turns)
game()


