import os

def size(file):
    with open(file) as f:
        stat_info=os.stat(file)
        return stat_info.st_size


print(size("count.txt"))