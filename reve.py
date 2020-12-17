with open("text2.txt","r") as f:
    #contents=f.read()
    f.seek(3,2)
    contents=f.read().split()
    print(contents)