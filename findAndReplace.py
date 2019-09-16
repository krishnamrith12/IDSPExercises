from tco import *

def updatePattern(valList):
    """find and return numbers which are divisible by 7 from a list of integers

    valList -- The list of integers from which the subset of numbers need to be returned.
    """
    if not valList:
        return []
    else:
        if valList[0] %7 == 0:
            return [valList[0]] + updatePattern(valList[1:])
        else:
            return [] + updatePattern(valList[1:])

"""
valList = [0, 1, 2, ...., 74]
[0] + updatePattern([1, 2, 3, ....., 74])
[0] + [] + updatePattern([ 2, 3, ....., 74])
[0] + [] + [] + updatePattern([ 3, ....., 74])
....
[0] + [] + [] + ... [7] + updatePattern([ 8, 9,  ....., 74])
"""


 
def updatePatternExtraList(valList, passList=[]):
    """find and return numbers which are divisible by 7 from a list of integers

    valList -- The list of integers from which the subset of numbers need to be returned.
    passList -- List where the integers that passed the criteria so far are stored at any given isntance.
    """
    if not valList:
        return passList
    else:
        if valList[0] %7 == 0:
            passList.append(valList[0]) 
        return  updatePatternExtraList(valList[1:],passList)



# download https://github.com/baruchel/tco or pip install tco
@with_continuations()
def updatePatternTail(valList, passList=[], self=None):
   """find and return numbers which are divisible by 7 from a list of integers

    valList -- The list of integers from which the subset of numbers need to be returned.
    passList -- List where the integers that passed the criteria so far are stored at any given isntance.
    self -- Mandatory requirement by the library
    """
    if not valList:
        return passList
    else:
        if valList[0] %7 == 0:
            passList.append(valList[0])
        return self(valList[1:], passList)

valList = range(75)
print(updatePattern(valList))
print(updatePatternExtraList(valList))
#print(updatePatternTail(valList))