import glob
l=[]
files_list=glob.glob("*.txt")
for line in files_list:
    with open(line,"r") as f:
        l.append(f.read())


print(l)