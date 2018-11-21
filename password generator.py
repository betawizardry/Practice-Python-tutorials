#password generator
# generates a random password for the user consisting of random Upper and lower
# case letters, numbers and symbols.
# password is between 8 and 14 characters long.
# python chr() function returns character ASCII number. keyboard characters
# useful for passwords are chr(33) to chr(126) inclusive.

#password length

def generate_password():
    import random
    pLength = random.randint(8,14)
    pword = ''
    for i in range(0,pLength):
        pword += chr(random.randint(33,126))
    return pword

generate_password()

