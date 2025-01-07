import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []
    numbers = range(min, max + 1)
    return random.sample(numbers, quantity)

print(get_numbers_ticket(1, 10, 5))