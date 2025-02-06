# Function to check if a character is uppercase or lowercase
def check_case(char):
    if char.isupper():
        return "The character is an uppercase letter."
    elif char.islower():
        return "The character is a lowercase letter."
    else:
        return "The character is not an alphabet letter."

# Input character
char = input("Enter a character: ")

# Check and display the result
result = check_case(char)
print(result)
