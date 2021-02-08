#Base Converter for Python
#This program converts a decimal integer into a string output in a different base

def convert(a, b):
    #a is number, b is base you want to convert it to
    baselist = []
    while a > 0:
        baselist.append(str(a%b))
        a = a//b
    baselist.reverse()
    baselist = ''.join(baselist)
    print(baselist)
    return baselist
