'''
*   File:       passgen.py
*   Author:     Adam Good
*   Version:    1.1
'''
import sys
import random

def main():
    """Script Starts Here"""
    argc = len(sys.argv)
    if argc < 5:
        print "Usage: passgen.py <min_password_length> <max_password_length> <number_of_passwords> <wordlist>"
        return

    min_pass_len = int(sys.argv[1])
    max_pass_len = int(sys.argv[2])
    number_of_passwords = int(sys.argv[3])
    word_list_file = open(sys.argv[4])

    word_list = [w.replace("\n", "").replace("'", "") for _, w in enumerate(word_list_file)]
    for i in range(number_of_passwords):
        password = gen_password(min_pass_len, max_pass_len, word_list)
        print str(i) + ".) " + password

def gen_password(min_pass_len, max_pass_len, word_list):
    """Generate A Password Based On Arguments"""
    password = ""

    list_len = len(word_list)
    while len(password) < min_pass_len:
        rand = random.randint(0, list_len-1)
        word = word_list[rand]
        password += word

        #TODO Find more effecient way of handling this
        if len(password) > max_pass_len:
            password = ""

    password = random_replace_cipher(password)

    return password

def random_replace_cipher(password):
    """Runs a replacement cipher on the password. Replacements are chosen at random"""

    # Literally just using "1337 Speak" for the replacements
    letters = ['a', 'e', 'l', 't', 's']
    numbers = ['4', '3', '1', '7', '5']

    # Currently it will replace between 1 and 3 of the letters.
    #TODO Maybe give user options to decide this
    for _ in range(1, 3):
        i = random.randint(0, len(letters)-1)
        letter = letters[i]
        number = numbers[i]

        password = password.replace(letter, number)

        letters.remove(letter)
        numbers.remove(number)

    return password

main()
