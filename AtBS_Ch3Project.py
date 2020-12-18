print ('Automate the Boring Stuff Chapter 3 Project')
#The Collatz Sequence
#Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1.
#Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1. (Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)

number = input("Please input an integer number:", )


def collatz(number):
    try:
        number = int(number)
        while number > 1:
            if number%2 == 0:
                #print("Even")
                number = number//2
                print(number)
            elif number %2 ==1:
                #print("Odd")
                number = 3*number+1
                print(number)
    except:
        print("Sorry that is not an integer number")

collatz(number)
