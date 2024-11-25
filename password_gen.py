import string
import secrets
import random

def get_password_requirements():
    """Get password requirements from user input"""
    while True:
        try:
            length = int(input("Enter desired password length (minimum 12): "))
            if length < 12:
                print("Password length must be at least 12 characters.")
                continue
                
            print("\nChoose password complexity:")
            print("1. Basic (letters only)")
            print("2. Medium (letters + numbers)")
            print("3. Strong (letters + numbers + special characters)")
            complexity = int(input("Enter complexity level (1-3): "))
            
            if complexity not in [1, 2, 3]:
                print("Please choose a valid complexity level (1-3)")
                continue
                
            if complexity >= 2:
                num_numbers = int(input("Enter number of digits to include: "))
            else:
                num_numbers = 0
                
            if complexity == 3:
                num_special = int(input("Enter number of special characters to include: "))
            else:
                num_special = 0
                
            return length, num_special, num_numbers
            
        except ValueError:
            print("Please enter valid numbers.")

def generate_password(length=12, num_special=2, num_numbers=2):
    """Generate a password based on user requirements"""
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Ensure minimum requirements
    password = []
    password.extend(secrets.choice(uppercase) for _ in range(2))
    password.extend(secrets.choice(lowercase) for _ in range(2))
    
    if num_numbers > 0:
        password.extend(secrets.choice(digits) for _ in range(num_numbers))
    if num_special > 0:
        password.extend(secrets.choice(special) for _ in range(num_special))

    # Fill remaining length with random characters
    remaining_length = length - len(password)
    if remaining_length > 0:
        all_chars = lowercase + uppercase
        if num_numbers > 0:
            all_chars += digits
        if num_special > 0:
            all_chars += special
        password.extend(secrets.choice(all_chars) for _ in range(remaining_length))

    # Shuffle the password list
    random.shuffle(password)
    return ''.join(password)

def main():
    site = input("Enter the site for which this password will be used: ")
    length, num_special, num_numbers = get_password_requirements()
    password = generate_password(length, num_special, num_numbers)
    print(f"\nGenerated password for {site}: {password}")

    # Save to file
    with open("passwords.txt", "a") as file:
        file.write(f"{site}: {password}\n")
    print("Password has been saved to passwords.txt")

if __name__ == "__main__":
    main()
