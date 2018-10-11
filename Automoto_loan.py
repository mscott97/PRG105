def ask_for_expenses():
    monthly_loan_payment = float(input("How  much do you pay for your loan" + "every month:"))

    monthly_insurance_payment = float(input("How much do you pay for your insurance" + "Every month:"))

    monthly_gas_payment = float(input("How much do you pay " + "For Gas every month: "))

    monthly_oil_payment = float(input("How much do you pay " + "For Oil each Month:"))

    monthly_tire_payment = float(input("How much do you pay for Tries" + "Each month:"))

    monthly_maintenace_payment = float(input("How much do you pay for maintenace " + "Each Month:"))

    total = calculate_total_monthly_expense(monthly_loan_payment, monthly_insurance_payment, monthly_gas_payment, monthly_gas_payment,monthly_oil_payment ,
           monthly_tire_payment, monthly_maintenace_payment)
    return total


def calculate_total_monthly_expense(payment1, payment2, payment3, payment4, payment5, payment6, payment7, ):
    calculate_total_monthly_expenses = payment1 + payment2 + payment3 + payment4 + payment5 + payment6 + payment7
    print(calculate_total_monthly_expenses)
    return calculate_total_monthly_expenses


def calculate_total_annual_cost(total_monthly_cost):
    total_annual_cost = total_monthly_cost * 12
    print(total_annual_cost)
    return total_annual_cost


def printDetails(total_monthly_cost, total_annual_cost ):
    print()
    print("Your total monthly cost is $" + \
          format(total_monthly_cost, ",.2f") + "\nYour total" + \
          "annual cost is $" + format(total_annual_cost, ",.2f"))


def main():
    expenses = ask_for_expenses()
    total_annual_cost = calculate_total_annual_cost(expenses)
    printDetails(expenses, total_annual_cost)


