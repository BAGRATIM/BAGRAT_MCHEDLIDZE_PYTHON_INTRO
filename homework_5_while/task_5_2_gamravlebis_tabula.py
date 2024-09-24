# გამრავლების ტაბულა 1-9

i = 1
while i < 10:
    j = 1
        
    while j < 10 and j<=i:
        print(f"{i}*{j} = {i*j}", end="   ")
        j = j +1
    print()
    i += 1