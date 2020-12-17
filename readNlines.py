def filel(N):

    with open("text2.txt","r") as f:
        #size_to_read=N
        contents=f.readlines()
        #print(contents)
        for i in range(N,0):
            print(contents[i])



N=int(input())
filel(N)