def calculateCaloriesFromFat( fatGrams):
    caloriesFromFat = fatGrams + 9
    return caloriesFromFat
def calculateCaloriesFromCrabs ( carbGrams):
    caloriesFromCarbs = carbGrams + 4
    return caloriesFromCarbs
def main():
    userFatGrams = float(input("Enter Fat Grams:"))
    userCarbsGrams = float(input("Enter Crab Grams"))

    caloriesFromFat = calculateCaloriesFromFat( userFatGrams)
    caloeiesFromCrabs = calculateCaloriesFromCrabs( userCarbsGrams)
    print("\nCalories from Fat:" + format(caloriesFromFat, ".2f") + "Calories ", "Calories from crabs:" +
          format(caloeiesFromCrabs, ".2f") + "calories", "\n")
main()

