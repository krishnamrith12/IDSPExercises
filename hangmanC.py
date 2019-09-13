def human():
    theWord = input("enter the word")
    return theWord


def hangman(humanWord):
    strPattern = "_"*len(humanWord)
    guessChar = input("enter the character to guess")
    guessed = set()
    maxMistakes = 8
    mists = 0
    recHangman(humanWord,strPattern,guessed,mists,maxMistakes)


def recHangman(humanWord2, strPattern, guessed, mists, maxMist):
    if mists >= maxMist:
        print("Better luck next time")
        return 0
    elif "_" not in strPattern:    
        print("yay!! you got it right")
        return 1
    else:
        guessChar = input("what's your guess?")
        if guessChar in guessed:
            print("you have alreeady guessed that. Try something new")
        else:
           
            guessed.add(guessChar)
            if guessChar in humanWord2:
                allIndices = allCharIndex(humanWord2, guessChar)
                strPattern = replacer(strPattern, allIndices, guessChar)
                print("updateds pattern is", strPattern)
            
            else:
                mists = mists + 1
                print("remaining chances:", maxMist - mists )

        recHangman(humanWord2,strPattern, guessed, mists, maxMist)


def allCharIndex(theString, theChar, theIndex=-1):
    if not theString:
        return []
    else:
        theIndex = theIndex + 1
        if theString[0] == theChar:
            return [theIndex] + allCharIndex(theString[1:], theChar, theIndex)
        else: 
            return allCharIndex(theString[1:],theChar,theIndex)


def replacer(strPattern, charIndex, theChar):
    if not charIndex:
        return strPattern
    else:
        strPattern = strPattern[:charIndex[0]]+ theChar + strPattern[charIndex[0] + 1:]
        myVal = replacer(strPattern,charIndex[1:], theChar )
        return myVal      

    

    



qword = human()
hangman(qword)
