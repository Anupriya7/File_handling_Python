def RemoveNewLine(file):
    with open(file,"r") as f:
        contents=f.readlines()
        return [s.rstrip('\n') for s in f]


print(RemoveNewLine("abc.txt"))