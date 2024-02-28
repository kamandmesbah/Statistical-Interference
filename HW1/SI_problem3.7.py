import random

def birthday_simulation_C(n, trials):
    count_C = 0
    for _ in range(trials):
        birthdays = [random.randint(1, 365) for _ in range(n)]
        unique_birthdays = set(birthdays)
        for day in unique_birthdays:
            if birthdays.count(day) >= 3:
                count_C += 1
                break
    return count_C / trials

trials = 10000
n = 1
while True:
    probability_C = birthday_simulation_C(n, trials)
    if probability_C > 0.5:
        break
    n += 1

print(f"Smallest n for P(C) > 0.5: {n}")