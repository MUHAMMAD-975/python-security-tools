# PASSWORD GENERATOR MODULE

import random
import string

# generate_password()
def generate_password():
    # Ask user for length
    length_input = input("Enter password length: ")

    # Convert to integer safely
    try:
        length = int(length_input)
    except ValueError:
        print("Please enter a valid number.")
        return None  # invalid input

    # Validate length
    if length < 8:
        print("Password must be at least 8 characters.")
        return None  # too short

    elif length > 64:
        print("Password cannot be more than 64 characters.")
        return None  # too long

    else:
        # VALID LENGTH → generate password here
        # (character sets, loop, random picks)

        # Create character set (letters, digits, symbols)
        characters = string.ascii_letters + string.digits + string.punctuation

        # Build the password step by step
        password = ""
        for i in range(length):
            password += random.choice(characters)

        # Return the final password to main.py
        return password
