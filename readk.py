with open("abc.txt","r") as f:
    f.seek(3,0)
    print(f.fileno)
    #f.truncate(10)
    contents=f.readlines(10)
    print(contents)
    print(f.closed) 
    print(f.encoding) 
    print(f.mode) 
    print(f.newlines) 
    print(f.softspace)  