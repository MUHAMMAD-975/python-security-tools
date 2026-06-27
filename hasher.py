# PASSWORD HASHING MODULE

import hashlib
import os
import base64

# hash_password_with_salt()
def hash_password_with_salt():
    # Ask the user for a password to hash
    password = input("Enter a password to hash: ")

    # Generate a cryptographically secure random salt (16 bytes)
    salt = os.urandom(16)

    # Convert salt to Base64 for readability
    salt_b64 = base64.b64encode(salt).decode()

    # Combine password + salt
    combined = password.encode() + salt

    # Hash the combined value using SHA-256
    hash_value = hashlib.sha256(combined).hexdigest()

    # Return both the salt and the final hash to main.py
    return salt_b64, hash_value