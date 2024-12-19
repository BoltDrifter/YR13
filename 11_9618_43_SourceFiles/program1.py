def IterativeVowels(Value):
    Total = 0
    StringLength = len(Value)
    for x in range(StringLength):
        FirstCharacter = Value[0].lower().strip()
        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u':
            Total = Total + 1
        Value = Value[1:len(Value)] 
    return Total

print(IterativeVowels("house"))