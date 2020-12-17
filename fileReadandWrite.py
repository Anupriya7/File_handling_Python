import string
with open("abc.txt","r") as f:
    with open("abcd.csv","w") as f2:
        contents=f.read()
        contents=contents.replace("#","")
       # contents=contents.translate(contents.maketrans("","",string.punctuation))
        contents=contents.split()
        f2.write("name"+"\n")
        for line in contents:
            
            f2.write(line+","+str(1)+"\n")