import random
import string

def generate_password(length):
    # Define possible character sets
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a password with the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        # Prompt the user to enter the desired password length
        length = int(input("Enter the desired password length: "))

        if length < 4:
            print("Password length should be at least 4 for better security.")
            return

        # Generate and display the password
        password = generate_password(length)
        print(f"Generated Password: {password}")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Run the program
if __name__ == "__main__":
    main()
