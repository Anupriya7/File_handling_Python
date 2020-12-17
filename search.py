with open("text.txt","r") as f:
    contents=f.readlines()
    #print(contents)
    for line in contents:
       if "Python" in line:
           print("yes")