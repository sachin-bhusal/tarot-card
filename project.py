# This file deals with displaying cards on the screen and connecting the cards to the required function

import tkinter as tk
import PIL.Image, PIL.ImageTk
import random

from meaning import *


# cards list is imported from meaning which is connected to the buttons
def main():
    GUI()


def tips_title():
    return "Tips for choosing cards:"


def tips_text():
    return "Choose exactly 4 cards and close the window when done.\nRelax and mindfully chose your cards, else you might not get an accurate reading."


# STORING CHOSEN cards

chosen_list = []
def button_click(card):
    chosen_list.append(card)


# GUI
def GUI():
    cards = []
    # the generated sequence is stored in this variable

    # generating sequence AKA shuffling
    for card_num_ in range(0, 22):
        card_num = str(card_num_)
        card_position_ = random.choice((0, 1))
        card_position = str(card_position_)
        card = card_position + "." + card_num
        cards.append(card)

    random.shuffle(cards)


    root = tk.Tk()

    root.geometry("847x300")
    root.configure(bg="gray1")

    # loading the card image in tkinter acceptable format
    img = PIL.Image.open("tarot_backdrop.jpg")
    resized_img = img.resize((100, 167))
    card_image = PIL.ImageTk.PhotoImage(resized_img)

    # setting icon and title of file
    root.title("Tarot Reading Game")
    root.iconphoto(True, card_image)

    choose_card_text = "choose 4 more cards"

    title = tk.Text(root, font=("Cambria", 16), fg="gold2", bg="gray1", borderwidth=0)
    title.insert(tk.END, tips_title())
    text = tk.Text(root, font=("Cambria", 12), fg="gold2", bg="gray1", borderwidth=0)
    text.insert(tk.END, tips_text())
    title.place(x=0, y=200)
    text.place(x=0, y=225)

    btn = []
    msg_text = tk.Text(
        root, font=("Cambria", 12), fg="blue4", bg="gray1", borderwidth=0
    )

    for i in range(0, 22):
        btn.append(tk.Button(image=card_image, command=lambda x=i:button_click(cards[x])))


    for i in range(0, 22):
        btn[i].grid(row=0, column=i, columnspan=3)


    root.mainloop()

    reading = []
    # this is a list that contains 4 items that are lists, each item contains three elements
    # 0->card number(0,1,2...21)
    # 1->reading area(0->general, 1->love...)
    # 2->sequence(1->upright,2->reverse)
    for i in range(0, 4):
        chosen = chosen_list[i]
        sequence, card_number = chosen.split(".")
        sequence = int(sequence)
        card_number = int(card_number)
        reading_area = i
        reading.append([card_number, reading_area, sequence])


    general_card = reading[0][0]
    general_card_sequence = reading[0][2]

    love_card = reading[1][0]
    love_card_sequence = reading[1][2]

    career_card = reading[2][0]
    career_card_sequence = reading[2][2]

    finance_card = reading[3][0]
    finance_card_sequence = reading[3][2]

    print(
        "\nGeneral Reading:\n", CardList[general_card][general_card_sequence]["general"]
    )
    print("\nLove Reading:\n", CardList[love_card][love_card_sequence]["love"])
    print("\nCareer Reading:\n", CardList[career_card][career_card_sequence]["career"])
    print(
        "\nFinance Reading:\n", CardList[finance_card][finance_card_sequence]["finance"]
    )

if __name__ == "__main__":
    main()