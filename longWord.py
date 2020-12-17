with open("text.txt", "r") as f:
    contents=f.read()
    contents=contents.split()
    max_len=len(contents[0])
    print(max_len)
    for i in contents[1:]:
        if max_len<len(i):
            max_len=len(i)

    print(max_len)
