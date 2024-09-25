import random

array = [0 for x in range(20)]

for x in range(20):
    array[x] = random.randint(1,20)
print(array)
choice = int(input("Enter A Value to search: "))
i = 0
found = False
while found == False and i < 20:
    if choice == array[i]:
        print(f"The number {choice} is at location {i+1}")
        found = True
    else:
        i += 1

if found == False:
    print("Number Not Found !")