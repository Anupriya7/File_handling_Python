#def readnlines(n):
with open("text_copy.txt","a") as f:

        #size_to_read=n
    fcontents=f.write("hi")
        #print(len(fcontents))
    print(fcontents)

with open("text_copy.txt","r") as rd:
    fcontents=rd.read()
    print(fcontents)




#n=int(input())
#readnlines(n)