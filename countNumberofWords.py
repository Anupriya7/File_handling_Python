import string

d=dict()

def countWords(file):
    with open(file) as f:
        contents=f.read()
        contents=contents.strip()
        contents=contents.translate(contents.maketrans("","",string.punctuation))
        #contents.replace(","," ")
        print(contents)
        for i in contents:
            if (i in d and i!=""):
                d[i]=d[i]+1

            else:
                if(i!=" " and i!="\n"):
                    d[i]=1
    x=0
    print(d)
    for i in d.keys():
        x +=d[i]

    return x
        

        


print(countWords("abc.txt"))