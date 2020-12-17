def readnlines(n):
    with open("text.txt","r") as f:
        contents=f.readlines()
        for line in contents:
            print(line)


readnlines("text.txt")