def human():
    """Inputs a word from user1 and returns it."""
    a = input("Enter the word that user2 should guess: ")
    return a


def hangman(humanWord, max_mistakes=8):
    """The function that initiates the hangman game

    Keyword arguments:
    humanWord -- The word given by user1, as captured in human().
                    Hidden from user2.
    max_mistakes -- The number of incorrect guesses allowed.
                    We set the valuee to 8 by default.
    """

    humanWord = humanWord.strip().lower()  # remove whitespace and lowercase.
    strPattern = "_"*len(humanWord)  # create a masked word
    guessed = set()  # initialise a set to keep track of guessed characters.
    print("Starting the game.\nTo guess: ", strPattern)
    recHangman(humanWord, strPattern, guessed, 0)


def recHangman(humanWord, strPattern, guessed, mists, maxMist=8):
    """The recursive function that enables to play the hangman game.

    Keyword arguments:
    humanWord -- The word given by user1, as captured in human().
                Hidden from user2.
    strPattern -- The pattern visible to user2, based on the guesses.
    guessed -- The set of characters already guessed by user2
    mists -- An integer that counts the number of incorrect guesses by user2.
    maxMist -- The number of incorrect guesses allowed.
                    We set the valuee to 8 by default.
    """
    if "_" not in strPattern:
        print("Wow, you got the whole word right!!!")
        return 1
    elif mists >= maxMist:
        print("Ohoh!! Better lcuk next time.")
        return 0
    else:
        guessChar = input("What's your guess? ")
        guessChar = guessChar.strip().lower()
        if guessChar in guessed:
            print("It seems we already covered that. try a different character")
        else:
            guessed.add(guessChar)
            if guessChar in humanWord:
                strPattern = updatePattern(humanWord,strPattern,guessChar)
                print("yay! thats a hit. There you go:")
                print(strPattern)
            elif guessChar not in humanWord:
                mists += 1
                if maxMist - mists > 0:
                    print("Tough luck!!, guessed character not in the word.")
                    print("You have", maxMist - mists, "chances left")
                print(strPattern)
        if "_" in strPattern:
            print("You already guesssed these:", guessed)
        recHangman(humanWord, strPattern, guessed, mists)


def allCharIndex(theString, theChar, theIndex=-1):
    """
    traverse through word; find indices of the letter in the word

    theString -- word guessed by user1
    theChar  -- letter guessed by user2
    theIndex -- integer; tracks the indices(if any) of theChar in theString
    """
    if not theString:
        return []
    else:
        theIndex += 1
        if theString[0] == theChar:
            return [theIndex] + allCharIndex(theString[1:], theChar, theIndex)
        else:
            return allCharIndex(theString[1:], theChar, theIndex)


def replacer(strPattern, charIndex, theChar):
    """replace _ in strPattern at the indices in charIndex

        strPattern -- stores the current string pattern visible to user2
        charIndex -- indices at which theChar needs to be put in strPattern
        theChar -- current letter guessed by user2
    """
    if not charIndex:
        return strPattern
    else:
        strPattern = strPattern[:charIndex[0]] + theChar + \
            strPattern[charIndex[0]+1:]
        myVal = replacer(strPattern, charIndex[1:], theChar)
        return myVal


def updatePattern(theString, strPattern, theChar, theIndex=-1):
    """find indices in strPattern where theChar is present and replace
    the _ with theChar at those positions.

    theString -- word by user1
    strPattern -- the string pattern visible to the user2
    theChar -- the letter guessed by user2
    theIndex -- integer, index at which theChar is present in strPattern
    """
    if not theString:
        return strPattern
    else:
        theIndex += 1
        if theString[0] == theChar:
            strPattern = strPattern[:theIndex] + theChar + strPattern[theIndex+1:]
        strPattern = updatePattern(theString[1:],strPattern,theChar,theIndex)
        return strPattern



if __name__ == '__main__':
    print("hello")
    qword = human()
    hangman(qword)
