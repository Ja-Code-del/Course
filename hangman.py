import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]
# TODO : THIS IS A LIST OF CONGRATS AND ENCOURAGEMENTS
final_congrats = ["Well done", "You win", "Wow Bravissiiiimo", "Yeah! You guessed it", "You did it, champion"]
congrats = ["Correct", "Take my five!", "Word boss!", "Great"]
congrat = ""
encouragements = ["Nooo!, try again", "This letter is not in, sorry", "No, never type it again",
                  "Try gain boss"]
#TODO - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(chosen_word)  #for the test
#TODO: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
lives = 6
#TODO: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
display = []
word_to_display = ""
for i in range(word_length):
    display.append('_')
#TODO : Loop and ask the player to guess the correct letter until he or she find the correct word; will use while loop
end_of_game = False
while not end_of_game and lives > 1:
    word_to_display = ""  #reinitialize word_to_display
    # TODO: - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter into the chosen word ").lower()
    #TODO: - Loop through each position in the chosen_word;
    #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    for i in range(word_length):
        if guess == chosen_word[i]:
            display[i] = guess
            found = True
        word_to_display = ''.join(display)  # to display it more like a word and not a table
    end_of_game = (word_to_display == chosen_word)
    print(word_to_display)
    # TODO : - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
if lives < 1:
    print("GAME OVER")
else:
    print("Well done, You guessed it")

