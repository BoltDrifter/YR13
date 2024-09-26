Array = [7,12,19,23,27,33,37,41,45,56,59,60,62,71,80,84,88,92,99]
MaxItems = len(Array)

Found = False
SearchFailed = False
First = 0
Last = MaxItems - 1

SearchItem = int(input("Enter the number you want to search: "))

while Found == False and SearchFailed == False:
    Middle = (First + Last) / 2
    if Array[int(Middle)] == SearchItem:
        Found = True
    elif First >= Last:
        SearchFailed = True
    elif Array[int(Middle)] > SearchItem:
        Last = int(Middle) - 1
    elif Array[int(Middle)] < SearchItem:
        First = int(Middle) + 1
if Found == True:
    print(f"The number was found at location {int(Middle) + 1 }  ")
else:
    print("Number not in Array !") 



