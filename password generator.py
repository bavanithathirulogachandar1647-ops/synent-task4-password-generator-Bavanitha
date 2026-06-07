import random
import string

def generate_password(length):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    special = string.punctuation

    all_characters = uppercase + lowercase + numbers + special

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(numbers),
        random.choice(special)
    ]

    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    return ''.join(password)

try:
    length = int(input("Enter password length: "))

    if length < 4:
        print("Password length must be at least 4.")
    else:
        password = generate_password(length)
        print("\nGenerated Password:")
        print(password)

except ValueError:
    print("Please enter a valid number.")