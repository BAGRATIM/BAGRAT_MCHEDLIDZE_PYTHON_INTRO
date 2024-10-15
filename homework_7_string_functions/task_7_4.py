# klaviaturis wanacvleba 1-it

keyboard_left =  "qwertyuiopasdfghjklzxcvbnm"
keyboard_right = "wertyuiopqsdfghjklaxcvbnmz"

keyboard_left_rev =  "wertyuiopqsdfghjklaxcvbnmz"
keyboard_right_rev = "qwertyuiopasdfghjklzxcvbnm"

input_action = input("Enter action (e/d): ").lower()
inputed_text = input("Enter text: ").lower()


if input_action == "d":
    translation_table = str.maketrans(keyboard_right, keyboard_left)
elif input_action == "e":
    translation_table = str.maketrans(keyboard_left, keyboard_right)
else:
    print("Invalid action, please enter 'e' or 'd'.")
    exit(1)

# Apply translation to the inputed text
output_word = inputed_text.translate(translation_table)
print(output_word)
