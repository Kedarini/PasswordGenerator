import random
import string

# Ask for password length
length = int(input("How long you want your password to be? min 5: "))

# Ask about special characters
specialcharacters = input("Do you want password to contain special characters? (Y/N): ")

# Define character sets
letters = string.ascii_letters   # a-z + A-Z
digits = string.digits           # 0-9
specials = string.punctuation    # !@#$%^&* etc.

# Build the pool of characters
characters = letters + digits
if specialcharacters.strip().upper() == "Y":
    characters += specials

# Generate password
password = ''.join(random.choice(characters) for _ in range(length))

print("Your password is:", password)