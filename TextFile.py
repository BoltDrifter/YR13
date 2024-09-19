FileHandle = open("sample.txt", "w")
for i in range(1,11):
    ask = input("Enter a Subject: ")
    FileHandle.write(f"Subject {i}: {ask}\n")


FileHandle.close()


FileHandleRead = open("sample.txt", "r")

ThisLine = FileHandleRead.readline()
while len(ThisLine) > 0:
    ThisLine = FileHandleRead.readline()
    print(ThisLine)
FileHandleRead.close()