import csv
import string

def FrequencyWords(file):
    with open("abc.txt","r") as f:
        d=dict()
        contents=f.read()
        contents=contents.split()
        
        for line in contents:
            line=line.translate(line.maketrans("","",string.punctuation))
            if line in d:
                d[line]=d[line]+1

            else:
                d[line]=1

    print(d)

    csvWrite(d)


def csvWrite(d):
    with open("file.csv","w") as f:
        f.write("words,frequency\n")
        for line in d:
            f.write(line+","+str(d[line])+"\n")



# def csvWrite(dict):
#     with open("new_dict.csv","w") as c:
#         field_names=['words','frequency']
#         csv_writer=csv.DictWriter(c,fieldnames=field_names)

#         csv_writer.writeheader()

#         for line in dict:
#             #del line['email']
#             #print(type(line))
#             #rint(line)
#             toWrite={"words":line,"frequency":dict[line]}
            

#             csv_writer.writerow(toWrite)




FrequencyWords("abc.txt")


