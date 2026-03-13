import random

def generate_secret_numbers(seed):
    random.seed(seed)
    return random.randint (1,100)
