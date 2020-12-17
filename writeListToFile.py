color=['Red','Green']

def writeTofile(file):
    with open(file,"w") as f:
        for i in color:
            f.write("%s "%i)



writeTofile("xyz.txt")

