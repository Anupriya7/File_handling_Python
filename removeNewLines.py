import os

with open("text2.txt","r") as f:
    contents=f.readlines()
    contents=os.remove("\n")
    print(contents)