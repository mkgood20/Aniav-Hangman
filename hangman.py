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
        
    