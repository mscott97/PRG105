def askForExpenses():
    monthlyLoanPayment = float( input("How  much do you pay for your loan" +  "every month:"))

    monthlyInsurancePayment = float( input( "How much do you pay for your insurance" + "Every month:"))

    monthlyGasPayment = float( input("How much do you pay " + "For Gas every month: "))

    monthlyOilPayment = float( input("How much do you pay " + "For Oil each Month:"))

    monthlyTirePayment = float( input("How much do you pay for Tries" + "Each month:"))

    monthlyMaintenacePayment = float( input("How much do you pay for maintenace " + "Each Month:"))

    return monthlyLoanPayment, monthlyInsurancePayment, monthlyGasPayment, monthlyGasPayment, monthlyOilPayment, \
            monthlyTirePayment, monthlyMaintenacePayment
def calculateTotalMonthlyExpenses(payment1, payment2, payment3, payment4, payment5, payment6):

    calculateTotalMonthlyExpenses = payment1 + payment2 + payment3 + payment4 + payment5 + payment6
    return TotalMonthlyExpenses

def calculateTotalAnnualCost( totalMonthlyCost):
    totalAnnualCost = totalMonthlyCost = 12
    return totalAnnualCost
def printDetails(totalMonthlyCost, totalAnnualCost):
    print()
    print("Your total monthly cost is $" + \
          format (totalMonthlyCost, ",. 2f") + "\nYour total" + \
          "annual cost is $" + format(totalAnnualCost, ", . 2f"))
def main():
    loanPayment, insurancePayment, gasPayment, oilPayment, tirePayment, \
    maintenacePayment  = askForExpenses()

    totalMonthlyCost = calculateTotalMonthlCost( loanPayment, insurancePayment, gasPayment, oilPayment, tirePayment,
                                                 maintenacePayment)
    TotalAnnualCost = calculateTotalAnnualCost()
    printDetails()
main()


