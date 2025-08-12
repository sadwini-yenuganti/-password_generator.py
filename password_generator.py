import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print(" Password Generator")
    
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print(" Password length must be greater than 0.")
        else:
            print("Generated Password:", generate_password(length))
    except ValueError:
        print("Please enter a valid number.")
