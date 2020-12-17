def LastNlines(fname): 
    # opening file using with() method 
    # so that file get closed 
    # after completing work 
    with open(fname,"r") as file: 
          
        # loop to read iterate  
        # last n lines and print it 
        for line in (file.read() [::-1]): 
            print(line, end ='') 
  
  
# Driver Code:  
if __name__ == '__main__': 
    fname = 'text.txt'
    N = 3
    try: 
        LastNlines(fname) 
    except: 
        print('File not found')