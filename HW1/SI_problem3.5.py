import random

def birthday_simulation(n, trials):
    count_B = 0
    for _ in range(trials):
      #Generates a list of n random numbers between 1 and 365, simulating the birthdays of n individuals.
        birthdays = [random.randint(1, 365) for _ in range(n)] 
        if len(birthdays) != len(set(birthdays)):
            count_B += 1
    return count_B / trials

trials = 10000
n = 1
while True:
    probability_B = birthday_simulation(n, trials)
    if probability_B > 0.9:
        break
    n += 1


print(f"Smallest n for P(B) > 0.9: {n}")