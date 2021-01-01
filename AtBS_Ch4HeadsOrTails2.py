print ('Automate the Boring Stuff Chapter 4 Coin Flip Streaks')

#Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails.
#This is a cleaned up version of the code with it now properly creating a list of 100 coin flips and seeing if there is a streak of 6 heads or tails inside and then iterating that 10000 times and counting how many lists have a streak of 6


import random
numberOfStreaks = 0



for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    fliplist = []
    streakcheck = 0
    for i in range(100):
        fliplist.append(random.randint(0,1))

    for flip in range(len(fliplist)):
        if flip<(len(fliplist)-6) and fliplist[flip] == fliplist[flip+1] and fliplist[flip] == fliplist[flip+2] and fliplist[flip] == fliplist[flip+3] and fliplist[flip] == fliplist[flip+4] and fliplist[flip] == fliplist[flip+5]:
            streakcheck =  1
    if streakcheck == 1:
        numberOfStreaks = numberOfStreaks + 1


    # Code that checks if there is a streak of 6 heads or tails in a row.
#print(fliplist)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))

#check total number of streaks  amounts
print('6 streak', numberOfStreaks)
