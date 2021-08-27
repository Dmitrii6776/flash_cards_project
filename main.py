from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data_frame = pandas.read_csv('data/words_to_learn')
except FileNotFoundError:
    data_frame = pandas.read_csv('data/English-russian_words.csv')

dict_data = data_frame.to_dict(orient='records')

current_card = {}


def flip_card():
    canvas.itemconfig(language_label, text='Russian', fill='white')
    canvas.itemconfig(word_label, text=current_card['Russian'], fill='white')
    canvas.itemconfig(card_img, image=card_back_img)


def change_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_img, image=card_front_img)
    current_card = random.choice(dict_data)
    canvas.itemconfig(language_label, text='English', fill='black')
    canvas.itemconfig(word_label, text=current_card['English'], fill='black')
    flip_timer = window.after(3000, flip_card)


def change_word_and_remove():
    dict_data.remove(current_card)
    data = pandas.DataFrame(dict_data)
    data.to_csv("data/words_to_learn", index=False)
    change_word()



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, heigh=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file='./images/card_front.png')
card_back_img = PhotoImage(file='./images/card_back.png')
right_button_img = PhotoImage(file='./images/right.png')
wrong_button_img = PhotoImage(file='./images/wrong.png')
card_img = canvas.create_image(400, 263, image=card_front_img)
language_label = canvas.create_text(400, 150, text='English', font=('Ariel', 40, 'italic'))
word_label = canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

know_button = Button(text=None, image=right_button_img, command=change_word_and_remove)
know_button.grid(column=1, row=1)

unknow_button = Button(text=None, image=wrong_button_img, command=change_word)
unknow_button.grid(column=0, row=1)

change_word()

window.mainloop()
