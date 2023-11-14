import random
import string

def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password using random.choices
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    # Get user input for password length
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Please enter a valid integer for the length.")
        return

    # Check if the length is a positive integer
    if length <= 0:
        print("Password length must be a positive integer.")
        return

    # Generate and display the password
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
