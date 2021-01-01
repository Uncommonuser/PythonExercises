print ('Automate the Boring Stuff Chapter 4 Coin Flip Streaks')

#Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails.
#The first time I did this I interpreted the question as building a program to just flip a coin 10000 times and count the number of streaks of at at least 6, not flip a coin 100 times and do that 10000 times to see how often a streak of 6 appears in each 100 fliplist
#This code is also messy in the way it appends results of the coin flips indirectly to the flip list
#I made multiple streak counters just to see how many streaks there would be. 

import random
numberOfStreaks = 0
numberOfStreaks2 = 0
numberOfStreaks3 = 0
numberOfStreaks4 = 0
fliplist = []

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flip = random.randint(0,1)
    if  flip == 0:
        fliplist.append(0)
    else:
        fliplist.append(1)
for flip in range(len(fliplist)):
    if flip<(len(fliplist)-6) and fliplist[flip] == fliplist[flip+1] and fliplist[flip] == fliplist[flip+2] and fliplist[flip] == fliplist[flip+3] and fliplist[flip] == fliplist[flip+4] and fliplist[flip] == fliplist[flip+5]:
        numberOfStreaks = numberOfStreaks + 1

   #code to check for streaks of other amounts of heads or tails
    if flip<(len(fliplist)-2) and fliplist[flip] == fliplist[flip+1]:
        numberOfStreaks2 = numberOfStreaks2 + 1

    if flip<(len(fliplist)-3) and fliplist[flip] == fliplist[flip+1]and fliplist[flip] == fliplist[flip+2]:
        numberOfStreaks3 = numberOfStreaks3 + 1

    if flip<(len(fliplist)-4) and fliplist[flip] == fliplist[flip+1]and fliplist[flip] == fliplist[flip+2] and fliplist[flip] == fliplist[flip+3]:
        numberOfStreaks4 = numberOfStreaks4 + 1


    # Code that checks if there is a streak of 6 heads or tails in a row.
#print(fliplist)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))

#check number of streaks for x amounts
print('6 streak', numberOfStreaks)
print('2 streak', numberOfStreaks2)
print('3 streak', numberOfStreaks3)
print('4 streak', numberOfStreaks4)
