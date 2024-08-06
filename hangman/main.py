from utils import *
from hangman.ascii_art import logo

#print the logo
logo()

##Menu and choice of the theme
theme = input("What theme do you prefer?\nType fruits, musique, animaux\n")

#choice of the list of word according to the theme chosen
chosen_list = list_selector(theme)

play_game(chosen_list)
