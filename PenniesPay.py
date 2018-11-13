numberOfDaysWorked = int(input("Please enter how many days you worked ?"))
totalNumberOfPennies = 0

print()

print("day\tSalary\n----\t----")
for  currentDay in range(numberOfDaysWorked ):
    PenniesForTheDay = 2 ** currentDay
    totalNumberOfPennies += PenniesForTheDay
    print(currentDay + 1,"\t",PenniesForTheDay )

totalPay = totalNumberOfPennies * 0.01

print("\nTotal pay: $", totalPay,)
