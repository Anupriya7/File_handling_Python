def reverse(file):

    with open(file,"r") as f:
        contents=f.readlines()
        print(f.tell())
        print(f.seek(0,1))
        #contents=contents.split("\n")
        contents=contents[::-1]
        contents=contents[:N]
        print(contents)
        #for i in range(0,3):
        contents=[i.replace("\n","") for i in contents]
        x="\n".join(contents)
            #print(contents[i])
        #print(contents)
        #x=" ".join(contents)
        return x



N=int(input())
print(reverse("text2.txt"))




