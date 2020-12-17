with open("abc.txt","r") as f:
    contents=f.read()
    with open("new_abc.txt","w") as f2:
        for line in contents:
            f2.write(line)