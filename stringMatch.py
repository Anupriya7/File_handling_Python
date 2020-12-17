import re

def stringMatch(file,s):
    with open(file,"r") as f:
        contents=f.readlines()
        for line in contents:
            if s in line:
                return True
        return False



print(stringMatch("text.txt","Python"))
