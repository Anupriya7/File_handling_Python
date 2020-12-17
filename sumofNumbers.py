with open("T.txt","r") as f:
    contents=f.readlines()
    sum=0
    for line in contents:
        if line!="\n":
            sum+=int(line)

    print(sum)

    