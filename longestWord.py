def longest_word(file):
    with open(file,"r") as f:
        words=f.read().split()

    max_len=len(max(words,key=len))
    print(max_len)
    
    for i in words:
        if(len(i)==max_len):
            return i





print(longest_word("text.txt"))