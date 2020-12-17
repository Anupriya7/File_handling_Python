def count_words(filepath):
   with open(filepath) as f:
       data = f.read()
       contents=data.replace(",", " ")
       print(contents)

       return len(data.split(" "))+1
print(count_words("abc.txt"))