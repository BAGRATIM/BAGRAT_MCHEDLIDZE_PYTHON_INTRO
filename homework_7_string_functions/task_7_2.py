#მხოლოდ თანხმოვანების დაბეჭდვა

inputed_text = input("Please enter text here: ")

new_word = ""

for t in inputed_text:
    if t not in "aeiou" :
        new_word += t

print(new_word)