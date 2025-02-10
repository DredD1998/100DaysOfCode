import art
import main
import random

def format_data(account):
    
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_desc}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(art.logo)
score = 0

random_data_b = random.choice(main.data)

game_should_continue = True
while game_should_continue:



    random_data_a = random_data_b
    random_data_b = random.choice(main.data)
    if random_data_a == random_data_b:
        random_data_b = random.choice(main.data)


    print(f"Compare A: {format_data(random_data_a)}.")
    print(art.vs)
    print(f"Against B: {format_data(random_data_b)}.")


    guess = input("Who has more followers? Type 'A' or 'B': ").lower()



    a_follower_count = random_data_a["follower_count"]
    b_follower_count = random_data_b["follower_count"]



    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Your current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False