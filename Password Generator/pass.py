import random
import string


def generate_password(min_length, numbers=True, special_chars=True):
    # Character sets
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # Create initial character set
    char_set = letters
    if numbers:
        char_set += digits
    if special_chars:
        char_set += special

    # Ensure the password meets the minimum length
    if min_length < 1:
        raise ValueError("Minimum length must be at least 1")

    # Generate a random password
    password = []

    # Ensure at least one number if required
    if numbers:
        password.append(random.choice(digits))
    # Ensure at least one special character if required
    if special_chars:
        password.append(random.choice(special))

    # Fill the rest of the password to meet the minimum length
    while len(password) < min_length:
        password.append(random.choice(char_set))

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    # Convert list to string and return
    return ''.join(password)


min_password_length = int(input("Enter minimum length of password: "))
has_number = input("Do you want to have numbers? (y/n)").lower() == "y"
has_specials = input("Do you want to have special characters? (y/n)").lower() == "y"
generated_password = generate_password(min_password_length, has_number, has_specials)
print(f"The Generated Password is: {generated_password}")
