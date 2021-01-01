print ('Automate the Boring Stuff Chapter 4 Comma Code')

#Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item.

testlist1 = ['apples', 'bannanas', 'tofu', 'cats']
testlist2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
testlist3 = []

def commacode(alist):
    if len(alist) > 0:
        andlist = ['and']
        newlist = alist[:-1] + andlist + alist[-1:]
        stringlist = ', '.join(newlist)
        print(stringlist)
    else:
        print('This list is empty!')
    pass

commacode(testlist1)
commacode(testlist2)
commacode(testlist3)
