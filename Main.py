#MichaelNyembo, Fri 9 Aug 12:55
import string

def password_Checker():
    password = input("Enter the password to be checked: ")

    if len(password) == 0:
        print("The input should not be empty")
        return

    length = len(password)
    has_upperCase = any(char.isupper() for char in password)
    has_lowerCase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_punctuation = any(char in string.punctuation for char in password)

    strength = 0
    if 12 <= length <= 16:
        strength += 1

    if has_lowerCase:
        strength += 1
    if has_upperCase:
        strength += 1
    if has_digit:
        strength += 1
    if has_punctuation:
        strength += 1

    if strength <= 2:
        print("This password is Weak")
    elif strength <= 3:
        print("This password is Moderate")
    elif strength == 4:
        print("This password is Strong")
    else:
        print("This password is Very Strong")
quit = ""
while quit != "q":
    password_Checker()
    quit = input("Click 'q' to quit or press any other key to continue: ")
rd = input("Click q to quit or Click any Button to Continue")