file = open(r"File Handling\names.txt","r")
newfile  = open(r"File Handling\NewNames.txt", "w")

def Extract(file,NewFile):
    x = file.readline().replace('for',"")
    y = x.split()
    NewString = ""
    for i in range(len(y)):
        z = y[i]
        NewString = NewString + z[0]
    print(NewString)
    NewString = NewString + "\n"
    NewFile.write(NewString)

Extract(file,newfile)
Extract(file,newfile)

file.close()
newfile.close()