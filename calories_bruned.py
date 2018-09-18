caloriesBurnedPerMinute = 4.2

for numberOfMinutes in range(10,31,5):
    numberOfCaloriesBurned = (numberOfMinutes / 1) * caloriesBurnedPerMinute
    print("you will burn",numberOfCaloriesBurned," calories in",numberOfMinutes,"Minutes")
