import random
from words import fruits
message = ""
word_list = fruits
#THIS IS A LIST OF CONGRATS AND ENCOURAGEMENTS
final_congrats = ["Well done", "You win", "Wow Bravissiiiimo", "Yeah! You guessed it", "You did it, champion"]
congrats = ["Correct", "Take my five!", "Word boss!", "Great"]
congrat = ""
encouragements = ["Nooo!, try again", "This letter is not in, sorry", "No, never type it again",
                  "Try gain boss"]
#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(f"This is a {word_length} letters word")  #for the test
#Create variables called 'lives' & 'score' to keep track of the number of lives left and the score
#Set 'lives' to equal 6.
lives = 6
score = 6 - lives
#Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
display = []
#word_to_display is the string, concatenate form of display
word_to_display = ""
for i in range(word_length):
    display.append('_')
    #now every element of display are _ display look like ['_', '_',...., '_']
#Loop and ask the player to guess the correct letter until he or she find the correct word; will use while loop
end_of_game = False
while not end_of_game:
    word_to_display = ""  #reinitialize word_to_display
    message = ""
    if lives > 0:
        #Ask the user to guess a letter and assign their answer to a variable called guess. Make guess
        #  lowercase.
        guess = input("Guess a letter into the chosen word ").lower()
        #Loop through each position in the chosen_word;
        #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
        for i in range(word_length):
            if guess == chosen_word[i]:
                display[i] = guess
                message = random.choice(congrats)
            word_to_display = ''.join(display)  # to display it more like a word and not a table
        #check now if the game can end if all the letter of display match with the chosen word
        end_of_game = (word_to_display == chosen_word)
        print(end_of_game)
        #Check if guess match not a letter in the word then reduce lives by 1
        if guess not in chosen_word:
            message = ""
            lives -= 1
            message = random.choice(encouragements)
    else:
        end_of_game = True
    print(message)
    print(word_to_display)
    #print the ASCII art
    print(stages[lives])
#out of while now
final_congratulation = random.choice(final_congrats)
if lives <= 0:
    print(looser_message)
else:
    print(final_congratulation)
