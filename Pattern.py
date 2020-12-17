
def Pattern(n):
    with open("Pattern.txt","w") as f:
        for i in range(1,n+1):
            for j in range(1,i+1):
                f.write(str(j))
                #f.write("%s\n"%i)

            for j in range(i-1,0,-1):
                f.write(str(j))
            
            f.write("\n")
                #print()




Pattern(3)

