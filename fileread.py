
def readnlines(n):
    with open("text_copy.txt","r") as f:

        size_to_read=n
        fcontents=f.read(size_to_read)
        print(fcontents)

        while(len(fcontents)>0):
            print(fcontents,end="*")
            fcontents=f.read(size_to_read)

        



n=int(input())
readnlines(n)