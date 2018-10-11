totalNumberOfMonths = 0
TotalInchesOfRainfall = 0
userNumberOfYears = int(input("Please enter the number of years "))

for currentYear in range(1, userNumberOfYears + 1):

    for currentMonth in range(1, 13):
        monthlyRainfallInches = float(input("Please type the inches " +
                                            "Rainfall for month " + format(currentMonth, "d") +
                                            "Year " + format(currentYear, "d") + ": "))
        TotalInchesOfRainfall += monthlyRainfallInches
        totalNumberOfMonths += 1
averageRainfall = TotalInchesOfRainfall / totalNumberOfMonths

print()

print("Number of months" + format(totalNumberOfMonths, "d", ), "total" +
      "inches of rainfall" + format(TotalInchesOfRainfall, ".2f"),
      "Average rainfall " + format(averageRainfall, ".2f"), )
