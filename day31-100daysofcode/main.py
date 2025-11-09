from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
try:
    df = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    org_df = pd.read_csv("./data/french_words.csv")
    to_learn = org_df.to_dict("records")
else:
    to_learn = df.to_dict(orient="records")

new_random_word = {}


# Save Your Progress
def mark_known():
    # optionally guard: if not new_random_word: return
    try:
        to_learn.remove(new_random_word)
    except ValueError:
        # If something went out of sync, ignore and continue
        pass
    pd.DataFrame(to_learn).to_csv("./data/words_to_learn.csv", index=False)
    if not to_learn:
        # disable buttons + show "done" message (your choice)
        print("You're done")
        return
    create_new_flash_card()

# Flip the Cards
def flip_the_cards():
    canvas.itemconfig(canvas_image, image=card_back_png)
    canvas.itemconfig(title_text, fill="white", text="English")
    canvas.itemconfig(word_text, fill="white", text=new_random_word["English"])

# Create New Flash Cards
def create_new_flash_card():
    global new_random_word, flip_timer
    window.after_cancel(flip_timer)
    new_random_word = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=new_random_word["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_png)
    flip_timer = window.after(3000, flip_the_cards)

# UI
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, flip_the_cards)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front_png = PhotoImage(file="./images/card_front.png")
card_back_png = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400,266, image=card_front_png)
title_text = canvas.create_text(400,150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400,263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_png = PhotoImage(file="./images/right.png")
known_button = Button(image=right_png, highlightthickness=0, command=mark_known)
known_button.grid(row=1, column=0)

wrong_png = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=wrong_png, highlightthickness=0, command=create_new_flash_card)
unknown_button.grid(row=1, column=1)

create_new_flash_card()

window.mainloop()