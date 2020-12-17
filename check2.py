with open("file.csv","r") as f:

    contents=f.readlines()
    sum=0

    for line in contents[1:]:
        line=line.strip("\n")
        sum+=int(line.split(",")[1])


    print(sum)
        