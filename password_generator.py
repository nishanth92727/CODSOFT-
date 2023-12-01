import random
import string

def generate_password(length, complexity):
    characters = ''
    
    if 'uppercase' in complexity:
        characters += string.ascii_uppercase
    if 'lowercase' in complexity:
        characters += string.ascii_lowercase
    if 'digits' in complexity:
        characters += string.digits
    if 'punctuation' in complexity:
        characters += string.punctuation

    if not characters:
        print("Invalid complexity selection. Please choose at least one option.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Ask the user for the desired length of the password
    while True:
        try:
            password_length = int(input("Enter the desired length of the password: "))
            if password_length <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Ask the user for the desired complexity of the password
    while True:
        complexity_options = ['uppercase', 'lowercase', 'digits', 'punctuation']
        complexity = input("Enter the desired complexity (comma-separated options - uppercase, lowercase, digits, punctuation): ").lower().split(',')
        
        if all(option in complexity_options for option in complexity):
            break
        else:
            print("Invalid complexity selection. Please choose from the available options.")

    # Generate the password
    password = generate_password(password_length, complexity)

    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()

