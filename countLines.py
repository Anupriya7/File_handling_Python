def countLines(file):
    with open(file) as f:
        contents=f.readlines()
        print(len(contents))



print(countLines("count.txt"))