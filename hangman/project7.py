import random
import randomwords
import hangman_art_logo


lives = 0

print(hangman_art_logo.welcome)
print(hangman_art_logo.logo)

random_choice = random.choice(randomwords.words)
print(random_choice)


placeholder = ""
for place in range(len(random_choice)):
    placeholder+="_"
print(placeholder)


game_over = False
correct_letters = []
while not game_over:
    print(f"*** {lives}/6 lives left. ***")
    guest_letter = input("Guest a letter: ")
    if guest_letter in correct_letters:
        print(f"You've already guessed {guest_letter}.")


    display = ""
    for letter in random_choice:
        if letter == guest_letter:
            display+=letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"
    print(display)
    if guest_letter not in random_choice:
        lives+=1
        print(f"You guessed {guest_letter} , that's not in the word.You lose a life.")
        if lives == 6:
            game_over = True
            print(f"*** It was {random_choice}.You lose! ***")



    if "_" not in display:
        game_over = True
        print("You win!")

    print(hangman_art_logo.stages[lives])