def boring_meals(meals):
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False
        
print(boring_meals(['Roast chicken', 'Meatloaf', 'Pizza', 'Pizza', 'Chicken parmesan', 'Lasagna']))