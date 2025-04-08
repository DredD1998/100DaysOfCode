from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}

to_learn = {}
try:

    data = pd.read_csv("flash-card-project-start/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("flash-card-project-start/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    Canvas.itemconfig(card_title, text="French",fill= "black")
    Canvas.itemconfig(card_word, text=current_card["French"],fill= "black")
    Canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    Canvas.itemconfig(card_title, text="English",fill = "white")
    Canvas.itemconfig(card_word, text=current_card["English"],fill= "white")
    Canvas.itemconfig(card_background, image=card_back_img)



def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("flash-card-project-start/data/words_to_learn.csv",index=False)
    next_card()



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)
Canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(
    file="flash-card-project-start/images/card_front.png")
card_back_img = PhotoImage(
    file="flash-card-project-start/images/card_back.png")
card_background = Canvas.create_image(400, 263, image=card_front_img)
card_title = Canvas.create_text(
    400, 150, text="", font=("Ariel", 40, "italic"))
card_word = Canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
Canvas.grid(column=0, row=0, columnspan=2)


cross_image = PhotoImage(
    file="flash-card-project-start/images/wrong.png")
unknown_button_img = Button(
    image=cross_image, highlightthickness=0, command=next_card)
unknown_button_img.grid(column=0, row=1)

check_image = PhotoImage(
    file="flash-card-project-start/images/right.png")
known_button_img = Button(
    image=check_image, highlightthickness=0, command=is_known)
known_button_img.grid(column=1, row=1)
next_card()

window.mainloop()
