#Hangman

#given code
lives = 10 # = # of incorrect guesses
word = "orange"

#project brief
#if you guess a letter correct, it does NOT subtract a life
#if you guess incorrect, decrement lives.
#can the user guess all the letters before running out of lives


wordList = list(word)

def hello :
    print("WELCOME TO \n💀HANGMAN.PY💀"+
    "\n😱😟🤯😰🧟‍😱😟🤯😰🧟‍♂️😱😟🤯😰🧟‍♂️😱😟🤯😰🧟‍♂️😱😟🤯😰🧟‍♂️♂️"+
    "\n_ _ _ _ _ _ "+
    " \nYOU MUST GUESS MY SECRET WORD🔮")

def getRevealedString(guessSet) =
    revealed = ""
    for letter in wordList
    if letter in guessSet:
        revealed += letter+" "
    else:
        revealed+= "_ "
    return(revealed)

hello()
guessSet = set

while lives >= 0:
    guess = input("Please guess a leter from my secret word: ")
    guessSet.add(guess.lower())
    if letter in wordList:#guess =="correct":
        print("CORRECT :)")
        continue;
    elsif guess in guessSet:    #guess was already guessed
        print("you have already guessed this letter")
        continue;
    else: #guess is incorrect
        #TODO: decrement lives
        #TODO: print lives left
        #TODO: if lives<=0: break, you are out of lives
    revealed = getRevealedString(guessSet)
