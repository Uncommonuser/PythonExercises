#Automate the Boring Stuff: Chapter 7 Practice Problem: Strong Password Detection
#Write a function that uses regular expressions to make sure the password string it is passed is strong.
#A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit.
#You may need to test the string against multiple regex patterns to validate its strength.

import re

def strongPword(password):
    detect = True
    printout = ['Your password is not strong.\n']
    #check length of password
    if len(password) < 8:
        detect = False
        printout.append('Please have at least 8 charaters. \n')
    #check password contains at least one digit
    if re.search('[0-9]', password) is None:
        detect = False
        printout.append('Please have at least one digit.\n')
    #check password has lower case letters
    if re.search('[a-z]', password) is None:
        detect = False
        printout.append('Password must have lower case letters.\n')
    #check password has uppercase
    if re.search('[A-Z]', password) is None:
        detect = False
        printout.append('Password must have uppercase letters.\n')
    #return fail or pass based on detect being false or true
    if detect == False:
        print('Password test for:', password, '\n', ' '.join(printout))
        return ' '.join(printout)
    else:
        print('Password is strong!')
        return 'Password is strong!'

strongPword('dog')
strongPword('Doggy')
strongPword('megabiscuits2')
strongPword('BIGFLUFFY')
strongPword('TheBestWaffles')
strongPword('1234tellmethatyouLOVEme')
