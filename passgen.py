'''
*   File:       passgen.py
*   Author:     Adam Good
*   Version:    1.0
'''
import sys
import random
import string

wordList = []
listLen = 0

def main():
    global wordList
    global listLen

    if len(sys.argv) < 5:
        print "Usage: passgen.py <min_password_length> <max_password_length> <number_of_passwords> <wordlist>"
        return
    # Initialize some important variables
    minPassLen = int(sys.argv[1])
    maxPassLen = int(sys.argv[2])
    passNum = int(sys.argv[3])      # Number of passwords
    wordfile = open(sys.argv[4])

    # Read the wordlist file into a list of words without the \n
    wordList = [w.replace('\n', '') for _,w in enumerate(wordfile)]
    listLen = len(wordList)

    # This loop generates each password
    for i in range(0, passNum):
        password = genPassword(minPassLen, maxPassLen)
        print(str(i+1) + ".) " + str(password))

# This function actually generates the passwords
def genPassword(minPassLen, maxPassLen):
    # These are the global variables of our list and its length
    global wordList
    global listLen

    # Prep our variables
    password = ""
    minPassLen = minPassLen - 5 # For 5 character salt
    maxPassLen = maxPassLen - 5

    # While the password is too short keep adding words to the password
    while len(password) < minPassLen:
        # Generate a random number to grab a random word and append it to password
        r = random.randint(0, listLen)
        password += wordList[r].replace("'", '')
        password += "_" # These are to help memorization by making it more readable
        # If the password is too long try again.
        # TODO detect this earlier so we don't have to gen an entire new password
        if len(password) > maxPassLen:
            password = ""
    # Append additional 5 char salt to the end for 26^5 extra combinations
    password += genSalt()
    # Add 2 new rules to our password; e.g. 'a' = '4' or 'y' = 'Y'
    password = randomRule(password)
    return password

# This function just generates a 5 character salt from uppercase alphabet
def genSalt():
    salt = ""
    for i in range(0, 5):
        r = random.randint(0, 25)
        salt += string.ascii_uppercase[r]
    return salt

# This function just changes 2 characteristics of the password.
# TODO make this slightly more complicated
def randomRule(password):
    for x in range(0, 2):
        # Get a random letter and implement its specific rule
        i = random.randint(0, 25)
        if string.ascii_lowercase[i] == 'a':
            password = password.replace('a', '4')
        elif string.ascii_lowercase[i] == 'e':
            password = password.replace('e', '3')
        elif string.ascii_lowercase[i] == 'l':
            password = password.replace('l', '1')
        elif string.ascii_lowercase[i] == 't':
            password = password.replace('t', '7')
        elif string.ascii_lowercase[i] == 's':
            password = password.replace('s', '5')
        else:
            password = password.replace(string.ascii_lowercase[i], string.ascii_uppercase[i])
    return password

main()