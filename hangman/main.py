import random
from data import *
from stages import stages
from hangman.ascii_art import logo, looser_message
import feedbacks


def alert_box(something_to_print):
    print(something_to_print)


logo()
message = ""

##Menu and choice of the theme
theme = input("What theme do you prefer?\nType fruits, musique, animaux")
themes_name = ["fruits", "music", "animaux"]
themes = [fruits, musique, animaux]
themes_dict = dict(zip(themes_name, themes))
word_list = themes_dict.get(theme, [])

# def play_game(word_list):
#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
congrat = ""
chosen_word = word_list[random.randint(len(word_list) - 1)]
chosen_word_hint = c
word_length = len(chosen_word)

#for the test
print(f"This is a {word_length} letters word")
#Create variables called 'lives' & 'score' to keep track of the number of lives left and the score
#Set 'lives' to equal 6.
lives = 10
score = 10 - lives
#Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
display = []
#word_to_display is the string,

for i in range(word_length):
    display.append('_')
    #now every element of display are _ display look like ['_', '_',...., '_']
#Loop and ask the player to guess the correct letter until he or she finds the correct word; will use while loop
end_of_game = False
while not end_of_game:
    # reinitialize word_to_display
    word_to_display = ""
    message = ""
    if lives > 0:
        #Ask the user to guess a letter and assign their answer to a variable called guess. Make guess
        #  lowercase.
        guess = input("Guess a letter into the chosen word ").lower()
        #if the player has already guessed the word
        if guess in display:
            print(f"You have already guessed {guess}")
        #Loop through each position in the chosen_word;
        #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
        for i in range(word_length):
            if guess == chosen_word[i]:
                display[i] = guess
                message = random.choice(feedbacks.congrats)
            word_to_display = ''.join(display)  # to display it more like a word and not a table
        #check now if the game can end if all the letter of display match with the chosen word
        end_of_game = (word_to_display == chosen_word)
        print(word_to_display)
        #Check if guess match not a letter in the word then reduce lives by 1
        if guess not in chosen_word:
            message = ""
            lives -= 1
            message = random.choice(feedbacks.encouragements)
    else:
        end_of_game = True
    print(message)
    #print the ASCII art
    print(stages[lives])
#out of while now
final_congratulation = random.choice(feedbacks.final_congrats)
if lives <= 0:
    print(looser_message)
    print(f"The word was {chosen_word}")
else:
    alert_box(final_congratulation)
    alert_box(f"your score is {score} ")
