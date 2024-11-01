# palindromi sityvebi



inputed_text = input("Please enter word or sentence: ").strip()

from re import sub

cleaned_text = sub(r'[^a-zA-Z]', '', inputed_text).lower()
if cleaned_text == cleaned_text[::-1]:
    print("Output: is palindrome")
else:
    print("Output: is not palindrome")