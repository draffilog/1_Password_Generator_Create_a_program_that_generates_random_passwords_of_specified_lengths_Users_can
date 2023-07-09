Sure! Here's an example of how you can create a password generator program in Python:

```python
import random
import string

def generate_password(length, include_letters=True, include_numbers=True, include_symbols=True):
    characters = []
    
    if include_letters:
        characters.extend(string.ascii_letters)
    if include_numbers:
        characters.extend(string.digits)
    if include_symbols:
        characters.extend(string.punctuation)
    
    if not characters:
        print("Error: Please select at least one character type.")
        return
    
    if length < 1:
        print("Error: Password length should be at least 1.")
        return
    
    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    print("Welcome to the Password Generator!")
    print("---------------------------------")
    
    length = int(input("Enter the desired length of your password: "))
    include_letters = input("Include letters (y/n)? ").lower() == 'y'
    include_numbers = input("Include numbers (y/n)? ").lower() == 'y'
    include_symbols = input("Include symbols (y/n)? ").lower() == 'y'
    
    password = generate_password(length, include_letters, include_numbers, include_symbols)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
```

In this program, the `generate_password` function takes in the desired length of the password and the options for including letters, numbers, and symbols. It then creates a list of characters based on the user's selections. If the user does not select any character type, an error message is displayed.

The function then checks if the provided password length is at least 1. If it's less than 1, an error message is displayed.

If all inputs are valid, the function uses `random.choices` to generate a random password of the specified length using the characters list. The generated password is then returned.

In the `main` function, the program prompts the user for the desired password length and the character types to include. It converts the input to lowercase and checks if it's 'y' to include that character type.

Finally, the `generate_password` function is called with the provided inputs, and the generated password is printed to the console.

You can modify this example or add more features to suit your needs.