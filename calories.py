def calculate_calories_from_fat(fatgrams):
    calories_from_fat = fatgrams * 9
    return calories_from_fat


def calculate_calories_from_crabs(crabsgrams):
    calories_from_crabs = crabsgrams * 4
    return calories_from_crabs


def calculate_calories_from_protein(proteingrams):
    calories_from_protein = proteingrams * 4
    return calories_from_protein


def main():
    user_fat_grams = float(input("Enter Fat Grams"))
    user_crabs_grams = float(input("Enter Crabs Grams"))
    user_protein_grams = float(input("Enter Protein Grams"))

    calories_from_fat = calculate_calories_from_fat(user_fat_grams)
    calories_from_crabs = calculate_calories_from_crabs(user_crabs_grams)
    calories_from_protein = calculate_calories_from_protein(user_protein_grams)

    print("\nCalories from Fat" + format(calories_from_fat, ".2f") + "calories", "calories from Crabs:" +
          format(calories_from_crabs, ".2f") + "calories",)
    format(calories_from_protein, ".2f") + "calories", "calories from Protien:"
