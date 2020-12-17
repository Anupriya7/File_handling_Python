import random
def random_line(file):
    with open(file,"r") as f:
        x=f.readlines()

    
    return random.choice(x)


print(random_line('text.txt'))

