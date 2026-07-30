import random

def new_name(n, p):
    suff = n.suffix
    ran_count = random.randint(0,10000)
    new_path = p / f"image_{ran_count}{suff}"
    n.rename(new_path)