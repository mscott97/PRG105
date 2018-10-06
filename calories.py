def calculatecaloriesfromfat(fatgrams):
    caloriesfromfat = fatgrams * 9
    return caloriesfromfat


def calculatecaloriesfromcrabs(crabsgrams):
    caloriesfromcrabs = crabsgrams * 4
    return caloriesfromcrabs


def calculatecaloriesfromprotein(proteingrams):
    caloriesfromprotein = proteingrams * 4
    return caloriesfromprotein


def main():
    userfatgrams = float(input("Enter Fat Grams"))
    usercrabsgrams = float(input("Enter Crabs Grams"))
    userproteingrams = float(input("Enter Protein Grams"))

    caloriesfromfat = calculatecaloriesfromfat(userfatgrams)
    caloriesfromcrabs = calculatecaloriesfromcrabs(usercrabsgrams)
    caloriesfromprotein = calculateCaloriesfromprotein(userproteingrams)

    print("\nCalories from Fat" + format(caloriesfromfat, ".2f") + "calories", "calories from Crabs:" +
          format(caloriesfromcrabs, ".2f") + "calories",)
    format(caloriesfromprotein, ".2f") + "calories", "calories from Protien:"


main()
