# მიმდევრობის n-ური წევრის წინა წევრების დაბეჭდვა 0=<n<20 with gpt : )

# Function to print the Fibonacci-like sequence up to position n
def print_fibonacci_sequence(n):
    a, b = 0, 1  # Initialize the first two numbers
    
    if n >= 0:
        print(a, end=' ')  # Print the first number
    
    if n >= 1:
        print(b, end=' ')  # Print the second number
    
    count = 2  # Start from the third number
    while count <= n:
        a, b = b, a + b  # Update the values to the next pair in the sequence
        print(b, end=' ')  # Print the next number in the sequence
        count += 1

# User input
user_input = int(input("Enter a number (0 or higher): "))

# Print the Fibonacci sequence up to the given position n
if user_input >= 0:
    print(f"Fibonacci-like sequence up to position {user_input}:")
    print_fibonacci_sequence(user_input)
else:
    print("Please enter a non-negative number.")
