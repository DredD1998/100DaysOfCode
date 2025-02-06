import random
import logo



EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURN = 5
attempts = 0
def check_answer(user_guess,actual_answer,turns):
    global attempts
    attempts+=1
    if user_guess > actual_answer:
        print("The number you guessed is very high.")
        return turns -1
    elif user_guess < actual_answer:
        print("The number you guessed is very low.")
        return turns -1
    else:
        print(f"Congrats! You guessed the number in {attempts} attempts!")
 



def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURN
    
def game():
    print("Welcome to the Number Guessing Game!")
    print(logo.logo)
    print("I am thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    print(f"The correct answer is: {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You've run out of guesses, You lose!")
            break


game()