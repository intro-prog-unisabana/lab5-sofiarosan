import random

def generate_secret_numbers(seed):
    random.seed(seed)
    return random.randint (start=1,end=100)
