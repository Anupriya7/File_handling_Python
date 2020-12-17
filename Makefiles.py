import os,string

if not os.path.exists("letters"):
    os.makedirs("letters")

for letter in string.ascii_lowercase:
    with open(letter+".txt","w") as f:
        f.writelines(letter)