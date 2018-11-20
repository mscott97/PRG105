def getUserNumbers(numberOfUserNumbers):
    userNumberlist =
    for currentUserNumberIndex in range(numberOfUserNumbers):
        userNumber = int(input("please enter number that is between 1 though 100" +\
            str((currentUserNumberIndex + 1)) + "!"))
        userNumberlist.append(userNumber)

        return userNumberlist

def findLowestNumber(userNumberlist):
    lowestNumber = min(userNumberlist)
    return lowestNumber

def findHighestNumber(userNumberlist):
    highestNumber = max(userNumberlist)
    return highestNumber

def calculateTotalOfNumbers(userNumberlist):
    totalOfnumbers = 0
        for currentUserNumberindex in range(len(userNumberlist)):
            totalOfnumbers = totalOfnumbers +\
                userNumberlist[currentUserNumberindex]
        return totalOfnumbers

def calculateAverageOfNumbers(userNumberList, totalOfNumbers):
    numberOfnumberInList = len(userNumberList)
    averageOfNumbers = TotalOfNumbers / numberOfnumberInList
    return averageOfNumbers

def printNumberAnalysis(userNumberList, lowerNumber, highestNumber, \
                        totalOfNumbers, averageOfNumbers):
    print("\nUser numbers provoide: ")
    for currentUserNumberIndex in range(len(userNumberList)):
        if currentUserNumberIndex == len(userNumberList)-1:
            print(userNumberList[currentUserNumberIndex])
        else:
            print(userNumberList[currentUserNumberIndex])
        

