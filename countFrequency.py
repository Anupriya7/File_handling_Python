from collections import Counter


def countFrequency(file):
    with open(file) as f:
        c=(Counter(f.read().split()))
        return c

            



print(countFrequency("abc.txt"))

