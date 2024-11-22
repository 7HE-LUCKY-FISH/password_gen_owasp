import string
import secrets
import random

def generate_password(length=12, num_special=2, num_numbers=2):
    """
    Generate a strong password following OWASP guidelines:
    - Minimum length of 12 characters
    - Mix of uppercase and lowercase letters
    - Include numbers and special characters
    """
    if length < 12:
        length = 12  # Enforce minimum length

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Ensure minimum requirements
    password = []
    password.extend(secrets.choice(uppercase) for _ in range(2))
    password.extend(secrets.choice(lowercase) for _ in range(2))
    password.extend(secrets.choice(digits) for _ in range(num_numbers))
    password.extend(secrets.choice(special) for _ in range(num_special))

    # Fill remaining length with random characters
    remaining = length - len(password)
    all_chars = uppercase + lowercase + digits + special
    password.extend(secrets.choice(all_chars) for _ in range(remaining))

    # Shuffle the password
    random.shuffle(password)
    return ''.join(password)

def main():
    site = input("Enter the site for which this password will be used: ")
    password = generate_password()
    print(f"Generated password for {site}: {password}")

    # Save the site and password to a text file
    with open("passwords.txt", "a") as file:
        file.write(f"{site}: {password}\n")

if __name__ == "__main__":
    main()
