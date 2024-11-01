# with GPT : )

def generate_sequence(n):
    sequence = [0, 1]  # Initialize with 0 and 1
    for i in range(2, n):
        next_value = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_value)
    return sequence

# Generate the sequence with 20 numbers
sequence = generate_sequence(20)

# User input
user_input = int(input("Enter a number (0 to 19): "))

# Print the number from the sequence
if 0 <= user_input < 20:
    print(f"Number at position {user_input} is {sequence[user_input]}")
else:
    print("Please enter a number between 0 and 19.")
