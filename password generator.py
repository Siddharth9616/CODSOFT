import random
import string

def generate_password(min_length, number=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters
    if number:
        characters += digits
    if special_characters:
        characters += special

    pwd = []
    meet_criteria = False
    has_number = False
    has_special = False

    while len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd.append(new_char)

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

    if number and not has_number:
        pwd.append(random.choice(digits))
    if special_characters and not has_special:
        pwd.append(random.choice(special))

    random.shuffle(pwd)

    return ''.join(pwd)

min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
print("The generated password is: ", pwd)
