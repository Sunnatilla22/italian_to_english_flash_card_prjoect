from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words_to_learn={}
# --------------------------COMMAND SETUP---------------------------------#
try:
    words_to_learn_data = pandas.read_csv("./data/words_to_learn.csv")
    words_to_learn = words_to_learn_data.to_dict(orient="records")
except:
    data = pandas.read_csv("./data/italian_words.csv")
    words_to_learn = data.to_dict(orient="records")


# print(italian_words_dict)

def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(canvas_title, text="Italian", fill="black")
    canvas.itemconfig(canvas_word, text=current_card["Italian"], fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_font, image=canvas_back_img)

def is_known():
    words_to_learn.remove(current_card)
    print(current_card)
    df = pandas.DataFrame(words_to_learn)
    df.to_csv("./data/words_to_learn.csv", index=False)
    next_word()


# --------------------------UI SETUP---------------------------------#
window = Tk()
window.title("Italian-English Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_back_img = PhotoImage(file="./images/card_back.png")
canvas_front_img = PhotoImage(file="./images/card_front.png")
canvas_font = canvas.create_image(400, 263, image=canvas_front_img)
canvas_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="Word", font=("Arial", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file="./images/right.png")
known_button = Button(image=right_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)
wrong_img = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=wrong_img, highlightthickness=0, command=next_word)
unknown_button.grid(row=1, column=0)

next_word()

window.mainloop()
