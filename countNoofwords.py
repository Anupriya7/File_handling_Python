import string

with open("abc.txt","r") as f:
    contents=f.read()
    contents=contents.strip()
    contents=contents.translate(contents.maketrans("","",string.punctuation))
    i=0
    for line in contents:
        if line!=" " and line!="\n":
            print(line)
            i+=1

    print(i)
