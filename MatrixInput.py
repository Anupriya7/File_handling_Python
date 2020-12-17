def MatrixInput(file):
    with open(file,"r") as f:
        contents=f.readlines()

        l=[]

        for line in contents:

            temp=line.split()
            #for i in temp:
            #l.append(int(temp))
            r=[]
            for i in temp:
                r.append(int(i))

            l.append(r)


        for i in range(len(l)):
            for j in range(0,i):
                l[i][j],l[j][i]=l[j][i],l[i][j]

        
        writeX(l)

        

def writeX(lines):       
    with open("output.txt","w") as fw:
        wlines=[]
        for i in range(len(lines[0])):
            for j in range(len(lines)):
                
                lines[i][j]=str(lines[i][j])
                print(lines[i][j])

        for i in lines:
            wlines.append(" ".join(i))
        print(wlines)


        for line in wlines:
            fw.writelines(line)

    #return lines


MatrixInput("matrix.txt")

