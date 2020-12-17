with open("sign2.jpg","rb") as rf:
    with open("sign_copy.jpg","wb") as wf:
        for line in rf:
            wf.write(line)