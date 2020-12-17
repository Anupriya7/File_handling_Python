import string
d=dict()
with open("strig.txt","r") as f:

    contents=f.readlines()

    for line in contents:
        line=line.lower()
        line=line.strip()
        line=line.translate(line.maketrans("","",string.punctuation))
        #print(line)
        words=line.split(" ")
        for word in words:
            if word in d:
                d[word]=d[word]+1

            else:
                d[word]=1

    for key in list(d.keys()):
        print(key,d[key])

    
