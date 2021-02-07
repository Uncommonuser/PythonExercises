#Automate the Boring Stuff: Chapter 7 Practice Problem: Regex Version of the strip() Method
#Write a function that takes a string and does the same thing as the strip() string method.
#If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string.
#Otherwise, the characters specified in the second argument to the function will be removed from the string.

import re
#can't figure out a way to strip both sides at once so made it strip front and back separately.
def regstrip(string, arg = ' '):
    print('Stripping:', arg)
    front = '^' + arg
    back = arg + '$'
    stripfront = re.compile(front)
    stripback = re.compile(back)
    strippedfront = stripfront.sub('', string)
    strippedboth = stripback.sub('',strippedfront)
    print(strippedboth)
    return strippedboth

regstrip('Test')
regstrip(' Test ')
regstrip('hhHellohh', 'h')
regstrip('hhHellohh', 'hh')
