def calcAverage(score1,score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5)
    return average
def determineGrade (userScore):
    if (userScore < 60 ):
        return "F"
    elif(userScore < 70):
        return "D"
    elif (userScore < 80):
        return "C"
    elif (userScore < 90):
        return "B"
    elif (userScore < 101):
        return "A"

def askForScore():
    score1 = float( input("please enter score for 1: "))
    score2 = float( input("please enter score for 2:"))
    score3 = float ( input("please enter score for 3:"))
    score4 = float ( input("please enter score for 4:"))
    score5 = float ( input("please enter score for 5:"))
    return score1, score2, score3, score4, score5

def printTableOfResults(score1, score2, score3, score4, score5):
    print("score\tLetter Grade:")
    print(str(score1) + "\t\t" + determineGrade(score1),
          str(score2) + "\t\t" + determineGrade(score2 ),
          str(score3)+ "\t\t" + determineGrade(score3),
          str(score4) + "\t\t" + determineGrade (score4),
          str(score5) + "\t\t" + determineGrade (score5),)

def main():
        score1, score2, score3, score4, score5 = askForScore()
        print()
        printTableOfResults()

main()
