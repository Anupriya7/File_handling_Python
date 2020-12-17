def appendArray(fileName):
    with open(fileName,"r") as f:
        content_Array=[]
        for line in f:
            content_Array.append(line)

        print(content_Array)



appendArray("text.txt")