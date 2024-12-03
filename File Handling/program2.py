file = open(r"File Handling\paragraph.txt", "r")

ask = input("Enter the word you want to replace: ")
ask2 = input("Enter the word you want to replace with: ")

x = file.readline().lower().strip().replace(ask,ask2)
print(x)

file.close()