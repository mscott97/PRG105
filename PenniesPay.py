numberOfDaysWorked = int(input("Please enter how many days you worked ?"))
totalNumberOfpennies = 0
print()

print("day\tSalary\n----\t----")
for currentDay in range(numberOfDaysWorked):
    penniesForTheday = 2 ** currentDay
totalNumberOfpennies += penniesForTheday
print(currentDay + 1,"\t", penniesForTheday)

totalPay = totalNumberOfpennies * 0.01

print("/Total pay = $, totalPay sep =")
