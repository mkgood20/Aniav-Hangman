import random
randomWords = ["ducks" , "jumbo" ,"lucky" , "pills" , "flour"]
secret = random.choice (randomWords)
letter = ""
updateWord = []
#print secret 
def initialize(): 
    print "We have a secret word"
    print "_ _ _ _ _"
def getLetter():
    print "Enter a letter"
    global letter
    letter = raw_input()     
def ifWon():
    if secret == updateWord: 
        print "you win"
    else:
        getLetter()

def test ():
    global letter
    global secret
    if letter in secret:
        updated(undatedworddisplay)
        ifWon()
    else:
        updated(updatedWord)
        get letter()
    global updatedWord

def main():
    initialize ()
    getLetter()
    ifWon()
main()


def test():
    global secret
    letter=int(input(What is letter :))
    if letter in secret:
        pos=secret.find(letter)
        updatedWord[pos]
        ifWon()
    else:
        updated(updatedWord)
        global updatedWord
        
    