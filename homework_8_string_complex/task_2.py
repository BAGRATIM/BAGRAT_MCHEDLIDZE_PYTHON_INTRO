# erti styivs asoebit meore sityvis migeba

inputed_text1 = input("Please enter word1: ")
inputed_text2 = input("Please enter word2: ")


i = 0
result = True 

while i < len(inputed_text2):
    char = inputed_text2[i]
    
    # ვამოწმებთ არის თუ არა სიმბოლო str1-ში
    if char in inputed_text1:
        # ვშლით პირველივე სიმბოლოს გამოჩენას str1-დან
        inputed_text1 = inputed_text1.replace(char, '', 1)
    else:
        result = False  # თუ სიმბოლო არ მოიძებნა, ვსვამთ False-ს და ვწყვეტთ ციკლს
        break
    
    i += 1

if result:
    print("YES")
else:
    print ("NO")