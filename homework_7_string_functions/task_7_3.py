# bolo, pirveli da shua asos dabechdva 5-jer

inputed_text = input("Please enter text here: ")

last = inputed_text[-1:]
first = inputed_text[:1]
length = len(inputed_text)

if length % 2 == 0:
    middle = inputed_text[(length//2-1):(length//2+1)]
else:
    middle = (inputed_text[(length//2)])

counter = 1
new_word = ""
while counter < 6:
    counter += 1
    new_word += last + first + middle  
    
print(new_word)
