with open("abc.txt","r") as f:
    contents=f.read()
    contents=contents.split()
    contents=contents[::-1]
    words=(" ".join(contents))
    with open("Ntofirst.txt","w") as f2:
        for line in words:
            f2.write(line) 