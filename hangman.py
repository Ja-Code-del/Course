import random
def logo():
    ascii_art = """
 _    _                                         
| |  | |                                        
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/                       
    """
    print(ascii_art)

logo()


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
word_list = [
    "pomme", "orange", "banane", "raisin", "kiwi", "mangue", "ananas", "cerise",
    "fraise", "framboise", "mûre", "myrtille", "pêche", "prune", "abricot",
    "nectarine", "cassis", "groseille", "poire", "pamplemousse", "citron",
    "mandarine", "pastèque", "melon", "papaye", "figue", "datte", "grenade",
    "litchi", "coco", "carotte", "tomate", "courgette", "brocoli", "chou",
    "épinard", "poivron", "patate", "aubergine", "radis"
]
ecole = [
    "élève", "professeur", "classe", "école", "cahier", "stylo", "crayon",
    "tableau", "bureau", "chaise", "ordinateur", "livre", "règle", "trousse",
    "cartable", "dictionnaire", "ardoise", "colle", "gomme", "ciseaux",
    "peinture", "feutre", "brouillon", "devoir", "examen", "dictée", "leçon",
    "matière", "récréation", "cantine", "horaire", "emploi", "directeur",
    "laboratoire", "bibliothèque", "cour", "gymnase", "stade", "uniforme",
    "note", "bulletin", "formation", "programme", "étude", "formation",
    "maître", "institutrice", "pupitre", "calendrier", "diplôme"
]
maths = [
    "addition", "soustraction", "multiplication", "division", "fraction",
    "décimale", "pourcentage", "algèbre", "géométrie", "arithmétique",
    "équation", "inégalité", "variable", "constante", "coefficient",
    "intégrale", "dérivée", "fonction", "graphique", "matrice", "vecteur",
    "polynôme", "racine", "exposant", "logarithme", "probabilité",
    "statistique", "moyenne", "médiane", "mode", "écart", "variance",
    "écart-type", "hypothèse", "théorème", "postulat", "axiome", "corollaire",
    "démonstration", "preuve", "calcul", "approximation", "solution",
    "intersection", "union", "ensemble", "somme", "produit", "différence",
    "quotient"
]
informatique = [
    "algorithme", "variable", "fonction", "boucle", "condition", "tableau",
    "donnée", "fichier", "réseau", "serveur", "client", "protocole",
    "cryptographie", "programmation", "compilateur", "interpréteur", "code",
    "bug", "débogage", "mémoire", "processeur", "stockage", "système",
    "logiciel", "matériel", "interface", "base", "donnée", "requête",
    "serveur", "client", "protocole", "cryptographie", "programmation",
    "compilateur", "interpréteur", "code", "bug", "débogage", "mémoire",
    "processeur", "stockage", "système", "logiciel", "matériel", "interface",
    "base", "donnée", "requête", "heuristique", "machine", "apprentissage",
    "intelligence", "artificielle", "réalité", "virtuelle", "robotique",
    "nanotechnologie"
]
music = [
    "accord", "batterie", "basse", "chant", "chanson", "chœur", "chorale",
    "compositeur", "concert", "contrebasse", "couplet", "cymbale", "djembé",
    "flûte", "guitare", "harmonica", "harmonie", "harpe", "instrument",
    "jazz", "lyrique", "mélodie", "musicien", "octave", "orchestre",
    "partition", "piano", "quatuor", "refrain", "rythme", "saxophone",
    "solfège", "solo", "sonate", "symphonie", "tambour", "tempo", "ténor",
    "trombone", "trompette", "ukulélé", "violon", "violoncelle", "voix",
    "compositeur", "maestro", "orchestrateur", "batteur", "chef", "d'orchestre"
]
sport = [
    "football", "basketball", "tennis", "natation", "athlétisme", "cyclisme",
    "boxe", "volley-ball", "rugby", "golf", "hockey", "karaté", "judo",
    "escrime", "gymnastique", "haltérophilie", "handball", "ski", "snowboard",
    "surf", "baseball", "cricket", "ping-pong", "badminton", "course",
    "marathon", "sprint", "lancer", "saut", "équitation", "escalade",
    "aviron", "canotage", "plongée", "voile", "planche", "à voile", "triathlon",
    "boxe", "thaïlandaise", "muay-thaï", "lutte", "grecque", "romaine",
    "crossfit", "fitness", "musculation", "aérobic"
]
cuisine = [
    "recette", "chef", "cuisinier", "four", "poêle", "casserole", "couteau",
    "planche", "mélanger", "battre", "faire", "frire", "cuire", "griller",
    "rôtir", "bouillir", "sauter", "émincer", "hacher", "mijoter", "assaisonner",
    "mariner", "ingrédient", "épice", "herbe", "sel", "poivre", "huile",
    "vinaigre", "sucre", "farine", "levure", "beurre", "lait", "crème", "fromage",
    "œuf", "pâte", "riz", "pomme", "de", "terre", "poulet", "bœuf", "poisson",
    "légume", "fruit", "sauce", "soupe"
]
automobile = [
    "moteur", "voiture", "carburant", "essence", "diesel", "électrique",
    "hybride", "batterie", "accélérateur", "frein", "embrayage", "transmission",
    "vitesses", "châssis", "carrosserie", "pare-brise",
    "phares", "rétroviseur", "pneus", "jantes", "amortisseurs", "suspension",
    "échappement", "pot", "catalytique", "turbo", "radiateur", "ventilateur",
    "filtre-à-air", "huile", "vidange", "courroie", "alternateur",
    "démarreur", "essuie-glaces", "volant", "sièges", "compteur", "climatisation", "chauffage", "autoradio", "GPS" 
    "ceinture", "sécurité", "airbag"
]




message = ""
looser_message = """  ____                       ___                 
 / ___| __ _ _ __ ___   ___ / _ \__   _____ _ __ 
| |  _ / _` | '_ ` _ \ / _ \ | | \ \ / / _ \ '__|
| |_| | (_| | | | | | |  __/ |_| |\ V /  __/ |   
 \____|\__,_|_| |_| |_|\___|\___/  \_/ \___|_|   
"""
# TODO : THIS IS A LIST OF CONGRATS AND ENCOURAGEMENTS
final_congrats = ["Well done", "You win", "Wow Bravissiiiimo", "Yeah! You guessed it", "You did it, champion"]
congrats = ["Correct", "Take my five!", "Word boss!", "Great"]
congrat = ""
encouragements = ["Nooo!, try again", "This letter is not in, sorry", "No, never type it again",
                  "Try gain boss"]
#TODO - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(f"This is a {word_length} letters word")  #for the test
#TODO: - Create variables called 'lives' & 'score' to keep track of the number of lives left and the score
#Set 'lives' to equal 6.
lives = 6
score = 6 - lives
#TODO: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
display = []
#word_to_display is the string, concatenate form of display
word_to_display = ""
for i in range(word_length):
    display.append('_')
    #now every element of display are _ display look like ['_', '_',...., '_']
#TODO : Loop and ask the player to guess the correct letter until he or she find the correct word; will use while loop
end_of_game = False
while not end_of_game:
    word_to_display = ""  #reinitialize word_to_display
    message = ""
    if lives > 0:
        # TODO: - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess
        #  lowercase.
        guess = input("Guess a letter into the chosen word ").lower()
        #TODO: - Loop through each position in the chosen_word;
        #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
        for i in range(word_length):
            if guess == chosen_word[i]:
                display[i] = guess
                message = random.choice(congrats)
            word_to_display = ''.join(display)  # to display it more like a word and not a table
        #check now if the game can end if all the letter of display match with the chosen word
        end_of_game = (word_to_display == chosen_word)
        print(end_of_game)
        #TODO: Check if guess match not a letter in the word then reduce lives by 1
        if guess not in chosen_word:
            message = ""
            lives -= 1
            message = random.choice(encouragements)
    else:
        end_of_game = True
    print(message)
    print(word_to_display)
    # TODO : - print the ASCII art
    print(stages[lives])
#out of while now
final_congratulation = random.choice(final_congrats)
if lives <= 0:
    print(looser_message)
else:
    print(final_congratulation)
