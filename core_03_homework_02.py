import random

# Function to get given number of random integer values within given range
def get_numbers_ticket(min_value: int, max_value: int, quantity: int) -> list:
    """
    Gets a given number of random integer values within a given range

    Input:
    :param min_value: integer
    :param max_value: integer
    :param quantity: integer
    
    Output:
    :return: list
    """
    if min_value < 1 or max_value > 1000 or not 0 < quantity <= max_value - min_value + 1:
        return []
    set_of_numbers = set()
    while len(set_of_numbers) < quantity:
        set_of_numbers.add(random.randrange(min_value, max_value + 1))
    return sorted(list(set_of_numbers))
