with open("input.txt","r") as f:
    contents=f.read()
    #print(len(contents))
    #for con
    #contents=contents.strip()
    c=0
    c2=0
    print(contents)
    for line in contents:
        if line=="\t":
            c+=1
        elif line==" ":
            c2+=1
        
            
    print(c)
    print(c2)
    #print(i+1)

        
