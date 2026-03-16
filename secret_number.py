import random

def seed_secret_numbers(seed):
    """Initialize random generator with seed."""
    random.seed(seed)

def generate_secret_number(start=1, end=100):
    """Return a random number between start and end."""
    return random.randint(start, end)
