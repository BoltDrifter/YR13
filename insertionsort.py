n = int(input("How many items in the list: "))
array = [0 for i in range(n)]


for i in range(len(array)):
    number = int(input("Enter Number: "))
    array[i] = number


Pointer = 0
NumberofItems = len(array)

for i in range(NumberofItems - 1):
    ItemToInsert = array[i]
    CurrentItem = i - 1
    while (array[CurrentItem] > ItemToInsert ) and (CurrentItem > -1):
        array[CurrentItem + 1] = array[CurrentItem]
        CurrentItem = CurrentItem - 1
    array[CurrentItem + 1] = ItemToInsert
    print(array)
print(array)