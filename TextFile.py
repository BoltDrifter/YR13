FileHandle = open("sample.txt", "w")
for i in range(100000):
    FileHandle.write(f"{i}\n")


FileHandle.close()