#Algorithm reduction function in multiple bases
#1) Start with a random number n, which is a nonnegative integer of length k in base b
#2) Define x and y as integers of length k.  x has the digits of n in descending order, and y has the digits of n in ascending order
#3) Define z = x - y.  Add leading zeros to z to maintain length k if necessary
#4) Assign n = z to get the next number n, and go back to step 2

#base converter function that returns a string of the number in that base
def convert(a, b):
    #a is number, b is base you want to convert it to
    baselist = []
    while a > 0:
        baselist.append(str(a%b))
        a = a//b
    baselist.reverse()
    baselist = ''.join(baselist)
    return baselist

def solution(n, b = 10):
    #running list of values
    thelist = ['0']
    n = str(n)
    #length of integer
    k = len(n)
    loop = 0
    #loop until a n is found in list
    while n not in thelist:
        thelist.append(n)
        #length of integers in ascending order
        x = list(n)
        x.sort(reverse=True)
        x = ''.join(x)
        #print('x now is', x)
        #convert x into base 10 for math
        x = int(x, b)

        #length of integers in descending order
        y = list(n)
        y.sort()
        y = ''.join(y)
        #print('y now is', y)
        #convert y into base 10 for math
        y = int(y, b)

        #z is the difference plus leading zeros to maintain k length
        z = x - y

        #convert z back into original base to add leading 0s and append to list
        z = convert(z, b)
        if len(z) < k:
           z =('0' * (k - len(z))) + z
        #set n to z
        n = z
        loop = loop + 1
        #print('n now is', n)
    #determine the length of the cycle which is the index position of n minus length of list
    thelist.pop(0)
    cycle = len(thelist) - thelist.index(n)
    #print(thelist.index(n))
    print('Length of cycle', cycle)
    print('Done!', thelist )
    return cycle

#solution(5221231)
#solution(1211)
solution(210022, 3)
