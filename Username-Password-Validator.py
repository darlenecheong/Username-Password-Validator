import random
import string

#function: display_username_requirements
#output: prints all requirements for a valid username
def display_username_requirements():
    print("\nUsername Requirements:")
    print("- Must be between 8 and 15 characters long.")
    print("- Must contain at least one uppercase letter.")
    print("- Must contain at least one lowercase letter.")
    print("- Must contain at least one digit.")
    print("- Cannot start or end with a digit.")
    print("- Must be alphanumeric (letters and digits only).")

#function: display_password_requirements
#output: prints all requirements for a valid password
def display_password_requirements():
    print("\nPassword Requirements:")
    print("- Must be at least 8 characters long.")
    print("- Cannot contain the username.")
    print("- Must contain at least one uppercase letter.")
    print("- Must contain at least one lowercase letter.")
    print("- Must contain at least one digit.")
    print("- Must contain at least one special character (#, $, %, &, etc.).")
    
    
#function: valid_username
#input: username entered by user (string)
#processing: validate username with rules
#output: return whether or not username is valid

#1. create function valid_username
def valid_username(username):

    #create accumulators to track uppercase characters, lowercase characters and numbers 
    uppercase_counter = 0
    lowercase_counter = 0
    digits_counter = 0

    #set variable of digits
    digits = "0123456789"

    #iterate over username to check for uppercase characters, lowercase characters and numbers 
    for c in username:
        if c.islower() == True:
            lowercase_counter += 1
        elif c.isupper() == True:
            uppercase_counter += 1
        elif c.isdigit() == True:
            digits_counter += 1

    #print length of username
    print("* Length of username:", len(username))

    #print whether or not username is alpha-numeric
    print("* All characters are alpha-numeric:", username.isalnum())

    #print whether or not the first and last characters of the username are not digits
    if (username[0] in digits) or (username[-1] in digits):
        print("* First & last characters are not digits: False")
    else:
        print("* First & last characters are not digits: True")
    
    #print # of uppercase letters in username
    print("* # of uppercase characters in the username:", uppercase_counter)

    #print # of lowercase letters in username
    print("* # of lowercase characters in the username:", lowercase_counter)

    #print # of digits in username
    print("* # of digits in the username:", digits_counter)

    #if length of username does not match requirement, return invalid message
    if len(username) < 8 or len(username) > 15:
        return "Username is invalid, please try again"

    #if username is not alpha numeric, return invalid message    
    elif username.isalnum() == False:
        return (uppercase_counter, lowercase_counter, digits_counter, "Username is invalid, please try again")

    #if first or last character is a digit, return invalid message
    elif username[0].isdigit() == True or username[-1].isdigit() == True:
        return "Username is invalid, please try again"

    #if there are no uppercase, return invalid message
    elif uppercase_counter < 1:
        return "Username is invalid, please try again"

    #if there are no lowercase, return invalid message
    elif lowercase_counter < 1:
        return "Username is invalid, please try again"

    #if there are no digits, return invalid message
    elif digits_counter < 1:
        return "Username is invalid, please try again"

    #return valid message if all these requirements are met
    else:
        return "Username is valid!"



#main program - username

#display username requirements
display_username_requirements()

while True:
    username = input("Enter a username: ")
    output = valid_username(username)

    if output == "Username is invalid, please try again.":
        print(output)
        print()
        continue
    else:
        print(output)
        break
print()


#function: valid_password
#input: password entered by user (string)
#processing: validate password with rules
#output: return whether or not password is valid

#2. create function valid_password
def valid_password(password, username):

    #create accumulators to track uppercase, lowercase, digits and special characters
    uppercase_counter = 0
    lowercase_counter = 0
    digits_counter = 0
    spec_characters_counter = 0

    #set variable for special characters and digits
    special_characters = "#$%&"
    digits = "0123456789"

    #iterate over password to check for uppercase characters, lowercase characters, digits, and special characters
    for c in password:
        if c in digits:
            digits_counter += 1
        elif c in special_characters:
            spec_characters_counter += 1
        elif c.islower() == True:
            lowercase_counter += 1
        elif c.isupper() == True:
            uppercase_counter += 1
        
    #print length of password
    print("* Length of password:", len(password))

    #print whether username is part of password
    if username in password:
        print("* Username is part of password: True")
    else:
        print("* Username is part of password: False")

    #print # of uppercase letters in password
    print("* # of uppercase characters in the password:", uppercase_counter)

    #print # of lowercase letters in password
    print("* # of lowercase characters in the password:", lowercase_counter)

    #print # of digits in password
    print("* # of digits in the password:", digits_counter)

    #print # of special characters in password
    print("* # of special characters in the password:", spec_characters_counter)
    
    #if length of password does not match requirement, return invalid message
    if len(password) < 8:
        return "Password is invalid, please try again."

    #if username is in password, return invalid message    
    elif username in password:
        return "Password is invalid, please try again."

    #if there are no special characters in password, return invalid message
    elif spec_characters_counter < 1:
        return "Password is invalid, please try again."

    #if there are no uppercase in password, return invalid message
    elif uppercase_counter < 1:
        return "Password is invalid, please try again."

    #if there are no lowercase in password, return invalid message
    elif lowercase_counter < 1:
        return "Password is invalid, please try again."

    #if there are no digits in password, return invalid message
    elif digits_counter < 1:
        return "Password is invalid, please try again."

    #return valid message if all these requirements are met
    else:
        return "Password is valid!"


#function: password_generator
#input: password entered by user (string)
#processing: generates a random valid password
#output: returns valid password
def password_generator(username, password):
    #store all lowercase letters as a string
    lowercase_letters = string.ascii_lowercase
    
    #store all uppercase letters as a string
    uppercase_letters = string.ascii_uppercase

    #set variable for special characters and digits
    special_characters = "#$%&"
    digits = "0123456789"

    #create variable for all valid letters and digits
    allvalid = lowercase_letters + uppercase_letters + special_characters + digits

    # Ensure password is at least 8 characters long
    while len(password) < 8:
        password += random.choice(allvalid)

    # Ensure password does not contain the username
    while username in password:
        username_pos = password.find(username)
        password = password[:username_pos] + random.choice(allvalid) + password[username_pos + len(username):]

    # Ensure at least one uppercase letter
    if not any(c.isupper() for c in password):
        password += random.choice(uppercase_letters)

    # Ensure at least one lowercase letter
    if not any(c.islower() for c in password):
        password += random.choice(lowercase_letters)

    # Ensure at least one digit
    if not any(c.isdigit() for c in password):
        password += random.choice(digits)

    # Ensure at least one special character
    if not any(c in special_characters for c in password):
        password += random.choice(special_characters)

    # Shuffle the password to avoid predictable patterns
    password = ''.join(random.sample(password, len(password)))

    return password


#main program - password

#display password requirements
display_password_requirements()

while True:
    password = input("Enter a password: ")
    output = valid_password(password, username)

    if output == "Password is invalid, please try again.":
        print(output)
        print()
        fix = input("Would you like us to generate a random password for you? (yes/no) ")
        if fix.lower() == "yes":
            password = password_generator(username, password)
            print("Random password generated:", password)
        else:
            continue
    else:
        print(output)
        break
